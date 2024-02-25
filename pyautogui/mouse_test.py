from pynput import mouse

xCoords = []
yCoords = []

# need to figure out a way to set the original x,y coords for each item
# start off with one item            
def findCoords(x, y, button, pressed):
    xCoord = int(x)
    yCoord = int(y)
    xCoords.append(xCoord)
    yCoords.append(yCoord)
    return False

with mouse.Listener(on_click=findCoords) as listener:
    listener.join()
    listener.stop()

print(f"X Coordinates: {xCoords}")
print(f"Y Coordinates: {yCoords}")