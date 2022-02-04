# Imports
import pyautogui
import PIL.ImageGrab
import time

# Function to get the colour of a pixel
def get_pixel_colour(i_x, i_y):
	return PIL.ImageGrab.grab().load()[i_x, i_y]
    
# Debug Tool - Get current mouse position (set the 0 to any number above 1 to activate)
while(0 > 1):
    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX, currentMouseY)
    print(get_pixel_colour(currentMouseX, currentMouseY))
    time.sleep(0.5)

# Gets the screen size
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

# Locations
joinCallButton = (887, 213)
messageBox = (515, 717)
orangeLocation = (120, 30)
closeBanner = (1348, 19)
membersList = (1095, 28)
evenOnly = (839, 110)
userLeft = (742, 107)
fourthUser = (668, 109)

# Colours
discordDarkGrey = (24, 25, 28)
discordGreen = (59, 165, 93)
discordOrange = (242, 101, 34)

# Main loop (Set 1 to 0 to deactivate)
time.sleep(5)
while (1 > 0):

    numPeople = 0
    twoPersonWait = 0

    # Close the Orange Banner
    if get_pixel_colour(orangeLocation[0], orangeLocation[1]):
        pyautogui.click(closeBanner[0], closeBanner[1])
    time.sleep(1)

    # Join the Call
    if get_pixel_colour(joinCallButton[0], joinCallButton[1]) == discordGreen:
        pyautogui.click(joinCallButton[0], joinCallButton[1])
    
    # Autoclicker
    pyautogui.click(membersList[0], membersList[1])
    pyautogui.click(membersList[0], membersList[1])
    
    # Main Call Checker
    if get_pixel_colour(evenOnly[0], evenOnly[1]) != discordDarkGrey:
        print("The number of people in the call is Odd\nPotentially Only 1\n Performing Further Checks")
        if get_pixel_colour(userLeft[0], userLeft[1]) == discordDarkGrey:
            # There is only 1 person in the call
            numPeople = 1
        else:
            numPeople = 3
    else:
        if get_pixel_colour(fourthUser[0], fourthUser[1]) != discordDarkGrey:
            numPeople = 2
        else:
            numPeople = 4
    
    print(numPeople)
    print("..users in call")
    match numPeople:
        case 1:
            print("Case 1")
            pyautogui.click(messageBox[0], messageBox[1])
            pyautogui.write("@everyone 1 Person in Call")
            pyautogui.press('enter')
        case 2:
            print("Case 2")
            if (twoPersonWait < 120):
                pyautogui.click(messageBox[0], messageBox[1])
                pyautogui.write("2 People in call... Another user should join")
                pyautogui.press('enter')
                twoPersonWait = twoPersonWait + 1
        case 3 | 4:
            print("Case 3 OR 4")
    time.sleep(1)
