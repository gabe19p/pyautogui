# start off with installing the packages 
# pip install customtkinter pyautogui keyboard random

import customtkinter as ctk
import pyautogui as pt
import keyboard
import random
from time import sleep
import sys
import asyncio
import threading


# set the GUI color scheme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
# set the GUI size
root = ctk.CTk()
root.title("OSRS Clicker")
root.geometry("500x600")

# logic to run inside the GUI
# 
# 
pt.FAILSAFE = True

clickData = []
clickDataInt = 0
# global stop variable
stop = False
hotkey = 'f8'
function_running = False


# this function allows the user to ...
# hover their mouse over specific coordinates ...
# then it prints those coordinates ...
# for the user to see then append
def mouseCoordinates():
    global clickDataInt
    sleep(3)
    currentMouseX, currentMouseY = pt.position() # Get the XY position of the mouse
    # get data for x, y, and pause
    xD = currentMouseX
    yD = currentMouseY
    pD = longPause.get()
    coordInfo = {
        'x': xD,
        'y': yD,
        'p': pD,
    }
    clickData.append(coordInfo)
    clickDataText = ctk.CTkLabel(frameBody1, text=f"Click {clickDataInt + 1}\nX: {clickData[clickDataInt]['x']}, Y: {clickData[clickDataInt]['y']}, Pause: {clickData[clickDataInt]['p']}")
    clickDataText.pack(pady = 2)
    clickDataInt += 1
    return currentMouseX, currentMouseY
# functions to start and stop on the buttons
# adds threading on start and then looks for stop
def button_stop_clicks():
    # if the stop button is pressed, stop function
    global stop
    stop = True
# the threaded function that is called
# by the 'button_starter()'
def button_start_clicks():
    # see if the spacebar is checked
    spacebarStatus = spacebar.get()
    # see how long the user sets cycle time
    cycleTime = (int(cycleTimeEntry.get())*1000)
    # global stop variable for stopping the function
    global stop
    stop = False
    running = True
    while running == True and not stop:
        # randomize the cycle time for each loop
        randomCycleTime = (random.randint(cycleTime, cycleTime+2000)/1000)
        # for loop to run through the clicks; all clicks happen first 
        for click in clickData:
            randomX = random.randint(int(click['x'])-10,int(click['x'])+10)
            randomY = random.randint(int(click['y'])-10,int(click['y'])+10)
            drag = (random.randint(100, 120) / 1000)       
            if click['p'] == 'Yes':
                preClickPause = (random.randint(200,500) / 1000)
                postClickPause = (random.randint(2000, 3000) / 1000)
            else:
                preClickPause = (random.randint(200,500) / 1000)
                postClickPause = (random.randint(200, 500) / 1000)
            pt.moveTo(randomX, randomY, drag)
            sleep(preClickPause)
            pt.click()
            sleep(postClickPause)        
        # pick up here after all clicks
        if spacebarStatus == 'Yes':
            # pause for 1-2 seconds then press the space bar on the keyboard
            sleep(random.randint(1000,2000)/1000)
            keyboard.press_and_release('space')  
            sleep(randomCycleTime)
        else:
            print(f"Pause length: {randomCycleTime}")
            print("End of click cycle...")
            # sleep for the random cycle and then run the clicks again
            sleep(randomCycleTime)
# this is the function to start the clicks
# this is what is called on by the button
def button_starter():
    t = threading.Thread(target=button_start_clicks)
    t.start()
# 
# 
# 
# building the GUI
# 
# this is the main frame of the GUI
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)
# title of the program
title = ctk.CTkLabel(master=frame, text=("Click Automation"), font=('Roboto', 25))
title.pack(pady=20, padx=10)
# 
# 
# top frame
# 
# 
topFrame = ctk.CTkFrame(master=frame, fg_color="transparent")
topFrame.pack(pady=20, padx=20, side=ctk.TOP ,fill="both")
# 
# top left frame
# 
topLeftFrame = ctk.CTkFrame(topFrame, fg_color="transparent")
topLeftFrame.pack(pady=20, padx=20, side=ctk.LEFT ,fill="both")
# click label
clickLabel = ctk.CTkLabel(topLeftFrame, text="Click")
clickLabel.pack()
# click size
clickSize = ctk.CTkSlider(topLeftFrame, width=150, button_length=10, from_=1, to=3, number_of_steps=2)
clickSize.pack(pady=5, padx=5)
# add coords button
addCoords = ctk.CTkButton(topLeftFrame, text="Add Coordinates", command=mouseCoordinates)
addCoords.pack(pady=5, padx=5, side=ctk.BOTTOM)
# sleep entry
clickSleep = ctk.CTkEntry(topLeftFrame, placeholder_text="Sleep Time")
clickSleep.pack(pady=5, padx=5, side=ctk.BOTTOM)
# 
# top right frame
# 
topRightFrame = ctk.CTkFrame(topFrame, fg_color="transparent")
topRightFrame.pack(pady=20, padx=20, side=ctk.RIGHT ,fill="both")
# keys label
keyLabel = ctk.CTkLabel(topRightFrame, text="Key")
keyLabel.pack()
# key entry
keyEntry = ctk.CTkEntry(topRightFrame, placeholder_text="Key")
keyEntry.pack(pady=5, padx=5)
# sleep entry
keySleep = ctk.CTkEntry(topRightFrame, placeholder_text="Sleep Time")
keySleep.pack(pady=5, padx=5)
# add key button
addKey = ctk.CTkButton(topRightFrame, text="Add Key")
addKey.pack(pady=5, padx=5, side=ctk.RIGHT)
# 
# 
# bottom actions frame
# 
# 
bottomFrame = ctk.CTkFrame(master=frame, fg_color="transparent")
bottomFrame.pack(pady=20, padx=20, side=ctk.BOTTOM ,fill="both")
# 
# bottom left frame for starting the program
# 
leftFrame = ctk.CTkFrame(master=bottomFrame, fg_color="transparent")
leftFrame.pack(pady=20, padx=20, side=ctk.LEFT ,fill="both")

# 
# bottom right frame for starting the program
# 
rightFrame = ctk.CTkFrame(master=bottomFrame, fg_color="transparent")
rightFrame.pack(pady=20, padx=20, side=ctk.RIGHT ,fill="both")
# start button
startButton = ctk.CTkButton(master=rightFrame, text="Start", fg_color="green", command=button_starter)
startButton.pack(pady=5, padx=5)
# stop button
stopButton = ctk.CTkButton(master=rightFrame, text="Stop", fg_color="red", command=button_stop_clicks)
stopButton.pack(pady=5, padx=5)





root.mainloop()