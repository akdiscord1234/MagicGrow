import time

from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.PHSensor import *
from time import sleep
from pantry_wrapper import *
from datetime import *
import pandas as pd

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
tempPantry = get_contents(pantry_id, "temperature", return_type="body")
pHPantry = get_contents(pantry_id, "pH", return_type="body")

while True:
    sleep(5)

    tempPantry[str(datetime.now())] = temp.getTemperature()
    pHPantry[str(datetime.now())] = pH.getPH()

    #varsave["kasa plug on " + str(time.ctime())] = True

    append_basket(pantry_id, "temperature", tempPantry, return_type="body") #temperature
    append_basket(pantry_id, "pH", pHPantry, return_type="body")  # pH