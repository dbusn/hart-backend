from src.events.SendPhonemesToPrototypeEvent import SendPhonemesToPrototypeEvent
from src.models.request_data.PhonemeTransformRequest import PhonemeTransformRequest
from src.modules.PrototypeConnection import PrototypeConnection

from definitions import ROOT_DIR

import os

connection = PrototypeConnection()\
                .connect_with_config(os.path.join(ROOT_DIR, 'test', 'resources', 'prototype_config_test.json'))


def test_handle_basic_case_1():
    ptr = PhonemeTransformRequest(phonemes=["H"])

    request_data = SendPhonemesToPrototypeEvent().handle(ptr)

    print(request_data.sent_phonemes)

    assert request_data.sent_phonemes[0][0] == "H"
