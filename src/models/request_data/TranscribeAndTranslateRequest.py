from typing import List, BinaryIO

from src.models.EventTypeEnum import EventType
from src.models.request_data.AbstractRequest import AbstractRequest


class TranscribeAndTranslateRequest(AbstractRequest):
    """
    Request type for a transformation that includes a transcription from an Audio file to sentences.
    """

    # audio file
    audio_file: BinaryIO

    # Type of audio file (e.g. "audio/flac")
    audio_type: str

    # Spoken language
    source_language: str

    # The target language code
    target_language: str

    # Transcription
    original_sentences: List[str]

    # Stores the translated sentences after translation
    translated_sentences: List[str]

    # The original language code of the sentences
    source_language: str

    def __init__(self,
                 audio_file: BinaryIO = None,
                 audio_type: str = None,
                 original_sentences: List[str] = None,
                 source_language: str = None,
                 target_language: str = 'en'):
        """
        Constructor to make object for transcribing and/or translating text/sentences. This constructor has 2 purposes:
            (1) To create a TranscribeAndTranslateRequest with the purpose of transcribing
                an audiofile and then translating.
            (2) To create a TranscribeAndTranslateRequest with the purpose of translating
                given sentences.

        Function throws an error when neither audiofile or original_sentences are set. If both are set, it
        eventually overwrites the given sentences with the transcription.

        @param audio_file           Bitewise fileobject of flac file.
        @param audio_type           String containing the type of audio (mimeType) submitted (i.e. 'audio/webm').
        @param original_sentences   ["list of sentences", "as strings each"].
        @param source_language      String containing the code of the source_language.
        @param target_language      String containing the code of the target_language.

        @raises ValueError          If neither audio_file and original_sentences filled 
                                    or when source_language is None
        """

        # source language needs to be set
        if not source_language:
            raise ValueError("TranscribeAndTranslateRequest.__init__: no source language passed.")

        # set source and goal language of transformation
        self.source_language = source_language
        self.target_language = target_language

        # either set audio_file, to be translated sentences, or throw error
        if audio_file:
            self.audio_file = audio_file
            self.audio_type = audio_type
            self.original_sentences = None
        elif original_sentences:
            self.original_sentences = original_sentences
            self.audio_type = None
            self.audio_file = None
        else:
            raise ValueError("TranscribeAndTranslateRequest.__init__: no audio file or sentences passed.")

    def get_event_type(self) -> EventType:
        # return event type for transcription and translation if source is an audio file
        if self.audio_file is not None:
            return EventType.TRANSCRIBE_AND_TRANSLATE_USING_GOOGLE_API
        # return event type for translation if source is sentences
        elif self.original_sentences is not None:
            return EventType.TRANSLATE_USING_GOOGLE_API
        else:
            raise ValueError("TranscribeAndTranslateRequest.get_event_type(): no audio file or sentences, illegal "
                             "state.")
