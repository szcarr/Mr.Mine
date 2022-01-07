import time
import pyautogui
import keyboard

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution

positions = positionsAndResolution.positions

#Selling
sellButton = 622, 758
amountOfMineralSellPlaces = 2

def sellMinerals():
    #goto mr mine screen
    print("Selling minerals...")
    generalFunctions.goToMrMineScreen()
    for everyTrader in range(amountOfMineralSellPlaces):
        time.sleep(positions.defaultDelay)
        mouseAndKeyboard.pressButton("s")
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(sellButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(sellButton[1], positions.currentResolution[1], positions.originalResolution[1]))
        time.sleep(positions.defaultDelay)
        mouseAndKeyboard.clickMouse()
    mouseAndKeyboard.clickMouse()
    time.sleep(positions.defaultDelay)
    mouseAndKeyboard.pressButton('esc')