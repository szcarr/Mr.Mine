import pyautogui
import keyboard
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

forRange = round(positions.currentResolution[1] / 100 * 30)

def trade():
    try:
        if fh.stringInFileExists(positions.userconfigFile, "tradingEnabled = True;"):
            print("Trading.")
            generalFunctions.goToMrMineScreen()
            mouseAndKeyboard.pressButton('esc')
            for i in range(amountOfTraders):
                mouseAndKeyboard.pressButton('t')
                keyboard.press('left shift')
                for i in range(0, forRange, round(500/100 * 8)):
                    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(makeTradeUpperOption[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(makeTradeUpperOption[1] + i, positions.currentResolution[1], positions.originalResolution[1]))
                    time.sleep(0.03)
                    mouseAndKeyboard.clickMouse()
                keyboard.release('left shift')
            mouseAndKeyboard.pressButton('esc')
    except Exception as e:
        print(e)
    finally:
        keyboard.release('left shift')