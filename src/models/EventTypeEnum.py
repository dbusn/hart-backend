from enum import Enum


class EventType(Enum):
    """
    Enum for all event types.
    """

    COMPLETE_GOOGLE_API_PHONEME_TRANSFORMATION = 1,
    TRANSFORM_TEXT_INTO_PHONEMES = 2,
    TRANSCRIBE_USING_GOOGLE_API = 3,
    TRANSLATE_USING_GOOGLE_API = 4,
    SEND_PHONEME_TO_MICROCONTROLLER = 5,
