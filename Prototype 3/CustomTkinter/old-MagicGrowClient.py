import customtkinter
from PIL import Image
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


print("takes about 10-15 seconds to load, please wait")

current_pH = 5.8
current_EC = 3.4
current_temperature = 30

print("pH done, window initializing")
#customtkinter window

#set appearance and theme
customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")  # default

#initial setup
app = customtkinter.CTk()
#root.geometry("700x700") uses maximized window
app.title("MagicGrow")

#tabview setup
tabview = customtkinter.CTkTabview(master=app)
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

temperatureImage = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Temp_icon.jpg"),
                                          dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Temp_icon.jpg"),
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

pHImage = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\pH_icon.jpg"),
                                 dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\pH_icon.jpg"),
                                 size=(70, 70))

pHImageLabel = customtkinter.CTkLabel(master=pHFrame, image=pHImage, text="")  # display image with a CTkLabel
pHImageLabel.grid(row=3, column=0)

#light frame in Homepage
lightFrame = customtkinter.CTkScrollableFrame(master=tabview.tab("Homepage 🏠"), width=200, height=200)
lightFrame.place(relx=0.2, rely=0.6, anchor='w')

global choice1
choice1 = "light on"
def light_option_menu(choice1):
    print("optionmenu dropdown clicked:", choice1)


optionmenu = customtkinter.CTkOptionMenu(master=lightFrame, values=["light on", "light off"],
                                         command=light_option_menu)
optionmenu.set(choice1)

#lightEntry = customtkinter.CTkEntry(master=lightFrame, placeholder_text=str(str(current_light_state)))
optionmenu.grid(padx=20, pady=20)

lightView = customtkinter.CTkLabel(master=lightFrame, text= str(choice1), font=("arial", 22))
lightView.grid(padx=20, pady=20)

lightImage = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Light_icon.png"),
                                    dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Light_icon.png"),
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


ECImage = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Ec_icon.jpg"),
                                 dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Ec_icon.jpg"),
                                 size=(70, 70))

ECImageLabel = customtkinter.CTkLabel(master=ECFrame, image=ECImage, text="")  # display image with a CTkLabel
ECImageLabel.grid(row=3, column=0)

#Water Pump Up frame in Homepage
WaterPumpUpFrame = customtkinter.CTkScrollableFrame(master=tabview.tab("Homepage 🏠"), width=200, height=200)
WaterPumpUpFrame.place(relx=0.6, rely=0.2, anchor='w')

#WaterPumpUpEntry = customtkinter.CTkEntry(master=WaterPumpUpFrame, placeholder_text=str("Water Pump is " + str(current_WaterPumpUp_str)))
#WaterPumpUpEntry.grid(padx=20, pady=20)

current_WaterPumpUp_str = "ON"

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


WaterPumpUpImage = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\PumpON_icon.jpg"),
                                          dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\PumpON_icon.jpg"),
                                          size=(70, 70))

WaterPumpUpImageLabel = customtkinter.CTkLabel(master=WaterPumpUpFrame, image=WaterPumpUpImage, text="")  # display image with a CTkLabel
WaterPumpUpImageLabel.grid(row=3, column=0)

#Water Pump Down frame in Homepage
WaterPumpDownFrame = customtkinter.CTkScrollableFrame(master=tabview.tab("Homepage 🏠"), width=200, height=200)
WaterPumpDownFrame.place(relx=0.6, rely=0.6, anchor='w')

#WaterPumpDownEntry = customtkinter.CTkEntry(master=WaterPumpDownFrame, placeholder_text=str("Water Pump is " + str(current_WaterPumpDown_str)))
#WaterPumpDownEntry.grid(padx=20, pady=20)
current_WaterPumpDown_str = "OFF"

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


WaterPumpDownImage = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\PumpOFF_icon.jpg"),
                                           dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\PumpOFF_icon.jpg"),
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

#GRAPH CODE HERE

side_icon = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Side_icon.png"),
                                   dark_image=Image.open(r"C:\Users\kavet\OneDrive\Documents\GitHub\MagicGrow\Prototype 3\CustomTkinter\Images\Side_icon.png"),
                                   size=(210, 210))

side_icon_label = customtkinter.CTkLabel(tabview.tab("Homepage 🏠"), image=side_icon, text="")  # display image with a CTkLabel
side_icon_label.pack(side="bottom")

try:
    app.after(0, lambda: app.state('zoomed'))
    app.mainloop()

except:
    print("the last 2 lines of code don't work")