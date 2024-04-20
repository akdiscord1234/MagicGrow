#much of the code is commented out because this alternative code has limiited functionality and is not the same as the original code.
#The code is commetned out to make sure that this alternative code will work properly if the main code does not work
import customtkinter
from PIL import Image
from pantry_wrapper import *
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import datetime
import asyncio

error_message_getpantry = "Getpantry.cloud limited requests, please try the MagicGrow app later. Thanks!"

print("takes about 10-15 seconds to load, please wait")

#Pantry setup
pantry_id = "33f98734-b9a2-49c2-8206-8dcef96707dd"

#temperature info

tempPantry = get_contents(pantry_id, "temperature", return_type="body")

tempkeys = []
tempvalues = []

for tempkey in tempPantry.keys():
    tempkeys.append(tempkey)

for tempvalue in tempPantry.values():
    tempvalues.append(tempvalue)
print("temperature done")
current_temperature = tempvalues[-1]

current_pH = 5.8
current_EC = 3.4

#pH Up Changes
pHUpChanges = get_contents(pantry_id, "pHUpChanges", return_type="body")
print("pH Up Pump Changes done")

#pH Down Changes
pHDownChanges = get_contents(pantry_id, "pHDownChanges", return_type="body")
print("pH Down Pump Changes done")

#Water Pump Up Changes
WaterPumpUpChanges = get_contents(pantry_id, "WaterUpPumpChanges", return_type="body")
print("Water Pump Up Changes done")


#Water Pump Down Changes
WaterPumpDownChanges = get_contents(pantry_id, "WaterDownPumpChanges.json", return_type="body")
print("Water Down Up Changes done")
#Water Pump Up
current_WaterPumpUpOn = True
if current_WaterPumpUpOn == True:
    current_WaterPumpUp_str = "On"
else:
    current_WaterPumpUp_str = "Off"

#Water Pump Down
current_WaterPumpDownOn = True
if current_WaterPumpDownOn == True:
    current_WaterPumpDown_str = "On"
else:
    current_WaterPumpDown_str = "Off"

#pH info
pHPantry = get_contents(pantry_id, "pH", return_type="body")
try:
    fjoewjfoiewijo = pHPantry.values()
    valuespH = list(fjoewjfoiewijo)
    current_pH = valuespH[-1]
    print("pH worked")
except:
    print(error_message_getpantry)

print("pH done, window initializing")
#customtkinter window

#set appearance and theme
customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")  # default

#initial setup
root = customtkinter.CTk()
#root.geometry("700x700") uses maximized window
root.title("MagicGrow 2.0")

#tabview setup
tabview = customtkinter.CTkTabview(master=root)
tabview.place(relx=0, rely=0.5, anchor='w', relheight =1, relwidth = 1)

tabview.add("Homepage 🏠") # add tab
tabview.add("Graphs/Charts 📈")  # add tab at the end
tabview.set("Homepage 🏠")  # set currently visible tab

#Homepage




#temperature frame in Homepage
temperatureFrame = customtkinter.CTkScrollableFrame(master=tabview.tab("Homepage 🏠"), width=200, height=200)
temperatureFrame.place(relx=0, rely=0.6, anchor='w')

temperatureEntry = customtkinter.CTkEntry(master=temperatureFrame, placeholder_text=str(str(current_temperature) + "°C currently, set to"))
temperatureEntry.pack(padx=20, pady=20)

temperatureView = customtkinter.CTkLabel(master=temperatureFrame, text= str(current_temperature) + " °C", font=("arial", 22))
temperatureView.pack(padx=20, pady=20)

temperatureImage = customtkinter.CTkImage(light_image=Image.open("Temp_icon.jpg"),
                                          dark_image=Image.open("Temp_icon.jpg"),
                                          size=(50, 70))

temperatureImageLabel = customtkinter.CTkLabel(master=temperatureFrame, image=temperatureImage, text="")  # display image with a CTkLabel
temperatureImageLabel.pack(padx=0, pady= 0)

#pH frame in Homepage
pHFrame = customtkinter.CTkScrollableFrame(master=tabview.tab("Homepage 🏠"), width=200, height=200)
pHFrame.place(relx=0.2, rely=0.2, anchor='w')

pHEntry = customtkinter.CTkEntry(master=pHFrame, placeholder_text=str(str(current_pH) + " pH currently, set to"))
pHEntry.grid(padx=20, pady=20)

pHView = customtkinter.CTkLabel(master=pHFrame, text= str(current_pH) + " pH", font=("arial", 22))
pHView.grid(padx=20, pady=20)

pHImage = customtkinter.CTkImage(light_image=Image.open("pH_icon.jpg"),
                                 dark_image=Image.open("pH_icon.jpg"),
                                 size=(70, 70))

pHImageLabel = customtkinter.CTkLabel(master=pHFrame, image=pHImage, text="")  # display image with a CTkLabel
pHImageLabel.grid(row=3, column=0)

#light frame in Homepage
lightFrame = customtkinter.CTkScrollableFrame(master=tabview.tab("Homepage 🏠"), width=200, height=200)
lightFrame.place(relx=0.2, rely=0.6, anchor='w')

