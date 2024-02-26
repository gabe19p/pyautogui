from pynput.mouse import Listener

clickData = []

def on_click(x, y, button, pressed):
    if pressed:
        click_info = {
            'x': int(x),
            'y': int(y),
        }
        clickData.append(click_info)

    # Save clicks to a file
    printClicks()

def printClicks():
    print(clickData)

# Create a listener
with Listener(on_click=on_click) as listener:
    listener.join()


# from pynput.mouse import Listener

# clickData = []
          
# def addCoords(x, y, button, pressed):
#         click_info = {
#             'x': x,
#             'y': y,
#         }
#         clickData.append(click_info)

# with Listener(on_click=addCoords) as listener:
#     listener.join()

# print(f"X Coordinates: {clickData}")