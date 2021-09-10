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
    

# Locations
joinCallButton = (887, 213)
messageBox = (515, 717)
orangeLocation = (120, 30)
closeBanner = (1348, 19)
membersList = (1095, 28)
evenOnly = (839, 110)
userLeft = (742, 107)

# Colours
discordDarkGrey = (24, 25, 28)
discordGreen = (59, 165, 93)
discordOrange = (242, 101, 34)

# Main loop (Set 1 to 0 to deactivate)
time.sleep(5)
while(1 > 0):

    # Definitions
    numberOdd = True
    numberSingle = True

    # If there is an orange banner, close it
    if get_pixel_colour(orangeLocation[0], orangeLocation[1]) == discordOrange:
       mouse.move(closeBanner[0], closeBanner[1])
       mouse.click(button='left')
       time.sleep(1)

    # If the call button is green, click on it (If the bot leaves the call on it's own, it is because the program was started when the bot was already in the call)
    if get_pixel_colour(joinCallButton[0], joinCallButton[1]) == discordGreen:
       mouse.move(joinCallButton[0], joinCallButton[1])
       mouse.click(button='left')

    # Autoclicker so you dont go afk
    mouse.move(membersList[0], membersList[1])
    mouse.click(button='left')
    mouse.click(button='left')

    # Checks if not even
    if get_pixel_colour(evenOnly[0], evenOnly[1]) != discordDarkGrey:
        print("The number of people in the call is ODD\n Performing Further Checks...")
        # Checks if there is not more people in the call
        if get_pixel_colour(userLeft[0], userLeft[1]) == discordDarkGrey:
            print("EMERGENCY")
            mouse.move(messageBox[0], messageBox[1])
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