global choice
choice = "light on"
def light_option_menu(choice):
    print("optionmenu dropdown clicked:", choice)


optionmenu = customtkinter.CTkOptionMenu(master=lightFrame, values=["light on", "light off"],
                                         command=light_option_menu)
optionmenu.set(choice)

#lightEntry = customtkinter.CTkEntry(master=lightFrame, placeholder_text=str(str(current_light_state)))
optionmenu.grid(padx=20, pady=20)

lightView = customtkinter.CTkLabel(master=lightFrame, text= str(choice), font=("arial", 22))
lightView.grid(padx=20, pady=20)

lightImage = customtkinter.CTkImage(light_image=Image.open("Light_icon.png"),
                                    dark_image=Image.open("Light_icon.png"),
                                    size=(70, 70))

lightImageLabel = customtkinter.CTkLabel(master=lightFrame, image=lightImage, text="")  # display image with a CTkLabel
lightImageLabel.grid(row=3, column=0)

#EC frame in Homepage
ECFrame = customtkinter.CTkScrollableFrame(master=tabview.tab("Homepage 🏠"), width=200, height=200)
ECFrame.place(relx=0, rely=0.2, anchor='w')

ECEntry = customtkinter.CTkEntry(master=ECFrame, placeholder_text=str(str(current_EC) + " EC currently, set to (only higher)"))
ECEntry.grid(padx=20, pady=20)

ECView = customtkinter.CTkLabel(master=ECFrame, text= str(current_EC) + " EC", font=("arial", 22))
ECView.grid(padx=20, pady=20)


ECImage = customtkinter.CTkImage(light_image=Image.open("Ec_icon.jpg"),
                                 dark_image=Image.open("Ec_icon.jpg"),
                                 size=(70, 70))

ECImageLabel = customtkinter.CTkLabel(master=ECFrame, image=ECImage, text="")  # display image with a CTkLabel
ECImageLabel.grid(row=3, column=0)

#Water Pump Up frame in Homepage
WaterPumpUpFrame = customtkinter.CTkScrollableFrame(master=tabview.tab("Homepage 🏠"), width=200, height=200)
WaterPumpUpFrame.place(relx=0.6, rely=0.2, anchor='w')

#WaterPumpUpEntry = customtkinter.CTkEntry(master=WaterPumpUpFrame, placeholder_text=str("Water Pump is " + str(current_WaterPumpUp_str)))
#WaterPumpUpEntry.grid(padx=20, pady=20)

global WaterPumpUpChoice
WaterPumpUpChoice = "pump" + current_WaterPumpUp_str
def WaterPumpUp_option_menu(WaterPumpUpChoice):
    print("optionmenu dropdown clicked:", WaterPumpUpChoice)


WaterPumpUp_optionmenu = customtkinter.CTkOptionMenu(master=WaterPumpUpFrame, values=["pump On", "pump Off"],
                                         command=WaterPumpUp_option_menu)
WaterPumpUp_optionmenu.set(WaterPumpUpChoice)

WaterPumpUp_optionmenu.grid(padx=20, pady=20)

WaterPumpUpView = customtkinter.CTkLabel(master=WaterPumpUpFrame, text= "Water Pump Up", font=("arial", 22))
WaterPumpUpView.grid(padx=20, pady=20)


WaterPumpUpImage = customtkinter.CTkImage(light_image=Image.open("PumpON_icon.jpg"),
                                          dark_image=Image.open("PumpON_icon.jpg"),
                                          size=(70, 70))

WaterPumpUpImageLabel = customtkinter.CTkLabel(master=WaterPumpUpFrame, image=WaterPumpUpImage, text="")  # display image with a CTkLabel
WaterPumpUpImageLabel.grid(row=3, column=0)

#Water Pump Down frame in Homepage
WaterPumpDownFrame = customtkinter.CTkScrollableFrame(master=tabview.tab("Homepage 🏠"), width=200, height=200)
WaterPumpDownFrame.place(relx=0.6, rely=0.6, anchor='w')

#WaterPumpDownEntry = customtkinter.CTkEntry(master=WaterPumpDownFrame, placeholder_text=str("Water Pump is " + str(current_WaterPumpDown_str)))
#WaterPumpDownEntry.grid(padx=20, pady=20)

global WaterPumpDownChoice
WaterPumpDownChoice = "pump" + current_WaterPumpDown_str
def WaterPumpDown_option_menu(WaterPumpDownChoice):
    print("optionmenu dropdown clicked:", WaterPumpDownChoice)


WaterPumpDown_optionmenu = customtkinter.CTkOptionMenu(master=WaterPumpDownFrame, values=["pump On", "pump Off"],
                                         command=WaterPumpDown_option_menu)
WaterPumpDown_optionmenu.set(WaterPumpDownChoice)

WaterPumpDown_optionmenu.grid(padx=20, pady=20)

WaterPumpDownView = customtkinter.CTkLabel(master=WaterPumpDownFrame, text= "Water Pump Down", font=("arial", 22))
WaterPumpDownView.grid(padx=20, pady=20)


