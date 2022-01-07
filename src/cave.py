import time
import pyautogui

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution

positions = positionsAndResolution.positions

def collectCaveItems(amountOfChestsToBeClicked):
    generalFunctions.goToMrMineScreen()
    mouseAndKeyboard.pressButton('k')
    time.sleep(positions.defaultDelay)
    maxCount = round(amountOfChestsToBeClicked * 0.60)
    if maxCount < 1:
        maxCount = 1
    for i in range(maxCount):
        print("Collecting rewards from caves: " + str(i + 1) + "/" + str(maxCount))
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.minerPosistionList[3] + MrMineMath.convertToCurrentResolutionPosition(15, positions.currentResolution[0], positions.originalResolution[0]), positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.minerYpositionMiddleLevel + MrMineMath.convertToCurrentResolutionPosition(230, positions.currentResolution[1], positions.originalResolution[1]), positions.currentResolution[1], positions.originalResolution[1]))
        time.sleep(positions.defaultDelay)
        mouseAndKeyboard.clickMouse()
        generalFunctions.clickChestInMiddleOfScreen()