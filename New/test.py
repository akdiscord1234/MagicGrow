import matplotlib
import customtkinter

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

#Init setup
#apperance
customtkinter.set_appearance_mode("System") # can also use "System", "Dark", and "Light"
customtkinter.set_default_color_theme("green") # Themes, blue, green, dark-blue, ect
#root
app = customtkinter.CTk()
app.geometry("1200x500")
app.title("MagicGrow")

Label = customtkinter.CTkLabel(master=app, text="This is a test program")

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

figure_canvas.get_tk_widget().pack()

Label.pack()
app.mainloop()