WaterPumpDownImage = customtkinter.CTkImage(light_image=Image.open("PumpOFF_icon.jpg"),
                                            dark_image=Image.open("PumpOFF_icon.jpg"),
                                            size=(70, 70))

WaterPumpDownImageLabel = customtkinter.CTkLabel(master=WaterPumpDownFrame, image=WaterPumpDownImage, text="")  # display image with a CTkLabel
WaterPumpDownImageLabel.grid(row=3, column=0)

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

# Water Pump Up graph
#fig = Figure(figsize=(5, 5), dpi=100)
#ax = fig.add_subplot(111)
#try:
#    ax.plot(WaterPumpUpChanges.keys(), WaterPumpUpChanges.values())
#except:
#    print(error_message_getpantry)


# Create the Tkinter canvas containing the figure
#canvas = FigureCanvasTkAgg(fig, master=graphview.tab("Up Pump Graph"))
#canvas.draw()
#canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Water Pump Down graph
#fig = Figure(figsize=(5, 5), dpi=100)
#ax = fig.add_subplot(111)
#try:
    #ax.plot(WaterPumpDownChanges.keys(), WaterPumpDownChanges.values())
#except:
print("Pantry cloud has limited storage, so it is not possible to show many graphs")
# Create the Tkinter canvas containing the figure
#canvas = FigureCanvasTkAgg(fig, master=graphview.tab("Down Pump Graph"))
#canvas.draw()
#canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# pH up pump graph
#fig = Figure(figsize=(5, 5), dpi=100)
#ax = fig.add_subplot(111)
#ax.plot(pHUpChanges.keys(), pHUpChanges.values())
#
# Create the Tkinter canvas containing the figure
#canvas = FigureCanvasTkAgg(fig, master=graphview.tab("pH Up Nutrient Pump Graph"))
#canvas.draw()
#canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# pH Down pump graph
#fig = Figure(figsize=(5, 5), dpi=100)
#ax = fig.add_subplot(111)
#ax.plot(pHDownChanges.keys(), pHDownChanges.values())

# Create the Tkinter canvas containing the figure
#canvas = FigureCanvasTkAgg(fig, master=graphview.tab("pH Down Nutrient Pump Graph"))
#canvas.draw()
#canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Temperature graph
fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(tempkeys, tempvalues)

# Create the Tkinter canvas containing the figure
canvas = FigureCanvasTkAgg(fig, master=graphview.tab("Temperature Graph 🌡️"))
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


#pH graph
fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(pHPantry.keys(), pHPantry.values())

# Create the Tkinter canvas containing the figure
canvas = FigureCanvasTkAgg(fig, master=graphview.tab("pH Graph"))
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


side_icon = customtkinter.CTkImage(light_image=Image.open("Side_icon.png"),
                                   dark_image=Image.open("Side_icon.png"),
                                   size=(210, 210))

side_icon_label = customtkinter.CTkLabel(tabview.tab("Homepage 🏠"), image=side_icon, text="")  # display image with a CTkLabel
side_icon_label.pack(side="bottom")
async def main():
    root.after(0, lambda: root.state('zoomed'))
    root.mainloop()
async def getvalues():
    #pH getvalue
    # temperature getvalue
    pHPantry = get_contents(pantry_id, "pH", return_type="body")
    current_temperature = pHPantry.values()[-1]

    # temperature getvalue
    tempPantry = get_contents(pantry_id, "temperature", return_type="body")
    current_temperature = tempPantry.values()[-1]

    # EC getvalue
    ECPantry = get_contents(pantry_id, "EC", return_type="body")
    current_EC = ECPantry.values()[-1]

#async def main2(): #this is for turning on and off the pumps and handling the user requests client wise

    #pH code
    #if pHEntry.get() > current_pH:
    #    pHDownChanges[str(datetime.now())] = "on"
    #    pHUpChanges[str(datetime.now())] = "on"
    #    append_basket(pantry_id, "pHUpChanges", pHUpChanges, return_type="body")
    #    append_basket(pantry_id, "pHDownChanges", pHDownChanges, return_type="body")

    #if pHEntry.get() < current_pH:
    #    pHDownChanges[str(datetime.now())] = "on"
    #    pHUpChanges[str(datetime.now())] = "off"
    #    append_basket(pantry_id, "pHUpChanges", pHUpChanges, return_type="body")
#3    append_basket(pantry_id, "pHDownChanges", pHDownChanges, return_type="body")

    # EC code
    #if ECEntry.get() > current_EC:
    #    ECChanges[str(datetime.now())] = "on"
    #    append_basket(pantry_id, "ECChanges", ECChanges, return_type="body")

    #if pHEntry.get() < current_pH:
    #    ECChanges[str(datetime.now())] = "off"
    #    append_basket(pantry_id, "ECChanges", ECChanges, return_type="body")


#root.after(0, lambda: root.state('zoomed'))
#root.mainloop()

asyncio.get_event_loop().run_until_complete(main())