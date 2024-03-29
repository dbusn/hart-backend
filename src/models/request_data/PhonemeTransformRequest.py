from typing import List, Dict, Any, Union

from definitions import RESOURCES
from src.helpers.LoadPhonemeJsonHelper import get_phoneme_patterns
from src.models.EventTypeEnum import EventType
from src.models.request_data.AbstractRequest import AbstractRequest


def split_sentences(sentences: List[str]) -> List[List[str]]:
    """
    Helper function to split sentences.
    @param sentences    List of sentences in form ["sentence one", "sentence two"].
    @returns            List of sentences where every sentence is divided into a list of words.
    """

    # the split sentences
    split_sen = []

    # loop through sentences
    for sentence in sentences:
        split_sen.append(sentence.split())

    return split_sen


class PhonemeTransformRequest(AbstractRequest):
    """
    Request type for a transformation that includes a phonemes transformation.
    """

    # List of sentences in which each sentence is divided into a list of words.
    sentences: List[List[str]]

    # Mapping of phoneme to the JSON pattern
    phoneme_patterns: Dict[str, Dict[str, Any]]

    # List of sentences, which are lists of words,
    # with every word being a list of decompositions,
    # with each decomposition being list of phoneme-strings.
    # created by PhonemeDecompositionEvent
    phonemes: List[List[List[List[str]]]]

    # the phoneme decompositions that were sent to the prototype
    # created by SendPhonemesToPrototypeEvent
    sent_phonemes: List[List[str]]

    def __init__(self, sentences: Union[List[str], List[List[str]]] = None,
                 phonemes: List[str] = None):
        """
        Constructor to make object for sentence processing or phoneme processing. This constructor has 2 purposes:
            (1) To create a PhonemeTransformRequest with the purpose of processing sentences into phonemes and sending
                    those to the microcontroller.
            (2) To create a PhonemeTransformRequest with the purpose of sending phonemes to the microcontroller.

        Function throws an error when both the sentences and phonemes parameter are filled.

        @param sentences            Text to process, either (1) list of strings, or (2) list of list of strings in the
                                        following form
                                            (1) ["first sentence", "second sentence"]
                                            (2) [["first", "sentence"], ["second", "sentence"]]
        @param phonemes             Phonemes to be send to the prototype in form
                                        ["PHO1", "PHO2"]
                                        
        @raises ValueError          If both sentences and phonemes are filled with data or when phoneme_patterns is
                                        None.
        """
        if sentences is not None and phonemes is not None:
            raise ValueError("PhonemeTransformRequest.__init__: both sentences and phonemes parameter was passed.")

        # set phoneme pattern
        self.phoneme_patterns = get_phoneme_patterns(RESOURCES)

        if phonemes is not None:
            # Creation for purpose 2
            # Phonemes is not None, thus sentences is None

            self.sentences = None
            self.phonemes = [[[phonemes]]]
        else:
            # Creation for purpose 1
            # Phonemes is None

            if sentences is None:
                # let sentences field be populated later or not at all
                sentences = []

            elif len(sentences) == 0:
                # if sentences is [] skip potentially splitting of next elif
                pass

            elif isinstance(sentences[0], str):
                # if list of strings, split strings
                sentences = split_sentences(sentences)

            self.sentences = sentences

    def get_event_type(self) -> EventType:
        if self.sentences is None:
            # if sentences is None, then we want to send phonemes to the microcontroller.
            return EventType.SEND_PHONEMES_TO_MICROCONTROLLER
        else:
            # fi sentences is not None, then we want to do a full processing process.
            return EventType.SEND_SENTENCES_TO_MICROCONTROLLER
