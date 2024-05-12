from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.PHSensor import *


#temperature sensing
temp = TemperatureSensor()
temp.setDeviceSerialNumber(702002)
temp.setHubPort(0)
temp.openWaitForAttachment(5000)
print("Temperature: " + str(temp.getTemperature()) + "°C")


#pH sensing
pH = PHSensor()
pH.setDeviceSerialNumber(702002)
pH.setHubPort(1)
pH.openWaitForAttachment(5000)
print("pH: " + str(pH.getPH()))


temp.close()