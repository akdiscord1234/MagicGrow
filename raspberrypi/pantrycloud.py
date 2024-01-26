import pantry_wrapper
from pantry_wrapper import *
import time

pantry_id = "759b6bd3-6956-480d-afa4-5569177af40b"

varsave = {
    "temp": [time.ctime(), 42],
    "pH " : [time.ctime(), 9],
    "kasa plug on " : [time.ctime(), 42]
}

try:

    data = get_contents(pantry_id, "mainbasket", return_type="body")
    print(data)

    append_basket(pantry_id, "mainbasket", varsave, return_type="body")

except:
    print("Error: call failed")