# start off with installing the packages 
# pip install customtkinter pyautogui keyboard random

import customtkinter as ctk
import pyautogui as pt
import keyboard
import random
from time import sleep
import sys
import asyncio


# set the GUI color scheme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
# set the GUI size
root = ctk.CTk()
root.title("OSRS Clicker")
root.geometry("400x600")

# logic to run inside the GUI
# 
# 
pt.FAILSAFE = True


clickData = []
clickDataInt = 0
 
def appendCoords():
    global clickDataInt
    xD = xCoords.get()
    yD = yCoords.get()
    coordInfo = {
        'x': xD,
        'y': yD
    }
    print(f"Coord Info: {coordInfo}")
    clickData.append(coordInfo)
    print(f"ClickData: {clickData}")

    clickDataText = ctk.CTkLabel(frameBody1, text=f"Click {clickDataInt + 1}\nX: {clickData[clickDataInt]['x']}, Y: {clickData[clickDataInt]['y']}")
    clickDataText.pack()

    clickDataInt += 1




# function to get coordinates
def mouseCoordinates():
    sleep(3)
    currentMouseX, currentMouseY = pt.position() # Get the XY position of the mouse
    currentX.configure(text=f"X Coordinate: {currentMouseX}")
    currentY.configure(text=f"Y Coordinate: {currentMouseY}")
    return currentMouseX, currentMouseY


# building the GUI
# 
# this is the main frame of the GUI
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)
# title of the program
title = ctk.CTkLabel(master=frame, text=("Click Automation"), font=('Roboto', 25))
title.pack(pady=20, padx=10)

# insert coordinates frames
# 
# ##########
frameBody1 = ctk.CTkFrame(master=frame, fg_color="transparent")
frameBody1.pack(ipady=5, fill="none")
# label for the first clicks
label = ctk.CTkLabel(master=frameBody1, text="Add Coordinates")
label.pack()
# x coord
xCoords = ctk.CTkEntry(master=frameBody1, placeholder_text="x", width=200)
xCoords.pack(pady=5, padx=5, fill="both")
# y coord
yCoords = ctk.CTkEntry(master=frameBody1, placeholder_text="y", width=200)
yCoords.pack(pady=5, padx=5, fill="both")
# add coords button
addCoords = ctk.CTkButton(frameBody1, text="Add Coordinates", command=appendCoords)
addCoords.pack(pady=5, padx=5, fill="both")

# bottom actions frame
# 
# #########
bottomFrame = ctk.CTkFrame(master=frame, fg_color="transparent")
bottomFrame.pack(pady=20, padx=20, side=ctk.BOTTOM ,fill="both")
# bottom left frame for finding location
# 
locateFrame = ctk.CTkFrame(master=bottomFrame, fg_color="transparent")
locateFrame.pack(side=ctk.LEFT, padx=20)
# location button
coordinatesButton = ctk.CTkButton(master=locateFrame, text="Locate Coordinates", command=mouseCoordinates)
coordinatesButton.pack(pady=5, padx=5)
# paste x location
currentX = ctk.CTkLabel(master=locateFrame, text="X Coordinate: ")
currentX.pack()
# paste y location
currentY = ctk.CTkLabel(master=locateFrame, text="Y Coordinate: ")
currentY.pack()
# bottom right frame for starting the program
# 
# 
actionFrame = ctk.CTkFrame(master=bottomFrame, fg_color="transparent")
actionFrame.pack(side=ctk.RIGHT, padx=20)
# start button
startButton = ctk.CTkButton(master=actionFrame, text="Start", fg_color="green")
startButton.pack(pady=5, padx=5)
# stop button
stopButton = ctk.CTkButton(master=actionFrame, text="Stop", fg_color="red")
stopButton.pack(pady=5, padx=5)




root.mainloop()




