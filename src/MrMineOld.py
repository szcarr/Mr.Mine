'''
OUTDATED FILE
ONLY KEPT AROUND JUST INCASE I NEED SOMETHING
'''


import pyautogui
import keyboard
import time

pyautogui.FAILSAFE = True
defaultDelay = 0.00000000000001 #Default value should be 0.02 i think
amountOfFloorsInMrMine = 1337

'''
When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort your program:
'''

# 0,0       X increases -->
# +---------------------------+
# |                           | Y increases
# |                           |     |
# |   1920 x 1080 screen      |     |
# |                           |     V
# |                           |
# |                           |
# +---------------------------+ 1919, 1079

#Values got at 1920 x 1080 screen
originalResolution = 1920, 1080

#currentResolution needs to be the resolution currently used by your monitor
currentResolution = 2560, 1440 #1920, 1080
'''
---------------------------------------------------MINER-INFO---------------------------------------------------
'''

'''
    These values are gotten at 1920x1080 screen
    New values need to be relative to 1920x1080 screen 
    See MrMineMath.py -> convertToCurrentResolutionPosition() function for more details
'''

menuDoubleClick = 935, 175

doubleArrowTop = 110, 200
oneArrowDown = 107, 906

clickChestInMiddleOfScreen = 969, 557

#Selling
sellButton = 622, 758
amountOfMineralSellPlaces = 2

#Miner position
minerYpositionMiddleLevel = 608
minerYpositionLowestLevel = 975
minerPosistionList = [
    190,
    329,
    470,
    609,
    746,
    885,
    1017,
    1163,
    1295, 
    1434,
]

#Minefloors spots to skip #NOT IN USE
mineFloorsThatIsDifferentToMiners = [
    20,
    45
]

modeList = {
    "getC": "GetCurrentPosition | Prints current XY value of mouse position | CTRL C to escape | Syntax: getc",
    "help": "Help | Prints all legal commands | Syntax: help",
    "exit": "Exit | Exits current program | Syntax: exit"
}

#runTime = time.process_time()


'''
-------------------------AUTOGUI-------------------------
'''
def doAutoEverythingBySequence():
    doFullscreen()
    doCollectAllPotensialChests()

def doEverythingWithExtraFailsafe():
    #Adding later
    print()

def doFullscreen():
    pyautogui.moveTo(menuDoubleClick)
    time.sleep(defaultDelay)
    pyautogui.doubleClick()
    time.sleep(defaultDelay)

def doCollectAllPotensialChests():
#while True:
#Outdated
    pyautogui.moveTo(doubleArrowTop)
    time.sleep(defaultDelay)
    pyautogui.click()
    time.sleep(defaultDelay)
    pyautogui.click()
    time.sleep(defaultDelay)
    for y in range(amountOfFloorsInMrMine):
        skip = False
        for l in range(len(mineFloorsThatIsDifferentToMiners)):
            if y == mineFloorsThatIsDifferentToMiners[l]:
                skip = True
        if skip:
            continue
        for i in range(len(minerPosistionList)):
            pyautogui.moveTo(minerPosistionList[i], minerYpositionLowestLevel)
            time.sleep(defaultDelay)
            pyautogui.click()
            time.sleep(defaultDelay)
            pyautogui.moveTo(clickChestInMiddleOfScreen)
            time.sleep(defaultDelay)
            pyautogui.click()
            time.sleep(defaultDelay)
        pyautogui.moveTo(oneArrowDown)
        time.sleep(defaultDelay) 
        pyautogui.click()
        time.sleep(defaultDelay)

def collectChests():
    #Main lol
    hop = True
    future = 0
    sellingTime = 0
    while True:
        pressedSpace = False
        now = time.process_time()
        if hop:
            pyautogui.moveTo(convertToCurrentResolutionPosition(clickChestInMiddleOfScreen[0]), convertToCurrentResolutionPosition(clickChestInMiddleOfScreen[1])) 
            clickMouse()
            future = now + 0.001
            sellingTime = now + 0.1
            hop = False
        if now > future:
            keyboard.press_and_release('space')
            pressedSpace = True
        if pressedSpace:
            for everyMiner in range(len(minerPosistionList)):
                pyautogui.moveTo(convertToCurrentResolutionPosition(minerPosistionList[everyMiner]), convertToCurrentResolutionPosition(minerYpositionMiddleLevel))
                clickMouse()
                clickChestInMiddleOfScreens()
        now = time.process_time()
        print(now, sellingTime)


def sellMinerals():
    #goto mr mine screen
    pyautogui.moveTo(convertToCurrentResolutionPosition(doubleArrowTop[0]), convertToCurrentResolutionPosition(doubleArrowTop[1]))
    clickMouse()
    for everyTrader in range(amountOfMineralSellPlaces):
        time.sleep(defaultDelay)
        pressButton("s")
        pyautogui.moveTo(convertToCurrentResolutionPosition(sellButton[0]), convertToCurrentResolutionPosition(sellButton[1]))
        time.sleep(defaultDelay + 0.01)
        clickMouse()
    clickMouse()

'''
-------------------------FORMULAS-------------------------
'''

'''
-------------------------GUI HELPERS-------------------------
'''

def getCurrentPosition():
    while True: 
        print(pyautogui.position())
        time.sleep(1)

def getScreenResoution():
    return pyautogui.size()

'''
-------------------------GENERAL HELPERS-------------------------
'''

def clickMouse():
    pyautogui.click()
    time.sleep(defaultDelay)

def pressButton(button):
    #button is a string
    #eksample: button = "s"
    pyautogui.press(button)
    time.sleep(defaultDelay)

def clickChestInMiddleOfScreens():
        pyautogui.moveTo(convertToCurrentResolutionPosition(clickChestInMiddleOfScreen[0]), convertToCurrentResolutionPosition(clickChestInMiddleOfScreen[1]))
        time.sleep(defaultDelay)
        clickMouse()
        clickMouse()

'''
-------------------------MAIN PROGRAM-------------------------
'''

#print(pyautogui.KEYBOARD_KEYS)

#MAIN
collectChests()

#menu()  
#doAutoEverythingBySequence()
#doCollectAllPotensialChests()
#sellMinerals()