# This is a python OBD Module Used to communicate with an OBDII device
# Over Serial

import serial
import socket
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

# TODO: Make ReadCommand Read when data is availble make it blocking

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
        self.debug = True

        self.UDP_IP = "127.0.0.1"
        self.UDP_PORT = 5050
        self.UDP_tup = (self.UDP_IP, self.UDP_PORT)
        self.udp_socket = 0

        ## Init Port and Modes
        if port_name != 'debug':
            self.debug = False
            self.init_port()
            self.init_ELM327()
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
        self.write_ELM('ATSP0')
        sleep(7)
        self.write_ELM('0100')
        sleep(3)
        self.readline()

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

    def toInt(self, string_in):
        # Return numerical val from string val
        return int(string_in, 16)

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

    def rpm(self):
        if self.debug is False:
            rpm_out = self.temp_tach()
        else:
            rpm_out = 768
        return 'RPM:' + str(rpm_out)

    def start_server(self):
        self.udp_socket = socket.socket(socket.AF_INET, #Internet
                                        socket.SOCK_DGRAM) #UDP

    def udp_send (self, data='DEADBEEF'):
        self.udp_socket.sendto(data, self.UDP_tup)

    def run_tach_server(self):
        # Contiuously Send RPM over UDP
        self.start_server()
        while True:
            data = self.rpm()
            self.udp_send(data)