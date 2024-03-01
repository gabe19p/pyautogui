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
root.geometry("500x600")

# logic to run inside the GUI
# 
# 
pt.FAILSAFE = True

clickData = []
clickDataInt = 0
loopCount = 0


# this function takes the coordinates ...
# (from the x and y ctk input fields) ...
# and then appends that data into the clickData list
def appendCoords():
    global clickDataInt
    # get data for x, y, and pause
    xD = xCoords.get()
    yD = yCoords.get()
    pD = longPause.get()
    coordInfo = {
        'x': xD,
        'y': yD,
        'p': pD,
    }
    print(f"Coord Info: {coordInfo}")
    clickData.append(coordInfo)
    print(f"ClickData: {clickData}")

    clickDataText = ctk.CTkLabel(frameBody1, text=f"Click {clickDataInt + 1}\nX: {clickData[clickDataInt]['x']}, Y: {clickData[clickDataInt]['y']}, Pause: {clickData[clickDataInt]['p']}")
    clickDataText.pack(pady = 2)

    clickDataInt += 1

# this function allows the user to ...
# hover their mouse over specific coordinates ...
# then it prints those coordinates ...
# for the user to see then append
def mouseCoordinates():
    sleep(3)
    currentMouseX, currentMouseY = pt.position() # Get the XY position of the mouse
    currentX.configure(text=f"X Coordinate: {currentMouseX}")
    currentY.configure(text=f"Y Coordinate: {currentMouseY}")
    return currentMouseX, currentMouseY

# this function executes the clicks
# 
# 
def startClicks():
    global loopCount
    currentCount = 0
    loopCount = int(loopsEntry.get())
    cycleTime = (int(cycleTimeEntry.get())*1000)
    spacebarStatus = spacebar.get()



    
    while currentCount < loopCount:
        # randomize the cycle time for each loop
        randomCycleTime = (random.randint(cycleTime, cycleTime+2000)/1000)
        # for loop to run through the clicks
        # all clicks happen first 
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
            print("End of click")
        
        # pick up here after all clicks
        if spacebarStatus == 'Yes':
            # pause for 1-2 seconds then press the space bar on the keyboard
            sleep(random.randint(1000,2000)/1000)
            keyboard.press_and_release('space')  
            sleep(randomCycleTime)
        else:
            # sleep for the random cycle and then run the clicks again
            sleep(randomCycleTime)
        currentCount += 1




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
# long pause
longPause = ctk.CTkCheckBox(frameBody1, checkbox_width = 16,
    checkbox_height= 16, border_width = 2, text="Extended pause after click", onvalue = 'Yes',
    offvalue = 'No')
longPause.pack(pady=5, padx=5, fill="both")
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
# loops input
loopsEntry = ctk.CTkEntry(actionFrame, placeholder_text='Loop count? Ex: 50')
loopsEntry.pack(pady=5, padx=5)
# cycle time input
cycleTimeEntry = ctk.CTkEntry(actionFrame, placeholder_text='Cycle time? Ex: 13')
cycleTimeEntry.pack(pady=5, padx=5)
# spacebar check
spacebar = ctk.CTkCheckBox(actionFrame, checkbox_width = 16,
    checkbox_height= 16, border_width = 2, text='SpaceBar', onvalue = 'Yes',
    offvalue = 'No')
spacebar.pack(pady=5, padx=5)
# start button
startButton = ctk.CTkButton(master=actionFrame, text="Start", fg_color="green", command=startClicks)
startButton.pack(pady=5, padx=5)
# stop button
# stopButton = ctk.CTkButton(master=actionFrame, text="Stop", fg_color="red", command=stopClicks)
# stopButton.pack(pady=5, padx=5)




root.mainloop()




