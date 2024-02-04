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


while True:
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
