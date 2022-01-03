import pyautogui
import keyboard
import time

import MrMineMath

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
    Mr mine needs to be in "fullscreen" then you can get the coords for

    These values are gotten at 1920x1080 screen
    New values need to be relative to 1920x1080 screen 
    See MrMineMath.py -> convertToCurrentResolutionPosition() function for more details
'''

'''
---------------------------------------------------1920x1080---------------------------------------------------
'''
menuDoubleClick = 935, 175

doubleArrowTop = 110, 200
oneArrowDown = 107, 906

clickChestInMiddleOfScreen = 969, 557

#Metaldetector 
maxAmountOfChestInMetalDetector = 200
metalDetector = 263, 780
clickNormalChest = 674, 633

#Selling
sellButton = 622, 758
amountOfMineralSellPlaces = 2

#Gem station 
amountOfGemSlots = 50

redGem = 726, 610
blueGem = 959, 610
greenGem = 1202, 610
purpleGem = 726, 760
yellowGem = 959, 760

gemList = [redGem, blueGem, greenGem, purpleGem, yellowGem]

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

#runTime = time.process_time()

'''
---------------------------------------------------2560x1440---------------------------------------------------
'''

'''
-------------------------AUTOGUI-------------------------
'''
def doAutoEverythingBySequence():
    while True:
        collectChestsInMineImproved()
        craftGems(amountOfGemSlots)
        sellMinerals()
        collectNormalChestsFromMetalDetector()
        craftGems(amountOfGemSlots)
        sellMinerals()
         

def doFullscreen():
    pyautogui.moveTo(menuDoubleClick)
    time.sleep(defaultDelay)
    pyautogui.doubleClick()
    time.sleep(defaultDelay)

def collectChestsInMineImproved():
    counter = 0
    goToMrMineScreen()
    while counter < 100:
        keyboard.press_and_release('space')
        time.sleep(defaultDelay)
        for everyMiner in range(len(minerPosistionList)):
            time.sleep(defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(minerPosistionList[everyMiner], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(minerYpositionMiddleLevel, currentResolution[1], originalResolution[1]))
            clickMouse()
            clickChestInMiddleOfScreens()
        counter = counter + 1

def sellMinerals():
    #goto mr mine screen
    goToMrMineScreen()
    for everyTrader in range(amountOfMineralSellPlaces):
        time.sleep(defaultDelay)
        pressButton("s")
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(sellButton[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(sellButton[1], currentResolution[1], originalResolution[1]))
        time.sleep(defaultDelay + 0.01)
        clickMouse()
    clickMouse()

def goToFloorZero():
    #DONE
    goToMrMineScreen()
    pressButton('k')
    time.sleep(defaultDelay)
    pressButton('esc')
    time.sleep(defaultDelay)
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(doubleArrowTop[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(doubleArrowTop[1], currentResolution[1], originalResolution[1]))
    time.sleep(defaultDelay)
    clickMouse()

def goToMrMineScreen():
    #DONE
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(doubleArrowTop[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(doubleArrowTop[1], currentResolution[1], originalResolution[1]))
    clickMouse()

def collectNormalChestsFromMetalDetector():
    #DONE
    goToFloorZero()
    counter = 0
    while counter < 200:
        time.sleep(defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(metalDetector[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(metalDetector[1], currentResolution[1], originalResolution[1]))
        clickMouse()
        time.sleep(defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(clickNormalChest[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(clickNormalChest[1], currentResolution[1], originalResolution[1]))
        clickMouse()
        clickChestInMiddleOfScreens()
        counter = counter + 1

def craftGems(amountOfGemSlots):
    goToMrMineScreen()
    pressButton('g')
    for i in range(len(gemList), 0, -1):
        time.sleep(defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(gemList[i - 1][0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(gemList[i - 1][1], currentResolution[0], originalResolution[0])) #LEGALHACK
        for x in range(amountOfGemSlots):
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

def convertValuesFromNewScreenToOld(x, y):
    print(MrMineMath.convertToCurrentResolutionPosition(x, 1920, 2560), end=" ")
    print(MrMineMath.convertToCurrentResolutionPosition(y, 1920, 2560))

'''
-------------------------GENERAL HELPERS-------------------------
'''

def clickMouse():
    pyautogui.click()
    time.sleep(defaultDelay)

def pressButton(button):
    #button is a string
    #example: button = "s"
    pyautogui.press(button)
    time.sleep(defaultDelay)

def clickChestInMiddleOfScreens():
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(clickChestInMiddleOfScreen[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(clickChestInMiddleOfScreen[1], currentResolution[1], originalResolution[1]))
        time.sleep(defaultDelay)
        clickMouse()
        clickMouse()

'''
-------------------------MAIN PROGRAM-------------------------
'''

collectChestsInMineImproved()
#doAutoEverythingBySequence()