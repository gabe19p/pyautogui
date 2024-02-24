import pyautogui as pt
import keyboard
import random
from time import sleep

screenWidth, screenHeight = pt.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pt.position() # Get the XY position of the mouse
pt.FAILSAFE = True

# set a half second sleep time before starting the program
sleep(1)
# print out the height/width of the screen and x/y coords
print(screenWidth, screenHeight)
print(currentMouseX, currentMouseY)