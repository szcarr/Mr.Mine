import pyautogui
import random

import mouseAndKeyboard
import MrMineMath
import positionsAndResolution
import generalFunctions
import fileHandling as fh

positions = positionsAndResolution.positions

maxTierElementalPike = 800, 483
maxTierDrillSpeed = 623, 404
maxTierMiningSpeed = 710, 320

lowestTierNuggetOfAttraction = 710, 413

listOfBuffs = [maxTierElementalPike, maxTierDrillSpeed, maxTierMiningSpeed]

listOfBuffImages = ["elementalpike", "drillspeed", "minerspeed"] #Must be of similar index as list of buffs

confidenceOfBuffs = {
    "drillspeed": 0.8,
    "elementalpike": 0.8,
    "minerspeed": 0.8
}

clickUseButton = 1117, 741

def buffLabMain():
    buffLabSmartSelect()

def buffLabSmartSelect():
    generalFunctions.goToMrMineScreen()
    generalFunctions.goToSafeClickArea()
    allBuffsActive = True
    for i in range(len(listOfBuffImages)):
        imageString = listOfBuffImages[i]
        print("Checking if buff " + imageString + " is active.")
        image = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\bufflab\\" + imageString + ".png", confidence = confidenceOfBuffs.get(listOfBuffImages[i]))
        if image:
            print("Buff: " + imageString + " is active.")
        else: #Did not find active buff
            allBuffsActive = False
            clickOneBuff(listOfBuffs[i])
    if allBuffsActive:
        buffLabRandomSelect()

def buffLabRandomSelect():
    generalFunctions.goToMrMineScreen()
    mouseAndKeyboard.pressButton('b')
    randomNumber = random.randrange(0, len(listOfBuffs) - 1)
    whatBuff = "ERROR"
    if randomNumber == 0:
        whatBuff = "elemental pike"
    elif randomNumber == 1:
        whatBuff = "drill speed"
    elif randomNumber == 2:
        whatBuff = "mining speed"
    textString = "Consuming " + whatBuff + " buff."
    print(textString)
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(listOfBuffs[randomNumber][0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(listOfBuffs[randomNumber][1], positions.currentResolution[1], positions.originalResolution[1]))
    mouseAndKeyboard.clickMouse()
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(clickUseButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(clickUseButton[1], positions.currentResolution[1], positions.originalResolution[1]))
    mouseAndKeyboard.clickMouse()

def clickOneBuff(xAndYTuple):
    generalFunctions.goToMrMineScreen()
    mouseAndKeyboard.pressButton('b')
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(xAndYTuple[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(xAndYTuple[1], positions.currentResolution[1], positions.originalResolution[1]))
    mouseAndKeyboard.clickMouse()
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(clickUseButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(clickUseButton[1], positions.currentResolution[1], positions.originalResolution[1]))
    mouseAndKeyboard.clickMouse()

#buffLabSmartSelect()