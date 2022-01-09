import pyautogui
import time

import MrMineMath
import mouseAndKeyboard
import positionsAndResolution

positions = positionsAndResolution.positions


def clickChestInMiddleOfScreen():
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.clickChestInMiddleOfScreen[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.clickChestInMiddleOfScreen[1], positions.currentResolution[1], positions.originalResolution[1]))
    time.sleep(positions.defaultDelay)
    mouseAndKeyboard.clickMouse()
    mouseAndKeyboard.clickMouse()
        
def doFullscreen():
    print("Doing fullscreen")
    pyautogui.moveTo(positions.menuDoubleClick)
    time.sleep(positions.defaultDelay)
    pyautogui.doubleClick()
    time.sleep(positions.defaultDelay)

def goToFloorZero():
    #DONE
    print("Going to floor zero")
    goToMrMineScreen()
    mouseAndKeyboard.pressButton('k')
    time.sleep(positions.defaultDelay)
    mouseAndKeyboard.pressButton('esc')
    time.sleep(positions.defaultDelay)
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.doubleArrowTop[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.doubleArrowTop[1], positions.currentResolution[1], positions.originalResolution[1]))
    time.sleep(positions.defaultDelay)
    mouseAndKeyboard.clickMouse()

def goToMrMineScreen():
    #DONE
    print("Going to Mr.Mine screen")
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.doubleArrowTop[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.doubleArrowTop[1], positions.currentResolution[1], positions.originalResolution[1]))
    mouseAndKeyboard.clickMouse()

def goToSafeClickArea():
    goToFloorZero()
    goDownXAmountOfFloors(4)

def goDownXAmountOfFloors(x):
        for i in range(x):
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.oneArrowDown[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.oneArrowDown[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()