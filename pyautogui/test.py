from pynput import keyboard
import threading
import time

# Define your function
def my_function(stop_event):
    while not stop_event.is_set():
        print("Function is running...")
        # Do whatever you want the function to do
        time.sleep(1)  # Placeholder for some task

# Flag to keep track of whether the function is running or not
function_running = False
stop_event = threading.Event()

# Function to toggle the function
def toggle_function():
    global function_running
    global stop_event
    if function_running:
        function_running = False
        stop_event.set()
        print("Function stopped.")
    else:
        function_running = True
        stop_event.clear()
        print("Function started.")
        threading.Thread(target=my_function, args=(stop_event,)).start()

# Define the hotkey
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('f'),
    toggle_function
)

# Listener for hotkey
listener = keyboard.Listener(on_press=hotkey.press)
listener.start()

try:
    # Keep the script running
    listener.join()
except KeyboardInterrupt:
    # Handle KeyboardInterrupt to gracefully exit
    listener.stop()
    print("Exiting...")