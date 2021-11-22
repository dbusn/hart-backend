from src.helpers.Logger import Logger
from src.helpers.SingletonHelper import Singleton
from definitions import CONNECTED_TO_PROTOTYPE, CONNECTED_VIA_BLUETOOTH, BAUDRATE

from typing import Dict, Any, List

import serial
import serial.tools.list_ports
import winreg
import bluetooth

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

    # baudrate for connected Teensy
    baudrate: int

    # list of serials of known microcontrollers (should include current connected microcontroller)
    serials: List[str]

    #  Stores the COM port for connecting with bluetooth if done manually
    com_port: str

    # list of known MAC addresses of HC-05 bluetooth module chips
    known_bluetooth_mac_addresses: List[str]

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
                    if self.com_port is None:
                        if len(self.known_bluetooth_mac_addresses) == 1:
                            mac = self.known_bluetooth_mac_addresses[0]
                        else:
                            mac = self.find_in_reach_bluetooth_known_mac()
                        port = self.get_spp_com_port(mac)
                    else:
                        port = self.com_port
                else:
                    port = self.find_outgoing_communication_port()

                Logger.log_info("Connecting to port: " + port)

                self.device = serial.Serial(port, baudrate=self.baudrate, timeout=5)
                Logger.log_info("Connection is open: " + str(self.device.is_open))
            except Exception as e:
                Logger.log_warning("Prototype connection NOT successfully created! " + str(e))
                if CONNECTED_VIA_BLUETOOTH:
                    Logger.log_warning("First, make sure that your bluetooth is on!")
                    Logger.log_warning("Additionally, for the bluetooth connection it might help to restart the prototype.")
                self.configured = False
                return

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

        # Reads known bluetooth mac addresses
        self.known_bluetooth_mac_addresses = config['known_bluetooth_mac_addresses']

        # Reads (possible) manually set bluetooth com port
        self.com_port = config['bluetooth_com_port']

        # baudrate that is used in prototype
        self.baudrate = BAUDRATE

        # debug mode or not
        self.debug = not CONNECTED_TO_PROTOTYPE

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

    # Windows registry location storing bluetooth details
    key_bthenum = r"SYSTEM\CurrentControlSet\Enum\BTHENUM"

    def find_in_reach_bluetooth_known_mac(self):
        """
        Looks around for discoverable bluetooth devices and returns the mac address of a discoverable bluetooth device
        of which the mac address is known and in the prototype configurations file.
        :return: String containing MAC address.
        """
        Logger.log_info("PrototypeConnection.find_in_reach_bluetooth_known_mac: Looking for devices")

        # sometimes bluetooth.discover_devices() fails to find all the devices
        for i in range(3):
            nearby_devices = bluetooth.discover_devices()

            for mac in nearby_devices:
                if mac in self.known_bluetooth_mac_addresses:
                    return mac

            Logger.log_info("PrototypeConnection.find_in_reach_bluetooth_known_mac: "
                            "Try one more time to find target device..")

    def get_spp_com_port(self, bt_mac_addr):
        bt_mac_addr = bt_mac_addr.replace(':', '').upper()
        for i in self.gen_enum_key('', 'LOCALMFG'):
            for j in self.gen_enum_key(i, bt_mac_addr):
                subkey = self.key_bthenum + '\\' + i + '\\' + j
                port = self.get_reg_data(subkey, 'FriendlyName')
                assert ('Standard Serial over Bluetooth link' in port[0])
                items = port[0].split()
                port = items[5][1:-1]
                return port

    def gen_enum_key(self, subkey, search_str):
        hKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.key_bthenum + '\\' + subkey)

        try:
            i = 0
            while True:
                output = winreg.EnumKey(hKey, i)
                if search_str in output:
                    yield output
                i += 1

        except:
            pass

        winreg.CloseKey(hKey)

    def get_reg_data(self, subkey, name):
        hKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                              subkey)
        output = winreg.QueryValueEx(hKey, name)
        winreg.CloseKey(hKey)
        return output
