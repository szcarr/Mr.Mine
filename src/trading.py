import pyautogui
import random
import time

import mouseAndKeyboard
import fileHandling as fh
import positionsAndResolution
import generalFunctions
import MrMineMath

positions = positionsAndResolution.positions

makeTradeUpperOption = 1206, 380

makeTradeLowerOption = 1206, 700

amountOfTraders = 2

forRange = 300

def trade():
    if fh.stringInFileExists(positions.userconfigFile, "tradingEnabled = True;"):
        print("Trading.")
        generalFunctions.goToMrMineScreen()
        mouseAndKeyboard.pressButton('esc')
        for i in range(amountOfTraders):
            mouseAndKeyboard.pressButton('t')
            if random.randint(0,100) > 50:
                print("Selecting upper trade.")
                for i in range(0, forRange, round(500/100 * 10)):
                    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(makeTradeUpperOption[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(makeTradeUpperOption[1] + i, positions.currentResolution[1], positions.originalResolution[1]))
                    time.sleep(0.03)
                    mouseAndKeyboard.clickMouse()
            else:
                print("Selecting lower trade.")
                for i in range(0, forRange, round(500/100 * 10)):
                    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(makeTradeLowerOption[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(makeTradeLowerOption[1] + i, positions.currentResolution[1], positions.originalResolution[1]))
                    time.sleep(0.03)
                    mouseAndKeyboard.clickMouse()
            
        mouseAndKeyboard.pressButton('esc')
    
#trade()