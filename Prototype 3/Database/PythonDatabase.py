#IP ADDRESSES
#Raspberry Pi- 192.168.4.31

#import libraries
import openpyxl
from openpyxl import Workbook, load_workbook
#load in workbook
book = load_workbook("MagicGrow.xlsx")
sheet = book.active



sheet["A1"].value = sheet["A1"].value + 1

print(sheet["A1"].value)

book.save("MagicGrow.xlsx")