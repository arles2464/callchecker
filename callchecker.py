# WARNING
#
# This code is extremely shit. It will break as soon as discord updates it's interface, or if it isn't aren't in the correct tab, or if the browser is not Firefox with no bookmarks
# (it might work on others, not tested yet), or if someone is screen-sharing
#
# This code also probably (maybe, idk) chugs RAM like a motherfucker, so probably restart it once in a while to stop it from crashing your PC

# Imports
import PIL.ImageGrab
import mouse
from pynput.keyboard import Key, Controller
import time

# Creates Keyboard Controller (needed for key presses)
keyboard = Controller()

# Function to get the colour of a pixel
def get_pixel_colour(i_x, i_y):
	return PIL.ImageGrab.grab().load()[i_x, i_y]

# Debug Tool - Get current mouse position (set the 0 to any number above 1 to activate)
while(0 > 1):
    pos = mouse.get_position()
    print(pos)
    print(get_pixel_colour(pos[0], pos[1]))
    time.sleep(0.5)
    

discordDarkGrey = (24, 25, 28)

# Gets the colour of the join call button
discordGreen = (59, 165, 93)

# Gets the colour of the orange banner
discordOrange = (242, 101, 34)

# Main loop (Set 1 to 0 to deactivate)
while(1 > 0):

    # Definitions
    numberOdd = True
    numberSingle = True

    # If there is an orange banner, close it
    if get_pixel_colour(93, 30) == discordOrange:
       mouse.move(1900, 16)
       mouse.click(button='left')
       time.sleep(1)

    # If the call button is green, click on it (If the bot leaves the call on it's own, it is because the program was started when the bot was already in the call)
    if get_pixel_colour(1165, 212) == discordGreen:
       mouse.move(1165, 212)
       mouse.click(button='left')

    # Autoclicker so you dont go afk
    mouse.move(470, 1030)
    mouse.click(button='left')

    # Checks if not even
    if get_pixel_colour(1115, 110) != discordDarkGrey:
        print("The number of people in the call is ODD\n Performing Further Checks...")
        # Checks if there is not more people in the call
        if get_pixel_colour(1020, 110) == discordDarkGrey:
            print("EMERGENCY")
            mouse.move(470, 1030)
            mouse.click(button='left')
            keyboard.type('@everyone ONLY ONE PERSON IN CALL')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        else:
            print("3 or more people in the call\n All Clear")
    else:
        print("2 or More People in the Call\n All Clear")
    # Waits 5 seconds before re-checking
    time.sleep(5)