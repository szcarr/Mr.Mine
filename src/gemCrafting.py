import time
import pyautogui

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution
import fileHandling

positions = positionsAndResolution.positions
fh = fileHandling

pathToCurrentDir = fh.getPathToCurrentDir()
splitBy = fh.detectOS()


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
    
    gamestageFile = pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt"

    file = fh.readTXTFile(gamestageFile)

    fileOutput = []

    for line in file:
        fileOutput = line.split("\n")

    incrementBy = 1
    startPoint = 0
    stopPoint = len(gemList)

    for outputString in fileOutput:
        if outputString == "startCraftingFromRedGems = True;":
            startPoint = 0
            incrementBy = 1
            stopPoint = len(gemList)
            fh.replaceLineInFile(gamestageFile, fh.getLineNumberFromFile(gamestageFile, "startCraftingFromRedGems = True;"), "startCraftingFromRedGems = False;")
        elif outputString == "startCraftingFromRedGems = False;":
            startPoint = len(gemList) - 1
            incrementBy = -1
            stopPoint = -1
            fh.replaceLineInFile(gamestageFile, fh.getLineNumberFromFile(gamestageFile, "startCraftingFromRedGems = False;"), "startCraftingFromRedGems = True;")

    for i in range(startPoint, stopPoint, incrementBy):
        time.sleep(positions.defaultDelay)
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(gemList[i][0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(gemList[i][1], positions.currentResolution[0], positions.originalResolution[0])) #LEGALHACK
        for x in range(amountOfGemSlots):
            print("Crafting " + str(gemMode.get(i)) + " " + str(x + 1) + "/" + str(amountOfGemSlots))
            mouseAndKeyboard.clickMouse()
