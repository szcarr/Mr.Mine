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

#Minefloors spots to skip
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
-------------------------MENU-------------------------
'''

def menu():
    exitProgram = False
    while True:
        if exitProgram:
            break
        printHelp()
        print("> ", end="")
        mode = input()
        checkModes(mode)

def checkModes(mode):
    try:
        modeList = mode.split(" ")
        print(modeList)
        print(modeList[0])
        if modeList[0] == "getc":
            getCurrentPosition()
        elif modeList[0] == "help":
            printHelp()
        elif modeList[0] == "exit":
            exit()
    except:
        print("Error in selecting mode")

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
            pyautogui.moveTo(clickChestInMiddleOfScreen) 
            clickMouse()
            future = now + 0.001
            sellingTime = now + 0.1
            hop = False
        if now > future:
            keyboard.press_and_release('space')
            pressedSpace = True
        if pressedSpace:
            for everyMiner in range(len(minerPosistionList)):
                pyautogui.moveTo(minerPosistionList[everyMiner], minerYpositionMiddleLevel)
                clickMouse()
                clickChestInMiddleOfScreens()
        now = time.process_time()
        print(now, sellingTime)
        if now > sellingTime:
            #sellMinerals()
            sellingTime = now + 0.1


def sellMinerals():
    #goto mr mine screen
    pyautogui.moveTo(doubleArrowTop)
    clickMouse()
    for everyTrader in range(amountOfMineralSellPlaces):
        time.sleep(defaultDelay)
        pressButton("s")
        pyautogui.moveTo(sellButton)
        time.sleep(defaultDelay)
        clickMouse()
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

def printHelp():
    keysForModeList = list(modeList.keys())
    counter = 0
    print("\n-------------------------HELP-------------------------")
    for key in keysForModeList:
        counter += 1
        print(str(counter) + ": " + str(modeList.get(key)))

def clickMouse():
    pyautogui.click()
    time.sleep(defaultDelay)

def pressButton(button):
    #button is a string
    #eksample: button = "s"
    pyautogui.press(button)
    time.sleep(defaultDelay)

def clickChestInMiddleOfScreens():
        pyautogui.moveTo(clickChestInMiddleOfScreen)
        time.sleep(defaultDelay)
        clickMouse()
        clickMouse()
'''
-------------------------MAIN PROGRAM-------------------------
'''

#print(pyautogui.KEYBOARD_KEYS)

collectChests()
#menu()  
#doAutoEverythingBySequence()
#doCollectAllPotensialChests()
#sellMinerals()