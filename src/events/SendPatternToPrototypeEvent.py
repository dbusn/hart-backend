import json
import os
from typing import List

from definitions import CONNECTED_TO_PROTOTYPE, RESOURCES
from src.events.AbstractEvent import AbstractEvent
from src.helpers.Logger import Logger
from src.models.EventTypeEnum import EventType
from src.models.request_data.AbstractRequest import AbstractRequest
from src.modules.PrototypeConnection import PrototypeConnection


class SendPatternToPrototypeEvent(AbstractEvent):
    """
    Event that sends given any pattern to prototype.

    expects request_data to have attribute "phonemes" which is followed by a filename of the pattern to send.
    """

    # Priority equal to sending a phoneme to the prototype
    PRIORITY: int = 90

    def __init__(self):
        pass

    def handle(self, request_data: AbstractRequest):
        # for each sentence
        request_data.sent_phonemes = []

        pattern_id = request_data.patterns[0]
        Logger.log_info("Request to send Pattern ID: {} obtained".format(pattern_id))
        pattern_path = (
            os.path.join(RESOURCES, "experiment_patterns", pattern_id) + ".json"
        )

        if not os.path.isfile(pattern_path):
            Logger.log_error(
                "SendPatternToPrototypeEvent.handle: Sending pattern {} failed: No file found".format(
                    pattern_id
                )
            )
            return request_data
        else:
            Logger.log_info(
                "SendPatternToPrototypeEvent.handle: Sending pattern {}".format(
                    pattern_id
                )
            )

            # Load the JSON file
            with open(pattern_path, "r") as f:
                pattern_json = json.load(f)

            # send phonemes to the prototype
            if CONNECTED_TO_PROTOTYPE:
                PrototypeConnection().send_pattern(pattern_json)

            # add the fulfilled effect to the result field
            request_data.sent_phonemes.append(pattern_id)

        return request_data

    @staticmethod
    def get_priority() -> int:
        return SendPatternToPrototypeEvent.PRIORITY

    @staticmethod
    def get_compatible_events() -> List[EventType]:
        return [
            EventType.SEND_PATTERN_TO_MICROCONTROLLER,
        ]
