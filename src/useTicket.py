import time
import pyautogui

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution

positions = positionsAndResolution.positions

def useTickets():
    '''
    Function to consume mr mine tickets before wasting them on scientists, since re rolling and forfeiting reward has yes button on the same pixel position.
    '''
    print("Going to ticket store")
    generalFunctions.goToFloorZero()
    time.sleep(positions.defaultDelay)

    firstRun = True
    dynamicString = ""
    for i in range(10):
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.minerPosistionList[7], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.minerYpositionMiddleLevel, positions.currentResolution[1], positions.originalResolution[1]))
        time.sleep(positions.defaultDelay)
        mouseAndKeyboard.clickMouse()
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.minerPosistionList[4], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.scientistCancelTicketPurchase[1] - MrMineMath.convertToCurrentResolutionPosition(80, positions.currentResolution[1], positions.originalResolution[1]), positions.currentResolution[1], positions.originalResolution[1]))
        time.sleep(positions.defaultDelay)
        mouseAndKeyboard.clickMouse()

        #Clicking gold chest
        if firstRun:
            firstRun = False
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.scientistHardDifficulty[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.scientistHardDifficulty[1] - MrMineMath.convertToCurrentResolutionPosition(80, positions.currentResolution[1], positions.originalResolution[1]), positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            dynamicString = "golden chest"
        else:
            #Openenig normal chests
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.scientistHardDifficulty[0] - MrMineMath.convertToCurrentResolutionPosition(360, positions.currentResolution[0], positions.originalResolution[0]), positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.scientistHardDifficulty[1] - MrMineMath.convertToCurrentResolutionPosition(80, positions.currentResolution[1], positions.originalResolution[1]), positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            dynamicString = "normal chest"
        print("Opening " + dynamicString + " with tickets...")
        mouseAndKeyboard.clickMouse()
        generalFunctions.clickChestInMiddleOfScreen()
    mouseAndKeyboard.pressButton('esc')