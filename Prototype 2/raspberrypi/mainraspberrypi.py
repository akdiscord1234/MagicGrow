import time
import asyncio
from kasa import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.PHSensor import *
from time import sleep
from pantry_wrapper import *
from datetime import *
import pandas as pd

# EC Sensor Setup

from pyfirmata2 import Arduino, util
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

pantry_id = "759b6bd3-6956-480d-afa4-5569177af40b"

#main get_contents
temperaturePantry = get_contents(pantry_id, "temperature", return_type="body")
pHPantry = get_contents(pantry_id, "pH", return_type="body")
ECPantry = get_contents(pantry_id, "EC", return_type="body")

execution = "none"

async def main(execution):

    #Discovering Plugs
    WaterPumpDown = SmartPlug("192.168.4.99")
    await WaterPumpDown.update()

    WaterPumpUp = SmartPlug("192.168.4.100")
    await WaterPumpUp.update()

    ECPumpUp = SmartPlug("192.168.4.101")
    await ECPumpUp.update()

    pHPumpDown = SmartPlug("192.168.4.87")
    await pHPumpDown.update()

    pHPumpUp = SmartPlug("192.168.4.98")
    await pHPumpUp.update()

    LightPlug = SmartPlug("192.168.4.89")
    await LightPlug.update()

    #functions

    if execution == "none":
        pass

    #Water Pump Up
    if execution == "WaterPumpUpOn":
        await WaterPumpUp.turn_on()

    if execution == "WaterPumpUpOff":
        await WaterPumpUp.turn_off()


    #Water Pump Down
    if execution == "WaterPumpDownOn":
        await WaterPumpDown.turn_on()

    if execution == "WaterPumpDownOff":
        await WaterPumpDown.turn_off()

    #EC Pump Up
    if execution == "ECPumpUpOn":
        await ECPumpUp.turn_on()

    if execution == "ECPumpUpOff":
        await ECPumpUp.turn_off()

    #pH Pump Up
    if execution == "pHPumpUpOn":
        await pHPumpUp.turn_on()

    if execution == "pHPumpUpOff":
        await pHPumpUp.turn_off()

    #pH Pump Down
    if execution == "pHPumpDownOn":
        await pHPumpDown.turn_on()

    if execution == "pHPumpDownOff":
        await pHPumpDown.turn_off()

    #Light Plug
    if execution == "LightOn":
        await LightPlug.turn_on()

    if execution == "LightOff":
        await LightPlug.turn_off()


while True:
    sleep(5)

    asyncio.get_event_loop().run_until_complete(main(execution))

    # add nutrients get_contents
    WaterUpPumpChanges = get_contents(pantry_id, "WaterUpPumpChanges", return_type="body")
    WaterDownPumpChanges = get_contents(pantry_id, "WaterDownPumpChanges.json", return_type="body")
    pHUpChanges = get_contents(pantry_id, "pHUpChanges", return_type="body")
    pHDownChanges = get_contents(pantry_id, "pHDownChanges", return_type="body")
    ECChanges = get_contents(pantry_id, "ECChanges", return_type="body")
    LightChanges = get_contents(pantry_id, "LightChanges", return_type="body")
    TemperatureChanges = get_contents(pantry_id, "TemperatureChanges", return_type="body")


    #list of Changes
    WaterDownPumpChangesList = [value for value in WaterDownPumpChanges.values() if not isinstance(value, (int, float))]
    print(WaterDownPumpChangesList)

    WaterUpPumpChangesList = [value for value in WaterUpPumpChanges.values() if not isinstance(value, (int, float))]
    print(WaterUpPumpChangesList)

    pHUpChangesList = [value for value in pHUpChanges.values() if not isinstance(value, (int, float))]
    print(pHUpChangesList)

    pHDownChangesList = [value for value in pHDownChanges.values() if not isinstance(value, (int, float))]
    print(pHDownChangesList)

    ECChangesList = [value for value in ECChangesList.values() if not isinstance(value, (int, float))]
    print(ECChangesList)

    LightChangesList = [value for value in LightChangesList.values() if not isinstance(value, (int, float))]
    print(LightChangesList)

    TemperatureChangesList = [value for value in TemperatureChangesList.values() if not isinstance(value, (int, float))]
    print(TemperatureChangesList)

    #Pump Changes

    #Water Down Pump Changes
    if WaterDownPumpChangesList[-1] == "True":
        execution = "WaterPumpDownOn"
    elif WaterDownPumpChangesList[-1] == "False":
        execution = "WaterPumpDownOff"

    # Water Up Pump Changes
    if WaterUpPumpChangesList[-1] == "True":
        execution = "WaterPumpUpOn"
    if WaterUpPumpChangesList[-1] == "False":
        execution = "WaterPumpUpOff"

    # pH Up Pump Changes
    if pHUpChangesList[-1] == "True":
        execution = "pHPumpUpOn"
    if pHUpChangesList[-1] == "False":
        execution = "pHPumpUpOff"

    # pH Down Pump Changes
    if pHDownChangesList[-1] == "True":
        execution = "pHPumpDownOn"
    if pHDownChangesList[-1] == "False":
        execution = "pHPumpDownOff"

    # EC Pump Changes
    if ECChangesList[-1] == "True":
        execution = "ECPumpUpOn"
    if ECChangesList[-1] == "False":
        execution = "ECPumpUpOff"

    #Other Changes

    # Light Changes
    if LightChangesList[-1] == "True":
        execution = "LightOn"

    if LightChangesList[-1] == "False":
        execution = "LightOff"

    #EC code

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


    #main append
    temperaturePantry[str(datetime.now())] = temp.getTemperature()
    pHPantry[str(datetime.now())] = pH.getPH()
    ECPantry[str(datetime.now())] = finalEC

    append_basket(pantry_id, "temperature", temperaturePantry, return_type="body") #temperature
    append_basket(pantry_id, "pH", pHPantry, return_type="body")  # pH
    append_basket(pantry_id, "EC", ECPantry, return_type="body")  # EC