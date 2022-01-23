import os

"""
Which sleeve is connected, and thus which settings should be loaded.

options:
    "old_sleeve.json"
    "s_sleeve.json"
    "m_sleeve.json"
    "l_sleeve.json"
"""
CONFIG_FILE_NAME = "m_sleeve.json"

# Whether the frontend is compiled and located in backend or not
DISTRIBUTION = False

# Whether the prototype is connected or not
CONNECTED_TO_PROTOTYPE = True

# If prototype is connected, is it connected by bluetooth, or by cable (also depends on the software on the
#       microcontroller
CONNECTED_VIA_BLUETOOTH = True

RUNNING_ON_MAC = False

# Dont touch this if you don't know what this is :P
BAUDRATE = 115200

# Probably don't want to touch this :P
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # this is the project root

# Shouldn't change
RESOURCES = os.path.join(ROOT_DIR, "resources")

"""
Mac addresses
    "00:19:08:36:22:1B"
    "00:19:08:36:54:d4"
"""

API_BASE_URL = "/api/v1"