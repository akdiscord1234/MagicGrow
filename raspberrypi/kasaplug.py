# 192.168.4.87 is plug 1
# 192.168.4.89 is plug 2
import asyncio

import kasa
from kasa import *

ip = ""

async def main():
    WaterPumpUp = SmartPlug("192.168.4.87")
    #plug = SmartPlug()
    #kasa.Discover(plug)

    await WaterPumpUp.update()
    

asyncio.get_event_loop().run_until_complete(main())