import pyautogui
import keyboard
import time

import MrMineMath

pyautogui.FAILSAFE = True
defaultDelay = 0.00000000000000001 #For testing use 1.5 seconds else 0.00000000000000001

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

'''
---------------------------------------------------MINER-INFO---------------------------------------------------
'''

'''
    Mr mine needs to be in "fullscreen" then you can get the coords for

    These values are gotten at 1920x1080 screen
    New values need to be converted from your main screen to 1920x1080 screen
    ## IF you have 1920x1080 main screen
    ## THEN you can use those values without converting them
    See MrMineMath.py -> convertToCurrentResolutionPosition() function for more details
'''

'''
---------------------------------------------------1920x1080---------------------------------------------------
'''

#General
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
amountOfGemsToCraft = 5

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

#Chests
amountOfChestsToBeClicked = 5

#Scientists
scientistCollectButton = 963, 732
scientistForfeitReward = 963, 771
scientistTabOne = 570, 248
scientistTabTwo = 761, 248
scientistTabThree = 942, 248
scientistHardDifficulty = 1199, 722
scientistRelicInvetoryFullOkButton = 968, 172
scientistForfeitRewardYesButton = 969, 200
scientistCancelTicketPurchase = 970, 229
scientistsList = [scientistTabOne, scientistTabTwo, scientistTabThree]

#runTime = time.process_time()


'''
---------------------------------------------------2560x1440---------------------------------------------------
'''

'''
-------------------------AUTOGUI-------------------------
'''
def doAutoEverythingBySequence():
    #Main
    while True:
        collectChestsInMineImproved()
        craftGems(amountOfGemsToCraft)
        scientists()
        sellMinerals()
        collectNormalChestsFromMetalDetector()
        craftGems(amountOfGemsToCraft)
        scientists()
        collectCaveItems()
        sellMinerals() #Do things before selling

def buffLab():
    pressButton('b')

def collectCaveItems():
    goToMrMineScreen()
    pressButton('k')
    time.sleep(defaultDelay)
    maxCount = round(amountOfChestsToBeClicked * 0.60)
    if maxCount < 1:
        maxCount = 1
    for i in range(maxCount):
        print("Collecting rewards from caves: " + str(i + 1) + "/" + str(maxCount))
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(minerPosistionList[3] + MrMineMath.convertToCurrentResolutionPosition(15, currentResolution[0], originalResolution[0]), currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(minerYpositionMiddleLevel + MrMineMath.convertToCurrentResolutionPosition(314, currentResolution[1], originalResolution[1]), currentResolution[1], originalResolution[1]))
        time.sleep(defaultDelay)
        clickMouse()
        clickChestInMiddleOfScreens()

