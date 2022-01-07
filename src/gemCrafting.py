import time
import pyautogui
import keyboard

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution

positions = positionsAndResolution.positions

#Gem station 
amountOfGemsToCraft = 5

redGem = 726, 610
blueGem = 959, 610
greenGem = 1202, 610
purpleGem = 726, 760
yellowGem = 959, 760

gemList = [redGem, blueGem, greenGem, purpleGem, yellowGem]

def craftGems(amountOfGemSlots):
    generalFunctions.goToMrMineScreen()
    mouseAndKeyboard.pressButton('g')

    gemMode = {
        0: "Red gem",
        1: "Blue gem",
        2: "Green gem",
        3: "Purple gem",
        4: "Yellow gem"
    }

    for i in range(len(gemList), 0, -1):
        time.sleep(positions.defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(gemList[i - 1][0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(gemList[i - 1][1], positions.currentResolution[0], positions.originalResolution[0])) #LEGALHACK
        for x in range(amountOfGemSlots):
            print("Crafting " + str(gemMode.get(i - 1)) + " " + str(x + 1) + "/" + str(amountOfGemSlots))
            mouseAndKeyboard.clickMouse()