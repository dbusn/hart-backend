import json
import os

from src.helpers.Logger import Logger
from src.models.CMUPhonemes import REEDPhonemes


def get_phoneme_patterns(resources: str, user_testing=False):
    """
    load the phoneme patterns
    """

    patterns = {}
    final_dir = 'phoneme_patterns' if user_testing is False else 'experiment_patterns'

    # loop through available phoneme patterns
    for pattern_file in os.listdir(os.path.join(resources, final_dir)):
        # pattern file should be json
        if pattern_file[-5::] != '.json':
            Logger.log_warning(f"{pattern_file} in \\resources\\phonemepatterns\\ is not a .json, ignoring! ")
        else:
            # get phoneme name
            phoneme = pattern_file.replace('.json', '')

            # CMUPhonemes are the phonemes supported in nltk.cmudict()
            # if not (phoneme in REEDPhonemes):
            #     raise NameError('The resource ' + phoneme + '.json is not a valid phoneme name')

            # load all patterns. This means if change of patterns, restart
            with open(os.path.join(resources, final_dir, pattern_file), 'r') as f:
                json_pattern = json.load(f)
            patterns[phoneme] = json_pattern

    return patterns
