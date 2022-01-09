import time
import pyautogui
import keyboard
from MrMineFunctions import clickChestInMiddleOfScreens, clickMouse

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution
import fileHandling

pyautogui.FAILSAFE = True

positions = positionsAndResolution.positions
fh = fileHandling

middleRowBottomLeftXValue = int(MrMineMath.convertToCurrentResolutionPosition(positions.middleRowBottomLeft[0], positions.currentResolution[0], positions.originalResolution[0]))
middleRowBottomLeftYValue = int(MrMineMath.convertToCurrentResolutionPosition(positions.middleRowBottomLeft[1], positions.currentResolution[0], positions.originalResolution[0]))

middleRowTopRightXValue = int(MrMineMath.convertToCurrentResolutionPosition(positions.middleRowTopRight[0], positions.currentResolution[1], positions.originalResolution[1]))
middleRowTopRightYValue = int(MrMineMath.convertToCurrentResolutionPosition(positions.middleRowTopRight[1], positions.currentResolution[1], positions.originalResolution[1]))

lowerThreeLeftXValue = int(MrMineMath.convertToCurrentResolutionPosition(positions.lowerThreeRowsBottomLeft[0], positions.currentResolution[0], positions.originalResolution[0]))
lowerThreeLeftYValue = int(MrMineMath.convertToCurrentResolutionPosition(positions.lowerThreeRowsBottomLeft[1], positions.currentResolution[0], positions.originalResolution[0]))

lowerThreeTopRightXValue = int(MrMineMath.convertToCurrentResolutionPosition(positions.lowerThreeRowsTopRight[0], positions.currentResolution[1], positions.originalResolution[1]))
lowerThreeLeftXValue = int(MrMineMath.convertToCurrentResolutionPosition(positions.lowerThreeRowsTopRight[1], positions.currentResolution[1], positions.originalResolution[1]))


def checkIfMonster():
    print("Checking for monsters...")
    monsterConfidence = 1
    monsterPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\monster.png", confidence = monsterConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))
    smallermonsterPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\smallermonster.png", confidence = monsterConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))
    earthmonsterPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\monsterearth.png", confidence = monsterConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))
    monstermoonPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\monstermoon.png", confidence = monsterConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))    
    
    monsterList = [monsterPosition, smallermonsterPosition, earthmonsterPosition, monstermoonPosition]
    foundMonster = False
    for m in range(len(monsterList)):
        pyautogui.failSafeCheck()
        #print(monsterList[m])
        if monsterList[m] != None:
            foundMonster = True
            print("Found a monster!")
            #Clicking on red exclamation mark
            monsterPosition = pyautogui.center(monsterList[m])
            pyautogui.moveTo(monsterPosition[0], monsterPosition[1] + 20)
            clickMouse()

            #Battlescreen
            for i in range(20):
                for x in range(len(positions.allRows)):
                    for y in range(len(positions.allRows[x])):
                        pyautogui.failSafeCheck()
                        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.allRows[x][y][0], positions.currentResolution[1], positions.originalResolution[1]), MrMineMath.convertToCurrentResolutionPosition(positions.allRows[x][y][1], positions.currentResolution[1], positions.originalResolution[1]))
                        clickMouse()
            break
    if not foundMonster:
        print("Did not find any monsters.")


def checkIfOre():
    print("Checking for ores...")
    oreConfidence = 0.7

    siliconPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\siliconore.png", confidence = oreConfidence)
    magnesiumPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\magnesiumore.png", confidence = oreConfidence)
    titaniumPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\titaniumore.png", confidence = oreConfidence)
    fishPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\fishore.png", confidence = oreConfidence)

    oreList = [siliconPosition, magnesiumPosition, titaniumPosition, fishPosition]
    foundOre = False
    for i in range(len(oreList)):
        pyautogui.failSafeCheck()
        if oreList[i] != None:
            foundOre = True
            print("Found ore!")
            #Clicking on red exclamation mark
            orePosition = pyautogui.center(oreList[i])
            pyautogui.moveTo(orePosition)
            for i in range(8):
                clickMouse()
    if not foundOre:
        print("Did not find any ores.")

def collectChestsInMineImproved():
    #Main
    print("Checking for chests...")
    counter = 0
    generalFunctions.goToMrMineScreen()
    generalFunctions.goToSafeClickArea()
    maxCount = positions.amountOfChestsToBeClicked * 5
    nothingToDoInARow = 0
    amountOfTriesBeforeSkip = 3
    foundChest = False
    while counter < maxCount:
        if nothingToDoInARow > amountOfTriesBeforeSkip:
            print("Nothing to do so skipping.")
            break
        pyautogui.failSafeCheck()
        keyboard.press_and_release('space')
        time.sleep(positions.defaultDelay)
        checkIfOre()
        checkIfMonster()
        chestConfidence = 0.6 #0.6 works really good

        minerWithChestEarth = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\minerwithchestearth.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            

        chest1Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\chest1.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            
        chest2Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\chest2.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            
        chest3Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\chest3.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            
        chest4Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\chest4.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            

        goldchest1Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\goldchest1.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            
        goldchest2Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\goldchest2.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            
        goldchest3Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\goldchest3.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            
        goldchest4Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\goldchest4.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            

        #chestleftside1 = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\chestleftside1.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            
        #chestleftside2 = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\chestleftside2.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            

        chestbackgroundcolor = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\smallchestbackgroundcolor.png", confidence = chestConfidence - 0.1, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            

        #print(minerWithChestEarth)
        chestList = [chest1Position, chest2Position, chest3Position, chest4Position, goldchest1Position, goldchest2Position, goldchest3Position, goldchest4Position,
        minerWithChestEarth] #chestleftside1, chestleftside2]
        correctXYToMoveTo = None
        for i in range(len(chestList)):
            if chestList[i] != None:
                correctXYToMoveTo = chestList[i]

        if correctXYToMoveTo != None:
            foundChest = True
            nothingToDoInARow = 0 # Resets if found a chest
            chestPosition = pyautogui.center(correctXYToMoveTo)
            pyautogui.moveTo(chestPosition[0], correctXYToMoveTo[1] + 50)
            clickMouse()
            clickChestInMiddleOfScreens()
        else:
            nothingToDoInARow = nothingToDoInARow + 1 #Did not find a a chest
            if chestbackgroundcolor != None:
                print("Did not find chest on screen, but detected yellow background.")
                iterateOverAllMinersMiddleFloor()
        print("Collecting chests from mine: " + str(counter + 1) + "/" + str(maxCount))
        print("Nothing to do count: " + str(nothingToDoInARow - 1) + "/" + str(amountOfTriesBeforeSkip))
        counter = counter + 1
    if not foundChest:
        print("Did not find any chests.")

def collectChestsInMineOldVersion():
    counter = 0
    generalFunctions.goToMrMineScreen()
    generalFunctions.goToSafeClickArea()
    maxCount = positions.amountOfChestsToBeClicked * 2
    while counter < maxCount:
        keyboard.press_and_release('space')
        time.sleep(positions.defaultDelay)
        iterateOverAllMinersMiddleFloor()
        print("Collecting chests from mine: " + str(counter + 1) + "/" + str(maxCount))
        counter = counter + 1

def iterateOverAllMinersMiddleFloor():
    for everyMiner in range(len(positions.minerPosistionList)):
        time.sleep(positions.defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.minerPosistionList[everyMiner], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.minerYpositionMiddleLevel, positions.currentResolution[1], positions.originalResolution[1]))
        mouseAndKeyboard.clickMouse()
        generalFunctions.clickChestInMiddleOfScreen()