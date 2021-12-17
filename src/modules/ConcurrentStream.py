from __future__ import division

import re
import sys

from definitions import API_BASE_URL, RESOURCES

from google.cloud import speech

import pyaudio
from six.moves import queue
from flask import request, jsonify
from src.helpers.Logger import Logger
from src.models.request_data.PhonemeTransformRequest import PhonemeTransformRequest
from src.models.request_data.TranscribeAndTranslateRequest import TranscribeAndTranslateRequest
from src.handlers.Dispatcher import Dispatcher

import threading

dispatcher = Dispatcher()


# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


class ConcurrentStream:
    """
    Interface for using the concurrent google cloud stream.
    """

    class toggle:
        """
        Datatype for a mutable boolean to stop the thread from the outside.
        """
        def __init__(self, val):
            self.value = val

        def set(self, val: bool):
            self.value = val

        def get(self):
            return self.value

    def __init__(self):
        # state
        self.is_on = self.toggle(False)

        # thread for processing
        self.th = None

    def start(self):
        self.is_on.set(True)

        self.th = threading.Thread(target=start_process,  args=(self.is_on,))
        self.th.start()

    def stop(self):
        self.is_on.set(False)
        Logger.log_info("ConcurrentStream: joining threads.." )
        self.th.join()
        Logger.log_info("ConcurrentStream: threads joined." )

    def get_state(self) -> bool:
        """
        Returns bool denoting whether stream is live or not.
        """
        return self.is_on.get()


class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)

        Logger.log_warning("ConcurrentStream: Generator has stopped. This is the not expected exit-event.")

def send_transcription_loop(responses, killswitch):
    """Iterates through server responses and prints them.

    The responses passed is a generator that will block until a response
    is provided by the server.

    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.

    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    num_chars_printed = 0
    for response in responses:
        if not killswitch.get():
            # If the killswitch is false, we should stop reading the generator. 
            break

        print('response came in on thread')
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript

        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        #
        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result

        overwrite_chars = " " * (num_chars_printed - len(transcript))

        # result.is_final tells us whether the Google algorithm thinks the sentence is finished
        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + "\r")
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            result_text = transcript + overwrite_chars
            print(result_text)
            # send transcript + overwrite_chars to dispatcher

            # issue translate event
            # translate_bool = False
            # if translate_bool:
            #     translate_request = TranscribeAndTranslateRequest(original_sentences=transcript+overwrite_chars,
            #                                                        source_language="nl-NL")
            #     try:
            #         translate_request = dispatcher.handle(translate_request)
            #     except RuntimeError:
            #         message = API_BASE_URL + "/microcontroller/sentences: Could not handle TranslateRequest successfully."
            #         Logger.log_error("ConcurrentStream.send_transcription_loop - " + message)
            #         return message, 500
            #     result = {
            #         "sentences": translate_request.original_sentences,
            #         "translation": translate_request.translated_sentences,
            #     }
            #     decomposition_request_translated = PhonemeTransformRequest(sentences=result["translation"])
            #     try:
            #         dispatcher.handle(decomposition_request_translated)
            #     except RuntimeError:
            #         message = API_BASE_URL + "/microcontroller/audiopath: Could not handle PhonemeTransformRequest successfully."
            #         Logger.log_error("ConcurrentStream.send_transcription_loop - " + message)
            #     return message, 500

            # Issue decomposition into phonemes and sending to microcontroller

            result_list = []
            result_list.append(result_text) #maybe make mod 10 iterator to save the context of the sentences
            decomposition_request = PhonemeTransformRequest(sentences=result_list)

            # The Dispatcher instance will try to handle all the required events for translation
            # If unsuccessful, we will log an error message. 
            try:
                dispatcher.handle(decomposition_request)
            except RuntimeError:
                message = API_BASE_URL + "/microcontroller/sentences: Could not handle PhonemeTransformRequest successfully."
                Logger.log_error("ConcurrentStream.send_transcription_loop - " + message)
                return message, 500



            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                print("Exiting..")
                break

            num_chars_printed = 0


def start_process(kill_switch):
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    """Initializes the microphone in the backend and the required threads
    when toggle_stream is triggered by a frontend request. 
    
    By using the state of the microphone (on/off) whose state can be changed 
    by requests from the Frontend, the microphone stream and transcription loop 
    will automatically terminate when kill_switch is False."""
    language_code = "en-US"  # a BCP-47 language tag

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config, interim_results=True
    )

    with MicrophoneStream(RATE, CHUNK) as stream:
        
        audio_generator = stream.generator()
        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        # Code terminates when kill_swith == False
        send_transcription_loop(responses, kill_switch)
