# This is a python OBD Module Used to communicate with an OBDII device
# Over Serial

import serial

# Init Port
ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 9600
    )

# OBD Commands for ELM327
reset_obd = 'ATZ'
check_voltage = 'ATRV'
init_obd = 'STP01'
list_commands = '0100'
rpm = '010c'

class ODB:
    """
    A Simple class for controlling ELM327 based OBD Scanners
    """

    def __init__(self, port_name):
        # Initilize the Port
        self.data = []
        self.baud_rate = 9600
        self.data_bits = 8
        self.stop_bits = 1
        self.line_ending = 'CR'
        self.elmchar = '>'
        self.obdcmds = {}

        try:
                # Attempt to Open Port
                self.ser.setBaudrate = self.baud_rate
                self.ser.port = port_name

                if os == 'win32':
                    self.ser = serial.Win32Serial()
                    self.ser.open()
                else:
                    self.ser = serial.Serial(
                        port = port_name,
                        baudrate = self.baud_rate
                        )
                ### Sleep necessary to prevent race condition ###
                sleep(.3)
        except serial.SerialException() as e:
                print 'Error'
                print e

        return None


    def close_port(self):
        self.ser.close()

    def readobd(self):
        return None

    def readline(self):
        """
        Read line from ELM327
        """
        buffer = ''
        retcmd = ''
        if self.ser.inWaiting() != 0:
            buffer += self.ser.read(self.ser.inWaiting())
        if self.elmchar in buffer:
            # TODO: Fix the buffer with correct information
            retcmd = buffer[:-4]
        else:
            retcmd = 'ERROR'

        return retcmd

    def loadcmds(self):
        """
        TODO: Load Commands from a file or defined dict
        """

        self.obdcmds = load_dict()

    def load_dict(self):
        """
        Creat Dict of Commands
        """



    self.ser.close()
