# This is a python OBD Module Used to communicate with an OBDII device
# Over Serial

import serial
from os import name
from obdCmd import obdCmd
from time import sleep


# Init Port
#ser = serial.Serial(
#    port = '/dev/ttyUSB0',
#    baudrate = 9600
#    )

# OBD Commands for ELM327
reset_obd = 'ATZ'
check_voltage = 'ATRV'
init_obd = 'ATP01'
list_commands = '0100'
rpm = '010c'

class obd:
    # A Simple class for controlling ELM327 based OBD Scanners

    def __init__(self, port_name='/dev/ttyUSB0'):
        # Initilize the Port
        # TODO: Add Port Name Back
        self.data = []
        self.port_name = port_name
        self.baud_rate = 9600
        self.data_bits = 8
        self.stop_bits = 1
        self.line_ending = '\r'
        self.elmchar = '>'
        self.elmerror = '?'
        self.obdcmds = {}
        self.obdmodes = {}
        self.os_type = name

        ## Init Port and Modes
        self.init_port()
        self.obdmodes = self.init_modes()
        self.obdcmds = self.loadcmds()

        return None

    def init_port(self):
        try:
        # Attempt to Open Port
            #self.ser.setBaudrate = self.baud_rate
            #self.ser.port = self.port_name

            if self.os_type == 'win32':
                self.ser = serial.Win32Serial()
                self.ser.open()
            else:
                self.ser = serial.Serial(
                    port = self.port_name,
                    baudrate = self.baud_rate
                    )
            ### Sleep necessary to prevent race condition ###
            sleep(.3)
        except serial.SerialException() as e:
                print 'Error'
                print e

        return None

    def write_ELM(self, data):
        # Write to ELM and Check that Command was Correct
        cmd_len = self.ser.write(data + self.line_ending)
        sleep(.7)
        response = self.readline(cmd_len)

        if 'BADCMD' in response:
            return 'ERROR'
        else:
            return response

    def init_ELM327(self):
        # Init ELM327 Device
        self.write_ELM('ATZ')
        sleep(1)
        # Find Protocol
        self.write_ELM('ATP01')
        sleep(.7)

        return None

    def init_modes(self):
        # Initilize OBD Modes Dict
        modes = {}

        modes['0x01'] = "Show Current Data"
        modes['0x02'] = "Show freeze frame data"
        modes['0x03'] = "Show stored Diagnostic Trouble Codes"
        modes['0x04'] = "Clear Diagnostic Trouble Codes and stored values"
        modes['0x05'] = "Test results, oxygen sensor monitoring (non CAN only)"
        modes['0x06'] = "Test results, other component/system monitoring (Test results, oxygen sensor monitoring for CAN only"
        modes['0x07'] = "Show pending Diagnostic Trouble Codes (detected during current or last driving cycle)"
        modes['0x08'] = "Control operation of on-board component/system"
        modes['0x09'] = "Request vehicle information"
        modes['0x0A'] = "Permanent Diagnostic Trouble Codes (DTCs) (Cleared DTCs)"

        return modes

    def get_mode(self, value):
        return self.obdmodes.keys()[self.obdmodes.values().index(value)]

    def close_port(self):
        self.ser.close()

    def sendCmd(self, cmd):
        self.ser.write(cmd.mode + cmd.pid)
        return cmd.short_name

    def readobd(self):
        return None

    def toInt(self, string):
        return int(string, 16)

    def readline(self, len=0):
        # Read line from ELM327

        buff = ''
        retcmd = ''
        if self.ser.inWaiting() != 0:
            buff += self.ser.read(self.ser.inWaiting())
        if self.elmchar in buff:
            # Pulls Response
            if self.elmerror not in buff:
                retcmd = buff[len:-3]
            else:
                retcmd = 'BADCMD'
        else:
            retcmd = 'ERROR'

        return retcmd

    def loadcmds(self):
        # TODO: Load Commands from a file or defined dict


        self.obdcmds = self.temp_dict()

        return None

    def load_dict(self):
        #Creat Dict of Commands
        obd_cmds = {}

        obd_cmds = self.temp_dict()

        return None

    def temp_dict(self):
        cmds = {}

        # Setting Up Basic Commands
        #ShortName, PID, Long_Name, Bytes Returned, Description, minValue
        #maxValue, units, formula

        cmds['RPM'] = obdCmd('RPM','0x0C','0x01',"Engine RPM",
                            2,'',0,16383.75,'rpm', '((A*256)+B)/4')

        return cmds

    def temp_tach(self):
        cmd = '010C'
        tach_data = self.write_ELM(cmd)
        # Response 41 0C 0B 03
        data = tach_data.split(' ')
        rpm = data[-3:-1]
        rpm_out = ((self.toInt(rpm[0])*256) + self.toInt(rpm[1]))/4

        return rpm_out