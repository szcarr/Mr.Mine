import time
import pyautogui
import keyboard

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution

positions = positionsAndResolution.positions

def collectChestsInMineImproved():
    counter = 0
    generalFunctions.goToMrMineScreen()
    maxCount = positions.amountOfChestsToBeClicked * 2
    while counter < maxCount:
        keyboard.press_and_release('space')
        time.sleep(positions.defaultDelay)
        for everyMiner in range(len(positions.minerPosistionList)):
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.minerPosistionList[everyMiner], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.minerYpositionMiddleLevel, positions.currentResolution[1], positions.originalResolution[1]))
            mouseAndKeyboard.clickMouse()
            generalFunctions.clickChestInMiddleOfScreen()
        print("Collecting chests from mine: " + str(counter + 1) + "/" + str(maxCount))
        counter = counter + 1