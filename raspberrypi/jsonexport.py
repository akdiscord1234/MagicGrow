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

    # time splitter



    # time splitter (other)


    #now = datetime.now()
    #minutes = float(now.minute)
    #seconds = float(now.second)

    #d0 = date(1, 1, 1)
    #d1 = (minutes / 1440) + (seconds / 86400)
    # Convert the float value to a timedelta object
    #d1 = pd.to_timedelta(d1, unit='d')
    # Use time.min instead of datetime.min
    #dtoday = datetime.combine(now.today(), time.min) + d1
    # Get the difference between the two dates as a timedelta object
    #diffdays0 = dtoday - datetime.combine(d0, time.min)
    # Get the total number of seconds as a float value
    #diffdays1 = diffdays0.total_seconds()
    # Divide by 86400 to get the number of days as a float value
    #diffdays2 = diffdays1 / 86400
    # Format the float value with two decimal places using the format function
    #diffdays3 = "{:.10f}".format(diffdays2)

    tempPantry[str(datetime.now())] = temp.getTemperature()
    pHPantry[str(datetime.now())] = pH.getPH()

    #varsave["kasa plug on " + str(time.ctime())] = True

    append_basket(pantry_id, "temperature", tempPantry, return_type="body") #temperature
    append_basket(pantry_id, "pH", pHPantry, return_type="body")  # pH