import time
import pyautogui

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution

positions = positionsAndResolution.positions

#Metaldetector 
maxAmountOfChestInMetalDetector = 200
metalDetector = 263, 780
clickNormalChest = 674, 636
clickGoldChest = 1250, 636
compressChest = 954, 774

def collectNormalChestsFromMetalDetector():
    #DONE
    generalFunctions.goToFloorZero()
    counter = 0
    maxCount = positions.amountOfChestsToBeClicked / 2
    if maxCount < 1:
        maxCount = 1
    while counter < maxCount:
        time.sleep(positions.defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(metalDetector[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(metalDetector[1], positions.currentResolution[1], positions.originalResolution[1]))
        mouseAndKeyboard.clickMouse()
        time.sleep(positions.defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(clickNormalChest[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(clickNormalChest[1], positions.currentResolution[1], positions.originalResolution[1]))
        mouseAndKeyboard.clickMouse()
        generalFunctions.clickChestInMiddleOfScreen()
        print("Collecting chests from Metal Detector: " + str(counter + 1) + "/" + str(maxCount))
        counter = counter + 1

def collectGoldChestsFromMetalDetector():
    #DONE
    generalFunctions.goToFloorZero()
    counter = 0
    maxCount = positions.amountOfChestsToBeClicked / 10
    if maxCount < 1:
        maxCount = 1
    while counter < maxCount:
        time.sleep(positions.defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(metalDetector[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(metalDetector[1], positions.currentResolution[1], positions.originalResolution[1]))
        mouseAndKeyboard.clickMouse()
        time.sleep(positions.defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(clickGoldChest[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(clickGoldChest[1], positions.currentResolution[1], positions.originalResolution[1]))
        mouseAndKeyboard.clickMouse()
        generalFunctions.clickChestInMiddleOfScreen()
        print("Collecting gold chests from Metal Detector: " + str(counter + 1) + "/" + str(maxCount))
        counter = counter + 1