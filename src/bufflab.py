import pyautogui
from generalFunctions import goToMrMineScreen
import mouseAndKeyboard
import MrMineMath
import random
import positionsAndResolution

positions = positionsAndResolution.positions

maxTierElementalPike = 800, 483
maxTierDrillSpeed = 623, 404

clickBuffButton = 1117, 741

def buffLab():
    goToMrMineScreen()
    mouseAndKeyboard.pressButton('b')
    randomNumber = random.randrange(0, 101)
    if randomNumber > 70:
        print("Consuming elemental pike buff.")
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(maxTierElementalPike[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(maxTierElementalPike[1], positions.currentResolution[1], positions.originalResolution[1]))
        mouseAndKeyboard.clickMouse()
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(clickBuffButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(clickBuffButton[1], positions.currentResolution[1], positions.originalResolution[1]))
        mouseAndKeyboard.clickMouse()
    elif randomNumber > 40:
        print("Consuming drill speed buff.")
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(maxTierDrillSpeed[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(maxTierDrillSpeed[1], positions.currentResolution[1], positions.originalResolution[1]))
        mouseAndKeyboard.clickMouse()
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(clickBuffButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(clickBuffButton[1], positions.currentResolution[1], positions.originalResolution[1]))
        mouseAndKeyboard.clickMouse()
    else:
        print("Not clicking any buff.")
