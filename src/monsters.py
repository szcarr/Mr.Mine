import pyautogui

import fileHandling
import MrMineMath
import positionsAndResolution
import mouseAndKeyboard

positions = positionsAndResolution.positions
fh = fileHandling

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
            mouseAndKeyboard.clickMouse()

            #Battlescreen
            fightMonster()
            break
    if not foundMonster:
        print("Did not find any monsters.")

def checkIfFightScreen():
    battle = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\monsterbattlescreen.png", confidence = 0.9)
    if battle != None:
        fightMonster()

def fightMonster():
    for i in range(20):
                for x in range(len(positions.allRows)):
                    for y in range(len(positions.allRows[x])):
                        pyautogui.failSafeCheck()
                        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.allRows[x][y][0], positions.currentResolution[1], positions.originalResolution[1]), MrMineMath.convertToCurrentResolutionPosition(positions.allRows[x][y][1], positions.currentResolution[1], positions.originalResolution[1]))
                        mouseAndKeyboard.clickMouse()