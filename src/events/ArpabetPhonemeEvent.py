from src.events.AbstractEvent import AbstractEvent
from src.helpers.Logger import Logger
from src.models.request_data import PhonemeTransformRequest
# from src.models.EventTypeEnum import EventType

import nltk


class ArpabetPhonemeEvent(AbstractEvent):
    """
    Transforms an English sentence into phonemes
    """

    def __init__(self):
        try:
            self.arpabet = nltk.corpus.cmudict.dict()
        except LookupError:
            nltk.download('cmudict')
            self.arpabet = nltk.corpus.cmudict.dict()

    def handle(self, event_type, request_data: AbstractEvent):
        # TODO will probably have to change this in the future
        if type(request_data) != type(PhonemeTransformRequest):
            raise ValueError("ArpabetPhonemeEvent.handle: request_data is of type " + str(type(request_data)))

        request_data.sentences = []
        for sentence in request_data.sentences:
            sentence_in_phonemes = []
            for word in sentence.split():
                try:
                    sentence_in_phonemes.append(self.arpabet[str(word).lower()])
                except KeyError:
                    # Continue processing, but log error
                    Logger.log_warning("ArpabetPhonemeEvent.handle: Word '" + str(word).lower()
                                       + "' was not found in Arpabet dictionary.")

            request_data.sentences.append(sentence_in_phonemes)

        print(request_data.sentences)
