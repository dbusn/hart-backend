import os

"""
Which sleeve is connected, and thus which settings should be loaded.

options:
    "old_sleeve.json"
    "s_sleeve.json"
    "m_sleeve.json"
    "l_sleeve.json"
"""
CONFIG_FILE_NAME = "old_sleeve.json"

# Whether the frontend is compiled and located in backend or not
DISTRIBUTION = False

# Whether the prototype is connected or not
CONNECTED_TO_PROTOTYPE = False

# If prototype is connected, is it connected by bluetooth, or by cable (also depends on the software on the
#       microcontroller
CONNECTED_VIA_BLUETOOTH = True

# Dont touch this if you don't know what this is :P
BAUDRATE = 115200

# Probably don't want to touch this :P
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # this is the project root

# Shouldn't change
RESOURCES = os.path.join(ROOT_DIR, "resources")

API_BASE_URL = "/api/v1"