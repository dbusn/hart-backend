import queue

from src.handlers.Dispatcher import Dispatcher
from src.helpers.Logger import Logger

from flask_socketio import send, emit

# we're being ugly and handling the google cloud calls in the socket handler
from google.cloud import speech

# hail mary for threading
from threading import Thread

# get the socketio instance from the main file
try:
    from __main__ import socketio
except ImportError:
    from app import socketio

# set Dispatcher
dispatcher = Dispatcher()

# Buffer queue that holds the audio of the stream in a thread-safe way. 
# _generator() yields from this queue, such that it does not block the program
_buff = queue.Queue()
thread1 = None

@socketio.on('connect')
def test_connect(auth):
    Logger.log_info("Socket connected - Audio Stream started")
    emit('connect response', {'message': 'Connected!'})

    # TODO get language from frontend input
    language = "nl-NL"  # a BCP-47 language tag
    global thread1
    thread1= Thread(target=_streamToCloud, args = (language, ))
    thread1.start()

@socketio.on('disconnect')
def test_disconnect():
    Logger.log_info("Socket Disconnected - Audio Stream stopped")
    # this will end the generator
    _buff.put(None)
    thread1.join()

@socketio.on('stream')
def handle_message(data):
    Logger.log_info('Received blob {} of size{}'.format(data['order'], data['size']))
    
    # get the audio chunk in bytes
    chunk = data['data']

    # put the audio bytes in the queue
    _buff.put(chunk)


'''
yields, when availabe, a chunk of audio from the queue, 
and stops iteration if queue has None object
'''
def _generator():
    # Use a blocking get() to ensure there's at least one chunk of
    # data, and stop iteration if the chunk is None, indicating the
    # end of the audio stream.
    global _buff
    chunk = _buff.get()
    if chunk is None:
        print('chunk is None')
        return
    data = [chunk]

    # Now consume whatever other data's still buffered.
    while True:
        try:
            print('waiting for buff')
            chunk = _buff.get(block=False)
            if chunk is None:
                return
            data.append(chunk)
        except queue.Empty:
            print("queue empty")
            break

    print('yielding')
    yield b"".join(data)

'''
Handles the transcription of the stream in gcloud
'''
def _streamToCloud(language_code):
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language_code,
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config, interim_results=False
    )

    audio_generator = _generator()
    requests = (
        speech.StreamingRecognizeRequest(audio_content=content)
        for content in audio_generator
    )

    responses = client.streaming_recognize(streaming_config, requests)

    # Now, put the transcription responses to use.
    _pushResults(responses)

'''
Sends events with definite transcription results to Dispatcher
'''
def _pushResults(responses):
    """Iterates through server responses and prints them.

    The responses passed is a generator that will block until a response
    is provided by the server.

    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.
    """
    for response in responses:
        Logger.log_info("RESPONSE")
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
        Logger.log_info(transcript)
    
Logger.log_info("Socket Handlers initialized")