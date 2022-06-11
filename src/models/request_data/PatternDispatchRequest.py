from typing import Any, Dict, List, Union

from definitions import RESOURCES
from src.helpers.LoadPhonemeJsonHelper import get_phoneme_patterns
from src.models.EventTypeEnum import EventType
from src.models.request_data.AbstractRequest import AbstractRequest


class PatternDispatchRequest(AbstractRequest):
    """
    Request type for dispatching a non-phoneme pattern to the prototype.
    """

    # TODO Make sure SendPatternToPrototypeEvent.handle works with these variables:

    # Mapping of phoneme to the JSON pattern
    patterns: str

    # created by SendPhonemesToPrototypeEvent
    sent_phonemes: List[List[str]]

    def __init__(self, pattern_name: List[str] = None):
        """
        # TODO Update this docstring.
        Constructor to make object for sentence processing or phoneme processing. This constructor has 2 purposes:
            (1) To create a PhonemeTransformRequest with the purpose of processing sentences into phonemes and sending
                    those to the microcontroller.
            (2) To create a PhonemeTransformRequest with the purpose of sending phonemes to the microcontroller.

        Function throws an error when both the sentences and phonemes parameter are filled.

        @param pattern_name            Name of the pattern to send to the prototype in the form of List[str].

        @raises ValueError          If both sentences and phonemes are filled with data or when phoneme_patterns is
                                        None.
        """
        if pattern_name is None:
            raise ValueError("PhonemeTransformRequest.__init__: both sentences and phonemes parameter was passed.")

        self.patterns = [[[]]]

        if pattern_name is not None:
            self.patterns = pattern_name

    def get_event_type(self) -> EventType:
        return EventType.SEND_PATTERN_TO_MICROCONTROLLER
