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

ser.close()
