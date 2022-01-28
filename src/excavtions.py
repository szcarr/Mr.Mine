import time
import pyautogui
import keyboard

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution
import useTicket
import fileHandling
import mineFloors

positions = positionsAndResolution.positions
fh = fileHandling

pathToCurrentDir = fh.getPathToCurrentDir()
splitBy = fh.detectOS()

#Scientists
scientistCollectButton = 963, 732
scientistForfeitReward = 963, 771
scientistTabOne = 570, 248
scientistTabTwo = 761, 248
scientistTabThree = 942, 248
scientistEasyDifficulty = 719, 722 #Need to convert
scientistHardDifficulty = 1199, 722
scientistRelicInvetoryFullOkButton = 968, 172
scientistForfeitRewardYesButton = 969, 200
scientistCancelTicketPurchase = 970, 229
scientistsList = [scientistTabOne, scientistTabTwo, scientistTabThree]

itemsToLookFor = ["book_of_secrets", "book_of_success", "book_of_time"]

confidenceOfItems = {
    "book_of_secrets": 0.7,
    "book_of_success": 0.7,
    "book_of_time": 0.7,
}

#-----------------1920x1080
rightChoiceValues = (957, 271, 459, 544)
leftChoiceValues = (489, 271, 459, 544)

rightChoiceRegion = (round(MrMineMath.convertToCurrentResolutionPosition(rightChoiceValues[0], positions.currentResolution[0], positions.originalResolution[0])), round(MrMineMath.convertToCurrentResolutionPosition(rightChoiceValues[1], positions.currentResolution[1], positions.originalResolution[1])), round(MrMineMath.convertToCurrentResolutionPosition(rightChoiceValues[2], positions.currentResolution[0], positions.originalResolution[0])), round(MrMineMath.convertToCurrentResolutionPosition(rightChoiceValues[3], positions.currentResolution[1], positions.originalResolution[1])))
leftChoiceRegion = (round(MrMineMath.convertToCurrentResolutionPosition(leftChoiceValues[0], positions.currentResolution[0], positions.originalResolution[0])), round(MrMineMath.convertToCurrentResolutionPosition(leftChoiceValues[1], positions.currentResolution[1], positions.originalResolution[1])), round(MrMineMath.convertToCurrentResolutionPosition(leftChoiceValues[2], positions.currentResolution[0], positions.originalResolution[0])), round(MrMineMath.convertToCurrentResolutionPosition(leftChoiceValues[3], positions.currentResolution[1], positions.originalResolution[1])))

#print(leftChoiceRegion)
choiceListRegion = [rightChoiceRegion, leftChoiceRegion]

#foundImage = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\excavations\\" + "book_of_secrets" + ".png", confidence = confidenceOfItems.get("book_of_secrets"), region = rightChoiceRegion)#region = rightChoiceRegion
#print(foundImage)

def excavationsMain():
    smarterScientists()

