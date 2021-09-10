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
    time.sleep(0.5)

# Gets the colour of the join call button
discordGreen = get_pixel_colour(1160, 303)

# Main loop (Set 1 to 0 to deactivate)
while(1 > 0):

    # Definitions
    numberOdd = False
    numberSingle = True
    emergency = False

    # If the call button is green, click on it (If the bot leaves the call on it's own, it is because the program was started when the bot was already in the call)
    if get_pixel_colour(1160, 303) == discordGreen:
       mouse.move(1160, 303)
       mouse.click(button='left')

    # Autoclicker so you dont go afk
    mouse.move(536, 994)
    mouse.click(button='left')

    # Checks if the person in the call IS NOT the only person in the call by comparing the pixel colour to the colour of the blackish grey background
    if get_pixel_colour(1052, 191) != get_pixel_colour(884, 129) and get_pixel_colour(1176, 191) != get_pixel_colour(884, 129):
        numberSingle = False
        print("not single")
    # Checks if the person in the call IS the oly person in the call (see above for details)
    if get_pixel_colour(1052, 191) == get_pixel_colour(884, 129) and get_pixel_colour(1176, 191) == get_pixel_colour(884, 129):
        numberSingle = True
        print("single")
    # Checks if the amount of people in the call is odd (see above for details)
    if get_pixel_colour(1052, 191) == get_pixel_colour(884, 129):
        numberOdd = True
        print("number is odd")
    # If number of people is NOT odd, print that it is even
    if numberOdd == False:
        print("number is even")

    # If the number of people in the call is odd, and it is NOT 'not single', set the emergency variable to true
    if numberOdd == True and numberSingle == True:
        emergency = True

    # If we are in a call emergency (see above) then alert the call by pinging it
    if emergency == True:
        print("BRO HELP HELP HELP HELP HELP")
        mouse.move(536, 994)
        mouse.click(button='left')
        keyboard.type('@everyone ONLY ONE PERSON IN CALL')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    # Waits 5 seconds before re-checking
    time.sleep(5)