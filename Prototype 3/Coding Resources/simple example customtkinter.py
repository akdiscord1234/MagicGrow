#Import libraries

import matplotlib
import customtkinter

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

from time import sleep

#Init setup
#apperance
customtkinter.set_appearance_mode("System") # can also use "System", "Dark", and "Light"
customtkinter.set_default_color_theme("green") # Themes, blue, green, dark-blue, ect
#root
app = customtkinter.CTk()
app.geometry("1200x500")
app.title("MagicGrow")

#tabview.grid()
#Grid Configure Layout
# app.columnconfigure((0, 1, 2, 3, 4), weight=3)
# app.rowconfigure((0, 1), weight=3)

# Content
MagicGrowLabel = customtkinter.CTkLabel(master=app, text="MagicGrow Home", text_color="green", font=("Calibri", 44))



#Temperature schedule
global TemperatureState
TemperatureState = 20

TemperatureLabel = customtkinter.CTkLabel(master=app, text="Temperature: " + str(TemperatureState) + "°C", text_color="red", font=("Calibri", 44))

#EC schedule
global ECState
ECState = 3
ECLabel = customtkinter.CTkLabel(master=app, text="EC: " + str(ECState) + "mS/cm", text_color="orange", font=("Calibri", 44))

#Light On/Off schedule
global LightState
LightState = "ON"
LightLabel = customtkinter.CTkLabel(master=app, text="Light is "+LightState, text_color="yellow", font=("Calibri", 44))

#Water Pump schedule
global WaterPumpUpState
global WaterPumpDownState
global WaterPumpTotalState

WaterPumpTotalState = "Water Pump Up is ON, Water Pump Down is OFF"

WaterPumpLabel = customtkinter.CTkLabel(master=app, text=WaterPumpTotalState, text_color="blue", font=("Calibri", 44))

#Update Button

def UpdateButtonpress():
    ECLabel.configure(text="changed")
UpdateButton = customtkinter.CTkButton(master=app, text = "update", command = UpdateButtonpress)

#Placing Widgets Layout

#Pack
MagicGrowLabel.pack(side="top", anchor="nw")
UpdateButton.pack(side="top", anchor="ne")
TemperatureLabel.pack(side="top")
ECLabel.pack(side="top")
LightLabel.pack(side="top")
WaterPumpLabel.pack(side="top")
#Grid
# MagicGrowLabel.grid(row=0, column=0, sticky="nw")
# UpdateButton.grid(row=0, column=1, sticky="ne")
# #Temperature
# TemperatureLabel.grid(row=1, column=0)

# #EC
# ECLabel.grid(row=2, column=0)

# #Light
# LightLabel.grid(row=3, column=0)

# #Water Pump
# WaterPumpLabel.grid(row=4, column=0)

#Graphs

data = {
    'A' : 1209,
    'B' : 1240,
    'C' : 1243,
    'D' : 3421
}

datakeys = data.keys()
datavalue = data.values()

figure = Figure(figsize=(6, 4), dpi=50)

figure_canvas = FigureCanvasTkAgg(figure)

NavigationToolbar2Tk(figure_canvas)

axes = figure.add_subplot()

axes.bar(datakeys, datavalue)
axes.set_title("I have no idea what this graph is about")
axes.set_ylabel("idk")

figure_canvas.get_tk_widget().grid(row=1, column=1)
    
app.mainloop()