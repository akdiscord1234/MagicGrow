import csv
from pantry_wrapper import *
import matplotlib.pyplot as plt
import math

pantry_id = "759b6bd3-6956-480d-afa4-5569177af40b"

tempPantry = get_contents(pantry_id, "temperature", return_type="body")

keys = []
values = []

for key in tempPantry.keys():
    keys.append(key)
print(keys)


#roundkeys = [math.ceil(keys) for keys in keys]

for value in tempPantry.values():
    values.append(value)
print(values)


with open("temperature.csv", "w") as f:
    # Create a DictWriter object with the dictionary keys as field names
    writer = csv.DictWriter(f, fieldnames=tempPantry.keys())
    # Write the header row
    writer.writeheader()
    # Write the dictionary as a single row
    writer.writerow(tempPantry)

# initializing the data
x = keys
y = values
# plotting the data
plt.plot(x, y)
# Adding the title
plt.title("Temperature over time")
# Adding the labels
plt.ylabel("Temperature in Celsius")
plt.xlabel("Time in days")
plt.show()



