import csv
from pantry_wrapper import *
import matplotlib.pyplot as plt

pantry_id = "759b6bd3-6956-480d-afa4-5569177af40b"

pHPantry = get_contents(pantry_id, "pH", return_type="body")

# Create a dictionary

# Open a CSV file for writing
with open("../pH.csv", "w") as f:
    # Create a DictWriter object with the dictionary keys as field names
    writer = csv.DictWriter(f, fieldnames=pHPantry.keys())
    # Write the header row
    writer.writeheader()
    # Write the dictionary as a single row
    writer.writerow(pHPantry)

keys = []
values = []

for key in pHPantry.keys():
    keys.append(key)
print(keys)


for value in pHPantry.values():
    values.append(value)
print(values)


# initializing the data
x = keys
y = values
# plotting the data
plt.plot(x, y)
# Adding the title
plt.title("pH levels over time")
# Adding the labels
plt.ylabel("pH")
plt.xlabel("Time in days")
plt.show()