import PIL.ImageGrab
import mouse
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def get_pixel_colour(i_x, i_y):
	return PIL.ImageGrab.grab().load()[i_x, i_y]

while(0 > 1):
    pos = mouse.get_position()
    print(pos)
    time.sleep(0.5)

while(1 > 0):
    numberOdd = False
    numberSingle = True
    emergency = False

    if get_pixel_colour(1025, 215) != get_pixel_colour(1655, 300):
        numberSingle = False
        print("not single")
    if get_pixel_colour(1025, 215) == get_pixel_colour(1655, 300):
        numberSingle = True
        print("single")
    if get_pixel_colour(1075, 250) == get_pixel_colour(1655, 300):
        numberOdd = True
        print("number is odd")

    if numberOdd == True and numberSingle == True:
        emergency = True

    if emergency == True:
        print("BRO HELP HELP HELP HELP HELP")
        mouse.move(536, 994)
        mouse.click(button='left')
        keyboard.type('@everyone ONLY ONE PERSON IN CALL')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    time.sleep(5)