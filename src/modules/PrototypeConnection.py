import bluetooth
from serial import Serial

from src.helpers.Logger import Logger
from src.helpers.SingletonHelper import Singleton
from definitions import CONNECTED_TO_PROTOTYPE, CONNECTED_VIA_BLUETOOTH, BAUDRATE, RUNNING_ON_MAC

from typing import Dict, Any, List

import serial
import serial.tools.list_ports

import json
import copy


class PrototypeConnection(metaclass=Singleton):
    """
    Represents the connection (via bluetooth) with the prototype.
    """

    # configured
    configured: bool = False

    # maps coord in the phoneme pattern jsons to the id of the motor from prototype
    mapping: Dict[int, int]

    # whether backend in debug (so no connected prototype)
    debug: bool

    # baudrate for connection to sleeve
    baudrate: int

    # Connection to the sleeve
    device: Serial

    # list of serials of known microcontrollers (should include current connected microcontroller)
    serials: List[str]

    # Name of bluetooth device to connect to
    bluetooth_device_name: str

    def __init__(self):
        pass

    def connect_with_config(self, fp_json: str):
        """
        Establish connection with prototype.

        param fp_json: filepath to JSON with prototype specific settings.
        """

        # load json file
        with open(fp_json, 'r') as f:
            json_config = json.load(f)

        # parse data from config json
        self.parse_config_JSON(json_config)

        # set found device if not in backend-debug mode
        if not self.debug:
            try:
                if CONNECTED_VIA_BLUETOOTH:
                    if not RUNNING_ON_MAC:
                        port = self.find_bluetooth_port_windows(self.bluetooth_device_name)
                    else:
                        port = "/dev/tty." + self.bluetooth_device_name + "-SPPDev"
                else:
                    port = self.find_outgoing_communication_port()

                Logger.log_info("Connecting to port: " + port)

                self.device = serial.Serial(port, baudrate=self.baudrate, timeout=5)

                Logger.log_info("Connection is open: " + str(self.device.is_open))
            except Exception as e:
                Logger.log_warning("Prototype connection NOT successfully created! " + str(e))
                if CONNECTED_VIA_BLUETOOTH:
                    Logger.log_warning("First, make sure that your bluetooth is on!")
                    Logger.log_warning(
                        "Additionally, for the bluetooth connection it might help to restart the prototype.")
                self.configured = False
                return
        else:
            Logger.log_info("PrototypeConnection initialized in debug mode.")

        self.configured = True

    def close_connection(self):
        if hasattr(self, 'device'):
            self.device.close()

    def parse_config_JSON(self, config):
        """
        parse the config json file.

        param config_file: JSON dictionary with prototype specific settings.
        """

        # get mapping of motor coord to id
        self.mapping = {}
        for pair in config['mapping']:
            self.mapping[pair['coord']] = pair['id']

        # serials of known microcontrollers
        self.serials = config['serial_numbers']

        # baudrate that is used in prototype
        self.baudrate = BAUDRATE

        # debug mode or not
        self.debug = not CONNECTED_TO_PROTOTYPE

        self.bluetooth_device_name = config['bluetooth_device_name']

    def find_outgoing_communication_port(self) -> Any:
        """
        Finds the first outgoing communication port with known connected microcontroller.
        """

        # run through ports to find matching serial-number
        for port_info in serial.tools.list_ports.comports():

            # if serial number of connection port is familiar
            if port_info.serial_number in self.serials:
                return port_info.device
        else:
            raise IOError('PrototypeConnection.find_outgoing_communication_port: Could not find a known connected '
                          'microcontroller, is it plugged in and set as known serial number?')

    def send_pattern(self, pattern_JSON: Dict[str, Any]):
        """
        Send a phoneme pattern to prototype.
        """

        # check if connection is configured
        if not self.configured:
            raise Exception("PrototypeConnection.send_pattern: Illegal state, "
                            "attempt to send pattern to prototype without it being configured.")

        # deep copy json as to prevent overwriting mapping
        mapped_pattern_JSON = copy.deepcopy(pattern_JSON)

        # map from coords to ids
        for i in range(len(mapped_pattern_JSON['pattern'])):
            for j in range(len(mapped_pattern_JSON['pattern'][i]['iteration'])):
                # translate coordinate (in pattern json) to ids of iteration of prototype (in config json)
                mapped_pattern_JSON['pattern'][i]['iteration'][j]['coord'] = self.mapping[
                    mapped_pattern_JSON['pattern'][i]['iteration'][j]['coord']]

        # send to prototype
        self.query(json.dumps(mapped_pattern_JSON, indent=4, sort_keys=True))

    def query(self, message: str) -> str:
        """
        Generic string query to the prototype.
        """

        # check if configured
        if not self.configured:
            raise Exception("PrototypeConnection.query: Illegal state, "
                            "attempt to send pattern to prototype without it being configured.")

        # Send message to prototype.
        if not self.debug:
            try:
                self.device.flushInput()

                self.device.write(message.strip().encode())

                # Make sure the prototype always gives an output, otherwise Python will wait forever.
                prototype_log = self.device.readline().decode()

                # Split the log for readability
                prototype_log = prototype_log.split("\r")

                # Flush input
                self.device.flushInput()

                # Log what the prototype has returned
                Logger.log_info("Prototype says: ")
                for log in prototype_log:
                    Logger.log_info(log)
            except Exception as e:
                Logger.log_warning(
                    "PrototypeConnection.query: error occurred during sending. Complete error: " + str(e))
                prototype_log = "PrototypeConnection.query: Prototype could not be obtained."

        else:
            Logger.log_info("PrototypeConnection.query: A query would have now arrived at the prototype.")
            prototype_log = "Debug log"

        return prototype_log

    def find_bluetooth_port_windows(self, bluetooth_device_name: str):
        """
        Functionality to find the bluetooth COM port corresponding to a given bluetooth device name for
        windows operating system. Does not work if bluetooth device was never paired before.
        :param bluetooth_device_name:   Name of the bluetooth device to find the COM port for.
        :return:                        String containing the COM port.
        """
        Logger.log_info("Searching for windows com port corresponding to bluetooth chip with name "
                        + bluetooth_device_name)

        mac = None

        # Find all com ports on device, and include names
        nb = bluetooth.discover_devices(lookup_names=True)

        # Loop over ports to check if device in question is in there.
        for address, name in list(nb):
            if bluetooth_device_name == name:
                mac = address
                Logger.log_info("MAC address to connect to: " + str(mac))
                break

        if mac is not None:
            # Get a list of COM ports
            com_ports = list(serial.tools.list_ports.comports())
            stripped_mac = mac.replace(":", "")

            # Loop over ports, and check which one corresponds to the MAC address
            for COM, _, hwid in com_ports:
                if stripped_mac in hwid:
                    return COM

            # Nothing corresponding was found, log warning and return
            Logger.log_warning("Could not find com port corresponding to found MAC address")
            return None
        else:
            # MAC address was not found, so user most likely has never yet paired their device with the sleeve.
            Logger.log_warning("MAC address of given bluetooth chip name could not be determined.")
            Logger.log_warning("Make sure to pair the computer to the bluetooth chip if you are using it "
                               "for the first time")
            return None
