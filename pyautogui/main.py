import pyautogui as pt
import keyboard
from time import sleep

screenWidth, screenHeight = pt.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pt.position() # Get the XY position of the mouse
pt.FAILSAFE = True

# set a half second sleep time before starting the program
sleep(0.5)
# print out the height/width of the screen and x/y coords
print(screenWidth, screenHeight)
print(currentMouseX, currentMouseY)

# use an input variable to ask how many times to run the function
userInput = input('How many cycles? ')
loopCount = int(userInput)
currentCycle = 0

# click in the invent
pt.moveTo(600, 350)
pt.click()


# this while loop will run through the function
while currentCycle < loopCount:
    # move mouse to top item
    pt.moveTo(580, 250)
    sleep(0.2)
    pt.click()
    # pause then move to next
    sleep(0.5)
    # move mouse to bottom item
    pt.moveTo(585, 290)
    sleep(0.2)
    pt.click()
    # press and release a keyboard action 
    # comment this out if not action is needed from the keyboard
    sleep(1)
    keyboard.press_and_release('space')  

    # change this sleep cycle for the amount of time it takes to complete the action
    currentCycle += 1
    print(currentCycle)
    sleep(13)
