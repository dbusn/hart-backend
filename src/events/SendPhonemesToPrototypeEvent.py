from src.models.EventTypeEnum import EventType
from src.events.AbstractEvent import AbstractEvent
from src.helpers.Logger import Logger
from src.models.request_data.AbstractRequest import AbstractRequest
from src.modules.PrototypeConnection import PrototypeConnection

from typing import List


class SendPhonemesToPrototypeEvent(AbstractEvent):
    """
    Event that sends given phonemes to prototype.

    expects request_data to have attribute "phonemes" which is a 3 dimensional list of strings:
    list of words, with every word being a list of decomposition, with each decomposition being list of phoneme-strings.
    """

    PRIORITY: int = 90

    def __init__(self):
        pass

    def handle(self, request_data: AbstractRequest):
        # for each sentence
        request_data.sent_phonemes = []

        for sentence in request_data.phonemes:
            # for each list of possible phoneme deconstructions of word
            for word in sentence:

                # find the first phoneme deconstruction that is valid
                valid_deconstruction = False
                i = 0

                while not valid_deconstruction and i != len(word):
                    # assume deconstruction is valid until proven otherwise
                    valid_deconstruction = True

                    # check for every phoneme if it is known
                    for phoneme in word[i]:
                        # check if phoneme is known
                        if phoneme not in request_data.phoneme_patterns.keys():
                            # not known, continue to next word
                            valid_deconstruction = False
                            i += 1
                            break

                # if a valid deconstruction is found, send it to the prototype
                if valid_deconstruction:
                    Logger.log_info("SendPhonemesToPrototypeEvent.handle: Sending word consisting of phonemes {}"
                                    .format(word[i]))

                    # send phonemes to the prototype
                    for phoneme in word[i]:
                        PrototypeConnection().send_pattern(request_data.phoneme_patterns[phoneme])
                        # TODO save data somewhere here to a database/csv

                        # add the fulfilled effect to the result field
                    request_data.sent_phonemes.append(word[i])
                else:
                    # one word was not decomposed in recognizable phonemes, log warning and skip
                    Logger.log_warning("SendPhonemesToPrototypeEvent.handle: non of the phoneme deconstructions " +
                                       "consisted of known phonemes: {}".format(word))

        return request_data

    @staticmethod
    def get_priority() -> int:
        return SendPhonemesToPrototypeEvent.PRIORITY

    @staticmethod
    def get_compatible_events() -> List[EventType]:
        return [
            EventType.SEND_SENTENCES_TO_MICROCONTROLLER,
            EventType.SEND_PHONEMES_TO_MICROCONTROLLER
        ]
