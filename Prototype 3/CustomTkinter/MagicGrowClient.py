import sys
PATH = sys.executable
print(PATH)

import customtkinter
from PIL import Image
import pathlib
from selenium import webdriver

from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk

#Setup accessing the api on server
browser = webdriver.Chrome()

#set initial pH, EC, temperature, ect that will be found real values later on

current_pH = 6
current_EC = 3
current_temperature = 30

#set appearance and theme
customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")

#root setup
app = customtkinter.CTk()
app.geometry('%dx%d+%d+%d' % (1000, 700, 0, 0)) #w, h, x, y

app.title("MagicGrow")

app.wm_iconphoto(True, r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Side_icon.bmp")

#tabview setup

tabview = customtkinter.CTkTabview(master=app)
tabview.pack(side="top", fill = "both")

HomePageTab = tabview.add("Homepage 🏠") # add tab
GraphTab = tabview.add("Graphs/Charts 📈")  # add tab at the end
tabview.set("Homepage 🏠")  # set currently visible tab


#Homepage

#Frame Width and Height
HomepageFrameWidth = 300
HomepageFrameHeight = 300

#Functions
#Water Pump OptionMenu
def optionmenu_callback_WaterPump(choice):
    if choice == "Pump Up On, Pump Down Off":
        browser.get("http://192.168.0.100:5000//water_pump_up_on")
        browser.get("http://192.168.0.100:5000/water_pump_down_off")
    elif choice == "Pump Up On, Pump Down On":
        browser.get("http://192.168.0.100:5000//water_pump_up_on")
        browser.get("http://192.168.0.100:5000//water_pump_down_on")
    elif choice == "Pump Up Off, Pump Down Off":
        browser.get("http://192.168.0.100:5000//water_pump_up_off")
        browser.get("http://192.168.0.100:5000//water_pump_down_off")
    elif choice == "Pump Up Off, Pump Down On":
        browser.get("http://192.168.0.100:5000//water_pump_up_off")
        browser.get("http://192.168.0.100:5000//water_pump_down_on")
    elif choice == "Automatic":
        pass

#Light Switch
def switch_event_Light():
    print("switch toggled, current value:", switch_var_Light.get())
    if switch_event_Light.get == "off":
        browser.get("http://192.168.0.100:5000/light_off")
    elif switch_event_Light.get == "on":
        browser.get("http://192.168.0.100:5000/light_on")

switch_var_Light = customtkinter.StringVar(value="on")

#Temperature Enter Button
def Temperature_Enter_Button():
    #Code here for Scheduling the Change of Temperature
    pass

#pH Enter Button
def pH_Enter_Button():
    #Code here for Scheduling the Change of pH
    pass

#EC Enter Button
def EC_Enter_Button():
    #Code here for Scheduling the Change of EC
    pass

#GridConfigure for Homepage
HomePageTab.columnconfigure(0, weight=2)
HomePageTab.columnconfigure(1, weight=2)
HomePageTab.columnconfigure(2, weight=2)
HomePageTab.rowconfigure(0, weight=2)
HomePageTab.rowconfigure(1, weight=2)
HomePageTab.rowconfigure(2, weight=2)

#Side Icon

Side_Icon_Image = customtkinter.CTkImage(dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Side_icon.png"), size=(200, 200))
Side_Icon_Image_Holder = customtkinter.CTkLabel(master=HomePageTab, image=Side_Icon_Image, text="")
Side_Icon_Image_Holder.grid(column=2, row=1, sticky="nw")

#Temperature Frame

TemperatureFrame = customtkinter.CTkFrame(master=HomePageTab, width=HomepageFrameWidth, height=HomepageFrameHeight)
TemperatureFrame.grid(column=0, row=0, ipady=20)

TemperatureLabel = customtkinter.CTkLabel(master=TemperatureFrame, text="Temperature", font=("arial", 22))
TemperatureLabel.pack(side="top")

TemperatureEntry = customtkinter.CTkEntry(master=TemperatureFrame, placeholder_text="Enter Temperature")
TemperatureEntry.pack(side="top", anchor="n")

TemperatureEntryTime = customtkinter.CTkEntry(master=TemperatureFrame, placeholder_text="Temp Schedule Time")
TemperatureEntryTime.pack(side="top", anchor="n")

TemperatureInfo = customtkinter.CTkLabel(master=TemperatureFrame, text=str(current_temperature) + "°C", font=("arial", 22))
TemperatureInfo.pack(side="top")

TemperatureImage = customtkinter.CTkImage(dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Temp_icon.jpg"), size=(83, 116))
TemperatureImageHolder = customtkinter.CTkLabel(master=TemperatureFrame, image=TemperatureImage, text="")
TemperatureImageHolder.pack(side="top")

TemperatureEnterButton = customtkinter.CTkButton(master=TemperatureFrame, text="Enter Changes", command=Temperature_Enter_Button)
TemperatureEnterButton.pack(side="top")

#pH Frame

pHFrame = customtkinter.CTkFrame(master=HomePageTab, width=HomepageFrameWidth, height=HomepageFrameHeight)
pHFrame.grid(column=0, row=1, ipady=20)

pHLabel = customtkinter.CTkLabel(master=pHFrame, text="pH", font=("arial", 22))
pHLabel.pack(side="top")

pHEntry = customtkinter.CTkEntry(master=pHFrame, placeholder_text="Enter pH")
pHEntry.pack(side="top", anchor="n")

pHEntryTime = customtkinter.CTkEntry(master=pHFrame, placeholder_text="pH Schedule Time")
pHEntryTime.pack(side="top", anchor="n")

pHInfo = customtkinter.CTkLabel(master=pHFrame, text=str(current_pH) + " pH", font=("arial", 22))
pHInfo.pack(side="top")

pHImage = customtkinter.CTkImage(dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\pH_icon.jpg"), size=(100, 100))
pHImageHolder = customtkinter.CTkLabel(master=pHFrame, image=pHImage, text="")
pHImageHolder.pack(side="top")

pHEnterButton = customtkinter.CTkButton(master=pHFrame, text="Enter Changes", command=pH_Enter_Button)
pHEnterButton.pack(side="top")

#EC Frame

ECFrame = customtkinter.CTkFrame(master=HomePageTab, width=HomepageFrameWidth, height=HomepageFrameHeight)
ECFrame.grid(column=1, row=0, ipady=20)

ECLabel = customtkinter.CTkLabel(master=ECFrame, text="EC", font=("arial", 22))
ECLabel.pack(side="top")

ECEntry = customtkinter.CTkEntry(master=ECFrame, placeholder_text="Enter EC")
ECEntry.pack(side="top", anchor="n")

ECEntryTime = customtkinter.CTkEntry(master=ECFrame, placeholder_text="EC Schedule Time")
ECEntryTime.pack(side="top", anchor="n")

ECInfo = customtkinter.CTkLabel(master=ECFrame, text=str(current_EC) + " EC", font=("arial", 22))
ECInfo.pack(side="top")

ECImage = customtkinter.CTkImage(dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Ec_icon.jpg"), size=(100, 100))
ECImageHolder = customtkinter.CTkLabel(master=ECFrame, image=ECImage, text="")
ECImageHolder.pack(side="top")

ECEnterButton = customtkinter.CTkButton(master=ECFrame, text="Enter Changes", command=EC_Enter_Button)
ECEnterButton.pack(side="top")

#Light Frame

LightFrame = customtkinter.CTkFrame(master=HomePageTab, width=HomepageFrameWidth, height=HomepageFrameHeight)
LightFrame.grid(column=1, row=1, ipady=20)

LightLabel = customtkinter.CTkLabel(master=LightFrame, text="Light", font=("arial", 22))
LightLabel.pack(side="top")

switch_Light = customtkinter.CTkSwitch(master=LightFrame, text="Light ON/OFF", command=switch_event_Light,
                                 variable=switch_var_Light, onvalue="on", offvalue="off")
switch_Light.pack(side="top")

LightStartTime = customtkinter.CTkEntry(master=LightFrame, placeholder_text="Light Sched Start Time")
LightStartTime.pack(side="top")

LightEndTime = customtkinter.CTkEntry(master=LightFrame, placeholder_text="Light Sched End Time")
LightEndTime.pack(side="top")

LightImage = customtkinter.CTkImage(dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Light_icon.png"), size=(100, 100))
LightImageHolder = customtkinter.CTkLabel(master=LightFrame, image=LightImage, text="")
LightImageHolder.pack(side="top")

#Water Pump Frame

WaterPumpFrame = customtkinter.CTkFrame(master=HomePageTab, width=HomepageFrameWidth, height=HomepageFrameHeight)
WaterPumpFrame.grid(column=2, row=0, ipady=20)

WaterPumpLabel = customtkinter.CTkLabel(master=WaterPumpFrame, text="Water Pump", font=("arial", 22))
WaterPumpLabel.pack(side="top")

optionmenu_WaterPump = customtkinter.CTkOptionMenu(master=WaterPumpFrame, values=["Pump Up On, Pump Down Off", "Pump Up On, Pump Down On", "Pump Up Off, Pump Down Off", "Pump Up Off, Pump Down On", "Automatic"],
                                         command=optionmenu_callback_WaterPump)
optionmenu_WaterPump.set("Automatic")

optionmenu_WaterPump.pack(side="top")

WaterPumpImage = customtkinter.CTkImage(dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\WaterPump_Icon.jpeg"), size=(100, 100))
WaterPumpImageHolder = customtkinter.CTkLabel(master=WaterPumpFrame, image=WaterPumpImage, text="")
WaterPumpImageHolder.pack(side="top")


#Graphs/Charts

graphview = customtkinter.CTkTabview(master=tabview.tab("Graphs/Charts 📈"))
graphview.pack(padx=10, pady=10, ipadx=1200, ipady=100)

graphview.add("Temperature Graph 🌡️") # add tab
graphview.add("pH Graph")  # add tab at the end
graphview.add("Up Pump Graph")  # add tab at the end
graphview.add("Down Pump Graph")  # add tab at the end
graphview.add("pH Up Nutrient Pump Graph")  # add tab at the end
graphview.add("pH Down Nutrient Pump Graph")  # add tab at the end
graphview.add("Base A and B Nutrient Pump Graph")  # add tab at the end

graphview.set("Temperature Graph 🌡️")  # set currently visible tab

#Code for accessing graphs here


#mainloop

app.mainloop()
