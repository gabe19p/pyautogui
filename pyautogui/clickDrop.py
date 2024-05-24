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
root.geometry("500x500")

# logic to run inside the GUI
# 
# 
pt.FAILSAFE = True

# global stop variable
stop = False

# functions
def button_stop_clicks():
    # if the stop button is pressed, stop function
    print("Stopping clicks")
    pt.moveTo(0,5000)
    global stop
    stop = True
def button_start_clicks():
    global stop
    stop = False
    running = True
    # begin script
    print("Starting clicks in 3 seconds...")
    sleep(3)
    while running == True and not stop:
        pt.click()
        sleep(random.randint(50,100) / 1000)
        keyboard.press('F2')
        sleep(random.randint(100,200) / 1000)

def button_starter():
    t = threading.Thread(target=button_start_clicks)
    t.start()

# 
# building the GUI 
# 
# this is the main frame of the GUI
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)
# title of the program
title = ctk.CTkLabel(master=frame, text=("Click & Drop Automation"), font=('Roboto', 25))
title.pack(pady=20, padx=10)


# start button
startButton = ctk.CTkButton(master=frame, text="Start", fg_color="green", command=button_starter)
startButton.pack(pady=5, padx=5)
# stop button
stopButton = ctk.CTkButton(master=frame, text="Stop", fg_color="red", command=button_stop_clicks)
stopButton.pack(pady=5, padx=5)


root.mainloop()