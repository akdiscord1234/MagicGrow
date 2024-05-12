import customtkinter
from PIL import Image

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
    print("optionmenu dropdown clicked:", choice)

#Light Switch
def switch_event_Light():
    print("switch toggled, current value:", switch_var_Light.get())

switch_var_Light = customtkinter.StringVar(value="on")

#Temperature Enter Button
def Temperature_Enter_Button():
    pass

#pH Enter Button
def pH_Enter_Button():
    pass

#EC Enter Button
def EC_Enter_Button():
    pass

#GridConfigure for Homepage
HomePageTab.columnconfigure(0, weight=2)
HomePageTab.columnconfigure(1, weight=2)
HomePageTab.columnconfigure(2, weight=2)
HomePageTab.rowconfigure(0, weight=2)
HomePageTab.rowconfigure(1, weight=2)
HomePageTab.rowconfigure(2, weight=2)

#Side Icon

Side_Icon_Image = customtkinter.CTkImage(dark_image=Image.open(r"C:\Users\kavet\PycharmProjects\MagicGrow\New\CustomTkinter\Images\Side_icon.png"), size=(200, 200))
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

TemperatureImage = customtkinter.CTkImage(dark_image=Image.open(r"C:\Users\kavet\PycharmProjects\MagicGrow\New\CustomTkinter\Images\Temp_icon.jpg"), size=(83, 116))
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

pHImage = customtkinter.CTkImage(dark_image=Image.open(r"C:\Users\kavet\PycharmProjects\MagicGrow\New\CustomTkinter\Images\pH_icon.jpg"), size=(100, 100))
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

ECImage = customtkinter.CTkImage(dark_image=Image.open(r"C:\Users\kavet\PycharmProjects\MagicGrow\New\CustomTkinter\Images\Ec_icon.jpg"), size=(100, 100))
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

LightImage = customtkinter.CTkImage(dark_image=Image.open(r"C:\Users\kavet\PycharmProjects\MagicGrow\New\CustomTkinter\Images\Light_icon.png"), size=(100, 100))
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

WaterPumpImage = customtkinter.CTkImage(dark_image=Image.open(r"C:\Users\kavet\PycharmProjects\MagicGrow\New\CustomTkinter\Images\WaterPump_Icon.jpeg"), size=(100, 100))
WaterPumpImageHolder = customtkinter.CTkLabel(master=WaterPumpFrame, image=WaterPumpImage, text="")
WaterPumpImageHolder.pack(side="top")

#mainloop

app.mainloop()
