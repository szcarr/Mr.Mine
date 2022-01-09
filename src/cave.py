import time
import pyautogui
from MrMineFunctions import clickMouse

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution
import fileHandling
import re

positions = positionsAndResolution.positions
fh = fileHandling

def collectCaveItems(amountOfChestsToBeClicked):
    generalFunctions.goToMrMineScreen()
    mouseAndKeyboard.pressButton('k')
    time.sleep(positions.defaultDelay)
    maxCount = round(amountOfChestsToBeClicked * 0.20)
    if maxCount < 1:
        maxCount = 1
    for i in range(maxCount):
        print("Collecting rewards from caves: " + str(i + 1) + "/" + str(maxCount))
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.minerPosistionList[3] + MrMineMath.convertToCurrentResolutionPosition(15, positions.currentResolution[0], positions.originalResolution[0]), positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.minerYpositionMiddleLevel + MrMineMath.convertToCurrentResolutionPosition(230, positions.currentResolution[1], positions.originalResolution[1]), positions.currentResolution[1], positions.originalResolution[1]))
        time.sleep(positions.defaultDelay)
        mouseAndKeyboard.clickMouse()
        generalFunctions.clickChestInMiddleOfScreen()

def doCaves():
    generalFunctions.goToMrMineScreen()
    mouseAndKeyboard.pressButton('k')

    clickToGoToCavePosition = pyautogui.locateAllOnScreen(str(fh.getPathToCurrentDir()) + "images\\cave\\caveUI.png", confidence = 0.5)
    
    centerList = []
    splitList = []

    for pos in clickToGoToCavePosition:
        centerList.append(pyautogui.center(pos))

    splitChars = r'\)' + "|,| |="
    for i in range(len(centerList)):
        splitList.append(re.split(splitChars, str(centerList[i])))

    amountOfCaves = []
    growthFactorDeviation = 0.05
    print(splitList)
    for i in range(len(splitList)):
        xvalue = int(splitList[i][1])
        yvalue = int(splitList[i][4]) #Getting y value
        coordinateList = []
        coordinateList.append(xvalue)
        coordinateList.append(yvalue)
        if len(amountOfCaves) == 0: # if list is empty
            amountOfCaves.append(coordinateList)
        print(amountOfCaves)
        for y in range(len(amountOfCaves)):
            largerThan = (int(amountOfCaves[y][0]) * (1 + growthFactorDeviation))
            lessThan = (int(amountOfCaves[y][1]) * (1 - growthFactorDeviation))
            print(largerThan, yvalue)
            print(lessThan, yvalue)
            if largerThan < yvalue or lessThan > yvalue:
                amountOfCaves.append(coordinateList)

    middleRowBottomLeftXValue = int(MrMineMath.convertToCurrentResolutionPosition(positions.middleRowBottomLeft[0], positions.currentResolution[0], positions.originalResolution[0]))
    middleRowBottomLeftYValue = int(MrMineMath.convertToCurrentResolutionPosition(positions.middleRowBottomLeft[1], positions.currentResolution[0], positions.originalResolution[0]))

    middleRowTopRightXValue = int(MrMineMath.convertToCurrentResolutionPosition(positions.middleRowTopRight[0], positions.currentResolution[1], positions.originalResolution[1]))
    middleRowTopRightYValue = int(MrMineMath.convertToCurrentResolutionPosition(positions.middleRowTopRight[1], positions.currentResolution[1], positions.originalResolution[1]))

    print(len(amountOfCaves))
    for i in range(len(amountOfCaves)):
        pyautogui.moveTo(amountOfCaves[i][0], amountOfCaves[i][1])
        mouseAndKeyboard.clickMouse()

        #time.sleep(1)
        #pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\cave\\bluecaveentrance.png", confidence = 0.8)
        #all cave colors
        redCaveCenter = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\cave\\redcaveentrance.png", confidence = 0.8, region=(middleRowBottomLeftXValue, middleRowBottomLeftYValue, middleRowTopRightXValue, middleRowTopRightYValue))            
        blueCaveCenter = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\cave\\bluecaveentrance.png", confidence = 0.8, region=(middleRowBottomLeftXValue, middleRowBottomLeftYValue, middleRowTopRightXValue, middleRowTopRightYValue))

        caveList = [redCaveCenter, blueCaveCenter]
        correctXYToMoveTo = None

        for i in range(len(caveList)):
            if caveList[i] != None:
                correctXYToMoveTo = caveList[i]


        xyToMoveTo = pyautogui.center(correctXYToMoveTo)
        pyautogui.moveTo(xyToMoveTo)
        clickMouse()
        clickMouse()    
        for i in range(2):
            pyautogui.scroll(-1000)

        #Next is scan for nodes

#doCaves()