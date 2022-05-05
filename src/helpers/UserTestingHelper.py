import json
import os
import random

from src.helpers.Logger import Logger


class UserTestingHelper:
    """
    Helper class for user testing
    """

    all_patterns = []

    def __init__(self):
        """
        Initialize the helper class
        """
        self.read_patterns()

    # Read all the available patterns
    def read_patterns(self):
        if os.path.exists(os.path.join('resources', 'experiment_patterns')):
            for pattern_file in os.listdir(os.path.join('resources', 'experiment_patterns')):
                if pattern_file[-5::] != '.json':
                    Logger.log_warning(f"{pattern_file} in \\resources\\phonemepatterns\\ is not a .json, ignoring! ")
                else:
                    # get phoneme name
                    phoneme = pattern_file.replace('.json', '')
                    self.all_patterns.append(phoneme)
        else:
            Logger.log_error('resources/experiment_patterns directory does not exist!')


    # Returns a randomly chosen pair of patterns and removes it from the pool of all patterns
    def get_random_pair(self):
        patterns = {}

        # First pattern
        pattern_a = self.all_patterns.pop(random.randint(0, len(self.all_patterns) - 1))
        # Second pattern
        pattern_b = self.all_patterns.pop(random.randint(0, len(self.all_patterns) - 1))

        # Read the first and the second patterns
        with open(os.path.join('resources', 'experiment_patterns', pattern_a) + '.json', 'r') as f:
            pattern_a_json = json.load(f)
        patterns[pattern_a] = pattern_a_json

        with open(os.path.join('resources', 'experiment_patterns', pattern_b) + '.json', 'r') as f:
            pattern_b_json = json.load(f)
        patterns[pattern_b] = pattern_b_json

        Logger.log_info(f"Selected random pair of patterns: ({pattern_a}, {pattern_b})")

        return patterns
