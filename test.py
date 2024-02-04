import asyncio
from kasa import *

#ips-
#192.168.4.87 Water Pump Down
#192.168.4.89 Base B
#192.168.4.94
#192.168.4.98
#192.168.4.99
#192.168.4.100
#192.168.4.101
#192.168.4.103

async def main(thingtodo):
    WaterPumpDown = SmartPlug("192.168.4.103")

    await WaterPumpDown.update()

    if thingtodo == "on":
        await WaterPumpDown.turn_on()
    if thingtodo == "off":
        await WaterPumpDown.turn_off()

while True:
    vartodo = input("type this for output")

    asyncio.get_event_loop().run_until_complete(main(vartodo))


