# from openpyxl.workbook import Workbook
# from openpyxl import load_workbook
import random
import time
import re
import Kasa
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.PHSensor import *
import time
from time import sleep
from datetime import *
# import pandas as pd

# EC Sensor Setup

from pyfirmata import Arduino, util #used to be from pyfirmata2 import Arduino, util
import time

# Define constants
TdsSensorPin = 0
VREF = 5.0
SCOUNT = 30

# Initialize Arduino board
board = Arduino('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_85733323939351A04291-if00')  # Replace with the correct port for your Arduino

analogBuffer = [0] * SCOUNT
analogBufferTemp = [0] * SCOUNT
analogBufferIndex = 0
copyIndex = 0

averageVoltage = 0
tdsValue = 0
temperature = 19.5

it = util.Iterator(board)
it.start()

# Configure analog pin
tds_sensor = board.get_pin('a:' + str(TdsSensorPin) + ':i')
time.sleep(1)

def get_median_num(b_array, i_filter_len):
    b_tab = b_array.copy()
    for i in range(i_filter_len - 1):
        for j in range(i_filter_len - i - 1):
            if b_tab[j] > b_tab[j + 1]:
                b_temp = b_tab[j]
                b_tab[j] = b_tab[j + 1]
                b_tab[j + 1] = b_temp

    if i_filter_len & 1:
        b_temp = b_tab[(i_filter_len - 1) // 2]
    else:
        b_temp = (b_tab[i_filter_len // 2] + b_tab[i_filter_len // 2 - 1]) // 2

    return b_temp


#temperature sensing
temp = TemperatureSensor()
temp.setDeviceSerialNumber(702002)
temp.setHubPort(0)
temp.openWaitForAttachment(5000)

#pH sensing
pH = PHSensor()
pH.setDeviceSerialNumber(702002)
pH.setHubPort(1)
pH.openWaitForAttachment(5000)

#Discovering Plugs
WaterPumpDown = Kasa.SmartPlug("192.168.4.99")
WaterPumpDown.update()

WaterPumpUp = Kasa.SmartPlug("192.168.4.100")
WaterPumpUp.update()

ECPumpUp = Kasa.SmartPlug("192.168.4.101")
ECPumpUp.update()

pHPumpDown = Kasa.SmartPlug("192.168.4.87")
pHPumpDown.update()

pHPumpUp = Kasa.SmartPlug("192.168.4.98")
pHPumpUp.update()

LightPlug = Kasa.SmartPlug("192.168.4.89")
LightPlug.update()

import time

#temperature sensing
temperature = 29

#pH sensing
pH = 6
#EXCEL FUNCTIONS HERE

#Code for getting current EC value
def get_current_EC():
    # Read analog value
    analog_value = tds_sensor.read()

    # Store analog value into the buffer
    if analog_value is not None:
        analogBuffer[analogBufferIndex] = analog_value * 1024
    else:
        analogBuffer[analogBufferIndex] = 0
    analogBufferIndex += 1

    if analogBufferIndex == SCOUNT:
        analogBufferIndex = 0

    # Read analog value every 40 milliseconds
    time.sleep(0.04)

    # Calculate median value using the median filtering algorithm
    for copyIndex in range(SCOUNT):
        analogBufferTemp[copyIndex] = analogBuffer[copyIndex]

    median_value = get_median_num(analogBufferTemp, SCOUNT)

    # Convert to voltage value
    averageVoltage = median_value * VREF / 1024.0

    # Your additional logic for TDS and temperature calculation can be added here
    finalEC = ((133.42 * (averageVoltage ** 3)) - 255.86 * (averageVoltage ** 2) + 857.39 * averageVoltage) * 0.5
    return finalEC
        

while True:
    #EXCEL CODE HERE
    
    #functions for controling the plugs

    def WaterPumpControls(control_name):
        #Water Pump Down controls
        if control_name == "down_on":
            WaterPumpDown.turn_on()
        elif control_name == "down_off":
            WaterPumpDown.turn_off()
        elif control_name == "down_toggle":
            WaterPumpDown.toggle()
        #Water Pump Up controls
        if control_name == "up_on":
            WaterPumpUp.turn_on()
        elif control_name == "up_off":
            WaterPumpUp.turn_off()
        elif control_name == "up_toggle":
            WaterPumpUp.toggle()

    def pHPumpControls(control_name):
        #pH Pump Down controls
        if control_name == "on":
            pHPumpDown.turn_on()
        elif control_name == "off":
            pHPumpDown.turn_off()
        elif control_name == "toggle":
            pHPumpDown.toggle()

        #pH Pump Up controls
        if control_name == "on":
            pHPumpUp.turn_on()
        elif control_name == "off":
            pHPumpUp.turn_off()
        elif control_name == "toggle":
            pHPumpUp.toggle()

    def ECPumpControls(control_name):
        #EC Pump Up controls
        
        if control_name == "on":
            ECPumpUp.turn_on()
        elif control_name == "off":
            ECPumpUp.turn_off()
        elif control_name == "toggle":
            ECPumpUp.toggle()
        
        

    def LightPlugControls(control_name):
        if control_name == "on":
            print("Light on")
        elif control_name == "off":
            print("Light off")
        elif control_name == "toggle":
            LightPlug.toggle()

    def get_current_value(value_name):
        if value_name == "temperature":
            return temp.getTemperature()
        if value_name == "pH":
            return pH.getPH()
        if value_name == "EC":
            #Code for getting current EC value
            # Read analog value
            analog_value = tds_sensor.read()

            # Store analog value into the buffer
            if analog_value is not None:
                analogBuffer[analogBufferIndex] = analog_value * 1024
            else:
                analogBuffer[analogBufferIndex] = 0
            analogBufferIndex += 1

            if analogBufferIndex == SCOUNT:
                analogBufferIndex = 0

            # Read analog value every 40 milliseconds
            time.sleep(0.04)

            # Calculate median value using the median filtering algorithm
            for copyIndex in range(SCOUNT):
                analogBufferTemp[copyIndex] = analogBuffer[copyIndex]

            median_value = get_median_num(analogBufferTemp, SCOUNT)

            # Convert to voltage value
            averageVoltage = median_value * VREF / 1024.0

            # Your additional logic for TDS and temperature calculation can be added here
            finalEC = ((133.42 * (averageVoltage ** 3)) - 255.86 * (averageVoltage ** 2) + 857.39 * averageVoltage) * 0.5
            return finalEC
        
        if temp.get_Temperature() <= 28:
            LightPlug.turn_off()
        elif temp.get_Temperature() >28:
            LightPlug.turn_on()
        
        if get_current_EC < 0.5:
            ECPumpUp.turn_on()
        elif get_current_EC > 0.5:
            ECPumpUp.turn_off()
        
        if pH.getPH() < 0.5:
            pHPumpUp.turn_on()
            pHPumpDown.turn_off()
        elif pH.getPH() < 0.5:
            pHPumpUp.turn_off()
            pHPumpDown.turn_on()
        
        if water_level_above_threshold == True:
            WaterPumpUp.turn_on()
            WaterPumpDown.turn_off()