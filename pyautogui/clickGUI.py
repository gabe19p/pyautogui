# start off with installing the packages 
# pip install customtkinter pyautogui keyboard random

import customtkinter as ctk
import pyautogui as pt
import keyboard
import random
from time import sleep
import sys

# set the GUI color scheme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
# set the GUI size
root = ctk.CTk()
root.title("OSRS Clicker")
root.geometry("600x600")

# logic to run inside the GUI
# 
# 
pt.FAILSAFE = True

clickCount = 0

# def updateClickCount():
#     # initialize click
#     click = 0
#     clickCount = int(clickCountInput.get())
#     # loop that will print all items
#     while click < clickCount:

#         click += 1


# function to get coordinates
def mouseCoordinates():
    sleep(3)
    currentMouseX, currentMouseY = pt.position() # Get the XY position of the mouse
    currentX.configure(text=f"X Coordinate: {currentMouseX}")
    currentY.configure(text=f"Y Coordinate: {currentMouseY}")
    return currentMouseX, currentMouseY

# clicking function
def automatedClicks():
    try:
        # below are a few different sleep variables to randomize the amount of milliseconds in the pauses
        pauseVariable1 = (random.randint(200,500) / 1000)
        pauseVariable2 = (random.randint(200,500) / 1000)
        pauseVariable3 = (random.randint(1000,1300) / 1000)
        pauseVariable4 = (random.randint(13000,16000) / 1000)
        # below are a few different location variables to alter the x,y coords
        x1Variable = random.randint(575,595)
        x2Variable = random.randint(575,595)
        y1Variable = random.randint(295,315)
        y2Variable = random.randint(335,350)
        # below are the drag variables to spice up the speed of the mouse movement
        dragVariable1 = (random.randint(100,200) / 1000)
        dragVariable2 = (random.randint(90, 210) / 1000)
        # action for the first click of the function
        # start with a move, a pause, then a click
        pt.moveTo(x1Variable, y1Variable, dragVariable1)
        sleep(pauseVariable1)
        pt.click()
        # action for the second click of the function
        # start with a move, a pause, then a click
        pt.moveTo(x2Variable, y2Variable, dragVariable2)
        sleep(pauseVariable2)
        pt.click()
        # press and release a keyboard action 
        # comment this out if not action is needed from the keyboard
        sleep(pauseVariable3)
        keyboard.press_and_release('space')  
        # change this sleep cycle for the amount of time it takes to complete the action
        sleep(pauseVariable4)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit_program()

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

# building the GUI
# 
# this is the main frame of the GUI
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)
# title of the program
title = ctk.CTkLabel(master=frame, text=("Click Automation"), font=('Roboto', 25))
title.pack(pady=20, padx=10)


# coordinates 1 frames
# 
# 
frameBody1 = ctk.CTkFrame(master=frame, fg_color="transparent")
frameBody1.pack(ipady=5, fill="none", expand=True)
# label for the first clicks
label1 = ctk.CTkLabel(master=frameBody1, text="Click 1 Coordinates")
label1.pack()
# x coord
xCoords1 = ctk.CTkEntry(master=frameBody1, placeholder_text="x", width=200)
xCoords1.pack(pady=5, padx=5, fill="both")
# y coord
yCoords1 = ctk.CTkEntry(master=frameBody1, placeholder_text="y", width=200)
yCoords1.pack(pady=5, padx=5, fill="both")

# coordinates 2 frames
# 
# 
frameBody2 = ctk.CTkFrame(master=frame, fg_color="transparent")
frameBody2.pack(ipady=5, fill="none", expand=True)
# label for the first clicks
label2 = ctk.CTkLabel(master=frameBody2, text="Click 2 Coordinates")
label2.pack()
# x coord
xCoords2 = ctk.CTkEntry(master=frameBody2, placeholder_text="x", width=200)
xCoords2.pack(pady=5, padx=5, fill="both")
# y coord
yCoords2 = ctk.CTkEntry(master=frameBody2, placeholder_text="y", width=200)
yCoords2.pack(pady=5, padx=5, fill="both")

bottomFrame = ctk.CTkFrame(master=frame, fg_color="transparent")
bottomFrame.pack()

# location frame
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

# frame for starting the program
# 
# 
actionFrame = ctk.CTkFrame(master=bottomFrame, fg_color="transparent")
actionFrame.pack(side=ctk.RIGHT, padx=20)
# start button
startButton = ctk.CTkButton(master=actionFrame, text="Start", fg_color="green", command=automatedClicks)
startButton.pack(pady=5, padx=5)
# stop button
stopButton = ctk.CTkButton(master=actionFrame, text="Stop", fg_color="red", command=exit_program)
stopButton.pack(pady=5, padx=5)


root.mainloop()




# field to take the amount of clicks
# clickCountLabel = ctk.CTkLabel(master=frame, text="How many actions do you have?")
# clickCountLabel.pack()
# # input field to track the amount of clicks
# clickCountInput = ctk.CTkEntry(master=frame, placeholder_text="Ex: 3")
# clickCountInput.pack()
# # button to save action count
# clickCountButton = ctk.CTkButton(master=frame, text="Next", command=updateClickCount)
# clickCountButton.pack()