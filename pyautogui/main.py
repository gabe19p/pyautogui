import pyautogui as pt
import keyboard
import random
from time import sleep

screenWidth, screenHeight = pt.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pt.position() # Get the XY position of the mouse
pt.FAILSAFE = True

# set a half second sleep time before starting the program
sleep(0.5)
# print out the height/width of the screen and x/y coords
print(screenWidth, screenHeight)
print(currentMouseX, currentMouseY)
# the 2 lines below can be uncommented to start with an inventory click
# pt.moveTo(600, 350)
# pt.click()

# use an input variable to ask how many times to run the function and then count up with the cycle variable
userInput = input('How many cycles? ')
loopCount = int(userInput)
currentCycle = 0

# this while loop will run through the function
while currentCycle < loopCount:
    # below are a few different sleep variables to randomize the amount of milliseconds in the pauses
    pauseVariable1 = (random.randint(200,500) / 1000)
    pauseVariable2 = (random.randint(200,500) / 1000)
    pauseVariable3 = (random.randint(1000,1300) / 1000)
    pauseVariable4 = (random.randint(13000,16000) / 1000)
    print(pauseVariable1)
    print(pauseVariable2)
    print(pauseVariable3)
    print(pauseVariable4)
    # below are a few different location variables to alter the x,y coords
    x1Variable = random.randint(575,585)
    x2Variable = random.randint(575,585)
    y1Variable = random.randint(245,255)
    y2Variable = random.randint(285,295)
    # action for the first click of the function
    # start with a move, a pause, then a click
    pt.moveTo(x1Variable, y1Variable)
    sleep(pauseVariable1)
    pt.click()
    # action for the second click of the function
    # start with a move, a pause, then a click
    pt.moveTo(x2Variable, y2Variable)
    sleep(pauseVariable2)
    pt.click()
    # press and release a keyboard action 
    # comment this out if not action is needed from the keyboard
    sleep(pauseVariable3)
    keyboard.press_and_release('space')  
    # change this sleep cycle for the amount of time it takes to complete the action
    currentCycle += 1
    print(currentCycle)
    sleep(pauseVariable4)


# references
# 1000 milliseconds in 1 second