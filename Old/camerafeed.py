import tkinter as tk
import cv2
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Camera Feed")

# Create a canvas to display the camera feed
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Open the camera
cap = cv2.VideoCapture(0)

def show_frame():
    # Get a frame from the camera
    ret, frame = cap.read()

    if ret:
        # Convert the frame to an RGB image
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the image to a PIL image
        img = Image.fromarray(frame)

        # Convert the PIL image to a Tkinter image
        photo = ImageTk.PhotoImage(image=img)

        # Display the image on the canvas
        canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    # Call this function again after 15 milliseconds
    root.after(15, show_frame)

# Start the camera feed
show_frame()

# Start the main loop
root.mainloop()