def smarterScientists():
    #NOT DONE
    mouseAndKeyboard.pressButton('esc')
    useTicket.useTickets()
    generalFunctions.goToMrMineScreen()
    time.sleep(positions.defaultDelay)
    generalFunctions.goToSafeClickArea() #GOINNG TO SAFE SCREEN FIRST
    time.sleep(positions.defaultDelay)
    keyboard.press_and_release('shift+s')
    time.sleep(positions.defaultDelay)
    textString = "Collecting rewards from scientists "

    gamestageFile = pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt"

    file = fh.readTXTFile(gamestageFile)

    fileOutput = []

    for line in file:
        fileOutput = line.split("\n")

    hardExcavations = False

    for outputString in fileOutput:
        if outputString == "chooseHardDifficulty = True;":
            hardExcavations = True

    for y in range(len(scientistsList)):
        hardExcavations = False
        print("Setting up scientist: " + str(y + 1))
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistsList[y][0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistsList[y][1], positions.currentResolution[1], positions.originalResolution[1]))
        mouseAndKeyboard.clickMouse()
        for x in range(2):#amount of scientists
            #print(textString + str(x + 1) + "/" + str(len(scientistsList)) + "...")

            # IMAGE RECOGNITION HERE
            canBreak = False
            for r in range(len(choiceListRegion)):
                if canBreak:
                    break
                regionChoice = choiceListRegion[r]
                imageConfidence = 0.8
                for i in range(len(itemsToLookFor)):
                    if canBreak:
                        break
                    image = itemsToLookFor[i]
                    if r < 1:
                        whatRegionWasFound = "right"
                    else:
                        whatRegionWasFound = "left"
                    print("Looking for " + image + " in " + whatRegionWasFound)
                    foundImage = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\excavations\\" + image + ".png", confidence = confidenceOfItems.get(image), region = regionChoice) #region = (leftChoiceRegion[0], leftChoiceRegion[1], leftChoiceRegion[2], leftChoiceRegion[3])
                    if foundImage:
                        whatRegionWasFound = ""
                        canBreak = True
                        if r < 1:
                            whatRegionWasFound = "right"
                            hardExcavations = True
                        else:
                            whatRegionWasFound = "left"
                            hardExcavations = False
                        print("Found " + image + " in " +  whatRegionWasFound + " region.")
                    else:
                        print("Did not find " + image + " in " + whatRegionWasFound + " region. For scientist " + str(y + 1) + ".")

            if hardExcavations:
                pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistHardDifficulty[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistHardDifficulty[1], positions.currentResolution[1], positions.originalResolution[1]))
                time.sleep(positions.defaultDelay)
                mouseAndKeyboard.clickMouse()
                time.sleep(positions.defaultDelay)
            else:
                pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistEasyDifficulty[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistEasyDifficulty[1], positions.currentResolution[1], positions.originalResolution[1]))
                time.sleep(positions.defaultDelay)
                mouseAndKeyboard.clickMouse()
                time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistCollectButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistCollectButton[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistRelicInvetoryFullOkButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistRelicInvetoryFullOkButton[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            time.sleep(positions.defaultDelay)
            generalFunctions.clickChestInMiddleOfScreen()
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistForfeitReward[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistForfeitReward[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistForfeitRewardYesButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistForfeitRewardYesButton[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            #next is forfeiting
    time.sleep(positions.defaultDelay)
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistCancelTicketPurchase[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistCancelTicketPurchase[1], positions.currentResolution[1], positions.originalResolution[1]))
    time.sleep(positions.defaultDelay)
    mouseAndKeyboard.clickMouse()
    time.sleep(positions.defaultDelay)
    mouseAndKeyboard.pressButton('esc')
    mineFloors.checkIfRainShower()

def scientists():
    #WORKS BUT OLDER VERSION
    mouseAndKeyboard.pressButton('esc')
    useTicket.useTickets()
    generalFunctions.goToMrMineScreen()
    time.sleep(positions.defaultDelay)
    generalFunctions.goToSafeClickArea() #GOINNG TO SAFE SCREEN FIRST
    time.sleep(positions.defaultDelay)
    keyboard.press_and_release('shift+s')
    time.sleep(positions.defaultDelay)
    textString = "Collecting rewards from scientists "

    gamestageFile = pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt"

    file = fh.readTXTFile(gamestageFile)

    fileOutput = []

    for line in file:
        fileOutput = line.split("\n")

    hardExcavations = False

    for outputString in fileOutput:
        if outputString == "chooseHardDifficulty = True;":
            hardExcavations = True

    for i in range(2):
        if i > 0:
            textString = "Queueing new tasks for scientists "
        for x in range(len(scientistsList)):#amount of scientists
            print(textString + str(x + 1) + "/" + str(len(scientistsList)) + "...")
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistsList[x][0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistsList[x][1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            time.sleep(positions.defaultDelay)
            if hardExcavations:
                pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistHardDifficulty[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistHardDifficulty[1], positions.currentResolution[1], positions.originalResolution[1]))
                time.sleep(4)
                mouseAndKeyboard.clickMouse()
                time.sleep(positions.defaultDelay)
            else:
                pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistEasyDifficulty[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistEasyDifficulty[1], positions.currentResolution[1], positions.originalResolution[1]))
                time.sleep(4)
                mouseAndKeyboard.clickMouse()
                time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistCollectButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistCollectButton[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistRelicInvetoryFullOkButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistRelicInvetoryFullOkButton[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            time.sleep(positions.defaultDelay)
            generalFunctions.clickChestInMiddleOfScreen()
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistForfeitReward[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistForfeitReward[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistForfeitRewardYesButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistForfeitRewardYesButton[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            #next is forfeiting
    time.sleep(positions.defaultDelay)
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistCancelTicketPurchase[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistCancelTicketPurchase[1], positions.currentResolution[1], positions.originalResolution[1]))
    time.sleep(positions.defaultDelay)
    mouseAndKeyboard.clickMouse()
    time.sleep(positions.defaultDelay)
    mouseAndKeyboard.pressButton('esc')
    mineFloors.checkIfRainShower()

#smarterScientists()