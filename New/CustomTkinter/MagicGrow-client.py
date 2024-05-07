#Import libraries
import customtkinter

#Init setup
#apperance
customtkinter.set_appearance_mode("System") # can also use "System", "Dark", and "Light"
customtkinter.set_default_color_theme("green") # Themes, blue, green, dark-blue, ect
#root
app = customtkinter.CTk()
app.geometry("600x500")
app.title("MagicGrow")

#Tabview
tabview = customtkinter.CTkTabview(master=app)
tabview.grid()

#Grid Configure Layout
app.columnconfigure((0, 1), weight=1)
app.rowconfigure((0, 1), weight=1)

# Content
MagicGrowLabel = customtkinter.CTkLabel(master=app, text="MagicGrow Home", text_color="green", font=("Calibri", 44))

#Temperature schedule

#EC schedule

#Light On/Off schedule

#Water Pump schedule

#Placing Widgets Layout

MagicGrowLabel.grid(row=0, column=0, padx=20)

app.mainloop()