def collectChestsInMineImproved():
    counter = 0
    goToMrMineScreen()
    maxCount = amountOfChestsToBeClicked * 2
    while counter < maxCount:
        keyboard.press_and_release('space')
        time.sleep(defaultDelay)
        for everyMiner in range(len(minerPosistionList)):
            time.sleep(defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(minerPosistionList[everyMiner], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(minerYpositionMiddleLevel, currentResolution[1], originalResolution[1]))
            clickMouse()
            clickChestInMiddleOfScreens()
        print("Collecting chests from mine: " + str(counter + 1) + "/" + str(maxCount))
        counter = counter + 1

def doFullscreen():
    print("Doing fullscreen")
    pyautogui.moveTo(menuDoubleClick)
    time.sleep(defaultDelay)
    pyautogui.doubleClick()
    time.sleep(defaultDelay)

def goToFloorZero():
    #DONE
    print("Going to floor zero")
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
    print("Going to Mr.Mine screen")
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(doubleArrowTop[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(doubleArrowTop[1], currentResolution[1], originalResolution[1]))
    clickMouse()


def sellMinerals():
    #goto mr mine screen
    print("Selling minerals...")
    goToMrMineScreen()
    for everyTrader in range(amountOfMineralSellPlaces):
        time.sleep(defaultDelay)
        pressButton("s")
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(sellButton[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(sellButton[1], currentResolution[1], originalResolution[1]))
        time.sleep(defaultDelay + 0.01)
        clickMouse()
    clickMouse()
    time.sleep(defaultDelay)
    pressButton('esc')

def collectNormalChestsFromMetalDetector():
    #DONE
    goToFloorZero()
    counter = 0
    maxCount = amountOfChestsToBeClicked
    while counter < amountOfChestsToBeClicked:
        time.sleep(defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(metalDetector[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(metalDetector[1], currentResolution[1], originalResolution[1]))
        clickMouse()
        time.sleep(defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(clickNormalChest[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(clickNormalChest[1], currentResolution[1], originalResolution[1]))
        clickMouse()
        clickChestInMiddleOfScreens()
        print("Collecting chests from Metal Detector: " + str(counter + 1) + "/" + str(maxCount))
        counter = counter + 1

def craftGems(amountOfGemSlots):
    goToMrMineScreen()
    pressButton('g')

    gemMode = {
        0: "Red gem",
        1: "Blue gem",
        2: "Green gem",
        3: "Purple gem",
        4: "Yellow gem"
    }

    for i in range(len(gemList), 0, -1):
        time.sleep(defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(gemList[i - 1][0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(gemList[i - 1][1], currentResolution[0], originalResolution[0])) #LEGALHACK
        for x in range(amountOfGemSlots):
            print("Crafting " + str(gemMode.get(i - 1)) + " " + str(x + 1) + "/" + str(amountOfGemSlots))
            clickMouse()

def scientists():
    #NOT DONE
    useTickets()
    goToMrMineScreen()
    time.sleep(defaultDelay)
    keyboard.press_and_release('k') #GOINNG TO SAFE SCREEN FIRST
    time.sleep(defaultDelay)
    keyboard.press_and_release('shift+s')
    time.sleep(defaultDelay)
    textString = "Collecting rewards from scientists "
    for i in range(2):
        if i > 0:
            textString = "Queueing new tasks for scientists "
        for x in range(len(scientistsList)):#amount of scientists
            print(textString + str(x + 1) + "/" + str(len(scientistsList)) + "...")
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistsList[x][0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistsList[x][1], currentResolution[1], originalResolution[1]))
            time.sleep(defaultDelay)
            clickMouse()
            time.sleep(defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistHardDifficulty[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistHardDifficulty[1], currentResolution[1], originalResolution[1]))
            time.sleep(defaultDelay)
            clickMouse()
            time.sleep(defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistCollectButton[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistCollectButton[1], currentResolution[1], originalResolution[1]))
            time.sleep(defaultDelay)
            clickMouse()
            time.sleep(defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistRelicInvetoryFullOkButton[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistRelicInvetoryFullOkButton[1], currentResolution[1], originalResolution[1]))
            time.sleep(defaultDelay)
            clickMouse()
            time.sleep(defaultDelay)
            clickChestInMiddleOfScreens()
            time.sleep(defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistForfeitReward[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistForfeitReward[1], currentResolution[1], originalResolution[1]))
            time.sleep(defaultDelay)
            clickMouse()
            time.sleep(defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistForfeitRewardYesButton[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistForfeitRewardYesButton[1], currentResolution[1], originalResolution[1]))
            time.sleep(defaultDelay)
            clickMouse()
            #next is forfeiting
    time.sleep(defaultDelay)
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistCancelTicketPurchase[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistCancelTicketPurchase[1], currentResolution[1], originalResolution[1]))
    time.sleep(defaultDelay)
    clickMouse()
    time.sleep(defaultDelay)
    pressButton('esc')

def useTickets():
    '''
    Function to consume mr mine tickets before wasting them on scientists, since re rolling and forfeiting reward has yes button on the same pixel position.
    '''
    print("Going to ticket store")
    goToFloorZero()
    time.sleep(defaultDelay)

    firstRun = True
    dynamicString = ""
    for i in range(10):
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(minerPosistionList[7], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(minerYpositionMiddleLevel, currentResolution[1], originalResolution[1]))
        time.sleep(defaultDelay)
        clickMouse()
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(minerPosistionList[4], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistCancelTicketPurchase[1] - MrMineMath.convertToCurrentResolutionPosition(80, currentResolution[1], originalResolution[1]), currentResolution[1], originalResolution[1]))
        time.sleep(defaultDelay)
        clickMouse()

        #Clicking gold chest
        if firstRun:
            firstRun = False
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistHardDifficulty[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistHardDifficulty[1] - MrMineMath.convertToCurrentResolutionPosition(80, currentResolution[1], originalResolution[1]), currentResolution[1], originalResolution[1]))
            time.sleep(defaultDelay)
            dynamicString = "golden chest"
        else:
            #Openenig normal chests
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistHardDifficulty[0] - MrMineMath.convertToCurrentResolutionPosition(360, currentResolution[0], originalResolution[0]), currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistHardDifficulty[1] - MrMineMath.convertToCurrentResolutionPosition(80, currentResolution[1], originalResolution[1]), currentResolution[1], originalResolution[1]))
            time.sleep(defaultDelay)
            dynamicString = "normal chest"
        print("Opening " + dynamicString + " with tickets...")
        clickMouse()
        clickChestInMiddleOfScreens()
    pressButton('esc')

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

def getMainMonitorSize():
    monitorRes = str(pyautogui.size())
    monitorRes = monitorRes.split(",")
    actualSize = [] 
    for i in range(len(monitorRes)):
        valueSplitted = str(monitorRes[i].split("=")[1])
        valueSplitted = valueSplitted.split(")")
        actualSize.append(int(valueSplitted[0])) #Dirty little 116 iq move

    #print for debug
    print("Using monitor size " + str(actualSize[0]) + "x" + str(actualSize[1]))

    return tuple(actualSize)

'''
-------------------------GENERAL HELPERS-------------------------
'''

def clickMouse():
    #print("Clicking mouse")
    pyautogui.click()
    time.sleep(defaultDelay)

def pressButton(button):
    #button is a string
    #example: button = "s"
    print("Pressing button " + button + "...")
    pyautogui.press(button)
    time.sleep(defaultDelay)

def clickChestInMiddleOfScreens():
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(clickChestInMiddleOfScreen[0], currentResolution[0], originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(clickChestInMiddleOfScreen[1], currentResolution[1], originalResolution[1]))
        time.sleep(defaultDelay)
        clickMouse()
        clickMouse()

'''
-------------------------INITIALIZERS-------------------------
'''

#currentResolution needs to be the resolution currently used by your monitor
currentResolution = getMainMonitorSize()

'''
-------------------------MAIN PROGRAM-------------------------
'''
#convertValuesFromNewScreenToOld(210, 898) # collect
#convertValuesFromNewScreenToOld(2046, 709) # forfeiting reward
#convertValuesFromNewScreenToOld(760, 330) # scientist 1
#convertValuesFromNewScreenToOld(1015, 330) # scientist 2
#convertValuesFromNewScreenToOld(1256, 330) # scienttist 3
#convertValuesFromNewScreenToOld(1293, 305) # hard difficulty
#useTickets()
#210, 898, 2046, 709