# plan-
# IN TEMPERATURESHEET,
# COlUMN A1 is temperature
# COLUMN A2 is time
# SAME FOR EC, pH, and WATERPUMP UP & WATERPUMP DOWN
#
# STEPS-
# 1. IMPORT + SETUP EVERYTHING FOR READING VALUES, INLCUDING KASA, PHIDGET, AND ARDUINO
# 2. IN LOOP, SAVE EACH VALUE (LIKE TEMPERATURE) TO EACH RESPECTIVE SHEET (LIKE TEMPERATURE SHEET) AND TIME
# 3. AUTOSAVE FILE EVERY 10 MINUTES

from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import random
import datetime

#Create a workbook object
#wb = Workbook()

#load existing spreadsheet
wb = load_workbook(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\Database\excel\Database.xlsx")

#Create Worksheets
ws_Temperature = wb["Temperature"] #THE TEMPERATURE SHEET IS ALSO THE LIGHT SHEET BECAUSE TEMPERATURE MODIFIES LIGHT
ws_EC = wb["EC"]
ws_pH = wb["pH"]
ws_WaterPumpUp = wb["WaterPumpUp"]
ws_WaterPumpDown = wb["WaterPumpDown"]

#Columns

temp_column_a = ws_Temperature["a"]
temp_column_c = ws_Temperature["c"]

# Set a variable
# name = ws["A3"].value
# color = ws["B3"].value

# Print something from our worksheet
# print(f'{name} : {color}')

# Grab a whole column



# #For loop
# for cell1 in temp_column_a:
#     print(cell1.value)
# for cell2 in temp_column_c:
#     print(cell2.value)

# #Grab a range
# range = ws_Temperature["A1":"D30"]

# #Loop
# for cell in range: #with tuple
#     for x in cell: #removes tuple parenthesis
#         print(x.value)

# #Getting the number of cells in a column

# # Specify the column number (e.g., column A is 1, B is 2, etc.)
# temp_column_a_number = 1

# # Get the column letter corresponding to the column number
# column_letter = chr(64 + temp_column_a_number)

# # List to store non-empty cell values in the specified column
# temp_column_a_cells = ws_Temperature[column_letter]

# # Calculate number of non-empty cells in the column
# num_of_in_temp_column_a = sum(1 for cell in temp_column_a_cells if cell.value is not None)

# # Print the number of cells in the column
# print(f"Number of non-empty cells in column {column_letter}: {num_of_in_temp_column_a}")

#To set value of a cell

# c2 = sheet.cell(row= 1 , column = 2) 
# c2.value = "RAI"

def save_file(): #function for saving file
    wb.save(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\Database\excel\Database.xlsx")


#Function for reading number of values in a cell
def number_of_values_in_cell(column_number_S, worksheeT): # First specify column number (e.g., column A is 1, B is 2, etc.), then worksheet
        
    # Specify the column number (e.g., column A is 1, B is 2, etc.)
    column_number = column_number_S

    # Get the column letter corresponding to the column number
    column_letter = chr(64 + column_number)

    # List to store non-empty cell values in the specified column
    column_cells = worksheeT[column_letter]

    # Calculate number of non-empty cells in the column
    num_of_in_column = sum(1 for cell in column_cells if cell.value is not None)
    
    return num_of_in_column

# def append_new_cell(append_value, worksheet, columN):
#     cValue = worksheet.cell(row=int(number_of_values_in_cell(1, worksheet)) + 1, column = columN)
#     cValue.value = append_value
#     save_file()

def append_new_cell(append_value, ws, col_num):
    cValue = ws.cell(row=1, column=col_num)
    # Ensure append_value is a string
    append_value = str(append_value)
    cValue.value = append_value

def append_row_Temperature(New_Temperature, New_Light_On, New_Meeting_Requirements, New_Time):
    append_new_cell(New_Temperature, ws_Temperature, 1)
    append_new_cell(New_Light_On, ws_Temperature, 2)
    append_new_cell(New_Time, ws_Temperature, 3)
    append_new_cell(New_Meeting_Requirements, ws_Temperature, 4)
    save_file()

#Temperature Add New Cell
# New_Temperature = 29
# New_Light_On = "ON"
# New_Meeting_Requirements = "ON"
# New_Time = "02:00:00 PM"

while True:
    New_Temperature = random.randint(20, 40)
    New_Light_OnOff = random.choices(["ON", "OFF"])
    New_Meeting_Requirements = random.choices(["ON", "OFF"])
    New_Time = datetime.datetime.ctime
    
    append_row_Temperature(New_Temperature, New_Light_OnOff, New_Meeting_Requirements, New_Time)
    
    exit()