from cmath import e
import time
import pyautogui
import keyboard
from MrMineFunctions import clickChestInMiddleOfScreens, clickMouse

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution
import fileHandling
import monsters
import bufflab

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

def miningMain():
    pass
    collectChestsInMineImproved()

def checkIfOre():
    print("Checking for ores...")
    oreConfidence = 0.85

    siliconPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\siliconore.png", confidence = oreConfidence - 0.01)
    magnesiumPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\magnesiumore.png", confidence = oreConfidence)
    titaniumPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\titaniumore.png", confidence = oreConfidence)
    fishPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\fishore.png", confidence = oreConfidence - 0.05)

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

    return foundOre

def collectChestsInMineImproved():
    #Main
    print("Checking for chests...")
    counter = 0
    generalFunctions.goToMrMineScreen()
    generalFunctions.goToSafeClickArea()
    maxCount = positions.amountOfChestsToBeClicked
    nothingToDoInARow = 0
    amountOfTriesBeforeSkip = 3

    yellowbackgroundConfidence = 0.85
    fh.replaceLineInFile(positions.userconfigFile, fh.getLineNumberFromFile(positions.gamestageFile, "skippedChestCollecting = True;"), "skippedChestCollecting = False;") #Resets it
    while counter < maxCount:
        if nothingToDoInARow > amountOfTriesBeforeSkip:
            fh.replaceLineInFile(positions.userconfigFile, fh.getLineNumberFromFile(positions.gamestageFile, "skippedChestCollecting = False;"), "skippedChestCollecting = True;") #If nothing to do then skips
            print("Nothing to do so skipping.")
            break
        pyautogui.failSafeCheck()
        checkIfRainShower()
        keyboard.press_and_release('space')
        time.sleep(1)
        foundOre = checkIfOre()
        if foundOre:
            continue #Skips most likely only one thing on floor skipping for better performance
        foundMonster = monsters.checkIfMonster()
        monsters.checkIfFightScreen()
        if foundMonster:
            continue #Skips most likely only one thing on floor skipping for better performance
        chestbackgroundcolor = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\smallchestbackgroundcolor.png", confidence = yellowbackgroundConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            

        if chestbackgroundcolor == None:
            nothingToDoInARow = nothingToDoInARow + 1
        else:
            nothingToDoInARow = 0 #reset counter if no background color was found
        iterateOverAllMinersOnAFloor(0)
        monsters.checkIfFightScreen()

        chestbackgroundcolor = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\smallchestbackgroundcolor.png", confidence = yellowbackgroundConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            

        print(chestbackgroundcolor)

        if chestbackgroundcolor != None:
            chestbackgroundcolor = pyautogui.center(chestbackgroundcolor)
            pyautogui.moveTo(chestbackgroundcolor)
            time.sleep(6)
            print("Yellow background detected below middle floor")
            collectChestBelowMiddle()
        counter = counter + 1
        print("Collecting chests from mine: " + str(counter + 1) + "/" + str(maxCount))
        print("Nothing to do count: " + str(nothingToDoInARow) + "/" + str(amountOfTriesBeforeSkip))

def collectChestsInMineWithImageRecognition():
    #Was used in version 0.7
    #Slower version but gives more precision
    #Ended with not using images for this as it slows down the performance alot
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

        chestbackgroundcolor = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\smallchestbackgroundcolor.png", confidence = chestConfidence - 0.1, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            

        pyautogui.failSafeCheck()
        keyboard.press_and_release('space')
        time.sleep(positions.defaultDelay)
        checkIfOre()
        monsters.checkIfMonster()
        monsters.checkIfFightScreen()

        chestConfidence = 0.6 #0.6 works really good
        grayscaleIsOn = False

        minerWithChestEarth = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\minerwithchestearth.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            

        earthchest1Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\earthchest1.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue), grayscale = grayscaleIsOn)            
        earthchest2Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\earthchest2.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue), grayscale = grayscaleIsOn)            
        earthchest3Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\earthchest3.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue), grayscale = grayscaleIsOn)            
        earthchest4Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\earthchest4.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue), grayscale = grayscaleIsOn)            

        moonchest1Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\moonchest1.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue), grayscale = grayscaleIsOn)            
        moonchest2Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\moonchest2.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue), grayscale = grayscaleIsOn)            
        moonchest3Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\moonchest3.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue), grayscale = grayscaleIsOn)            
        moonchest4Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\moonchest4.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue), grayscale = grayscaleIsOn)            

        goldchest1Position = None
        goldchest2Position = None
        goldchest3Position = None
        goldchest4Position = None

        #Can disable gold chest detection for better performance
        if fh.stringInFileExists(positions.userconfigFile, "goldchestDetection = True;"):
            print("goldchest = True")
            goldchest1Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\goldchest1.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            
            goldchest2Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\goldchest2.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            
            goldchest3Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\goldchest3.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            
            goldchest4Position = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\goldchest4.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            

        #chestleftside1 = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\chestleftside1.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            
        #chestleftside2 = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\chestleftside2.png", confidence = chestConfidence, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            

        chestbackgroundcolor = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\mine\\smallchestbackgroundcolor.png", confidence = chestConfidence - 0.1, region=(lowerThreeLeftXValue, lowerThreeLeftYValue, lowerThreeTopRightXValue, lowerThreeLeftXValue))            

        #print(minerWithChestEarth)
        chestList = [
            earthchest1Position, earthchest2Position, earthchest3Position, earthchest4Position, moonchest1Position,
            moonchest2Position, moonchest3Position, moonchest4Position, goldchest1Position, goldchest2Position, goldchest3Position,
            goldchest4Position, minerWithChestEarth
        ] #chestleftside1, chestleftside2]
        correctXYToMoveTo = None
        for i in range(len(chestList)):
            if chestList[i] != None:
                print(chestList[i], i)
                correctXYToMoveTo = chestList[i]

        if correctXYToMoveTo != None: #Means it found something
            foundChest = True
            nothingToDoInARow = 0 # Resets when it has found a chest
            chestPosition = pyautogui.center(correctXYToMoveTo)
            pyautogui.moveTo(chestPosition[0], correctXYToMoveTo[1] + 50)
            clickMouse()
            clickChestInMiddleOfScreens()
        else:
            nothingToDoInARow = nothingToDoInARow + 1 #Did not find a a chest
            if chestbackgroundcolor != None: #Found yellow background
                print("Did not find chest on screen, but detected yellow background.")
                iterateOverAllMinersOnAFloor()
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
        iterateOverAllMinersOnAFloor()
        print("Collecting chests from mine: " + str(counter + 1) + "/" + str(maxCount))
        counter = counter + 1

def iterateOverAllMinersOnAFloor(modifier):

    '''
    Modifier can be 0\n
    If 0 then scans middle floor\n

    ------
    ------
    XXXXXX
    ------\n
    ------\n

    If modifier = 200
    then goes up one level

    ------
    XXXXXX
    ------
    ------
    ------

    If modifier = -200
    then goes down one level

    ------
    ------
    ------
    XXXXXX
    ------

    '''

    try:
        keyboard.press("left shift")
        for everyMiner in range(len(positions.minerPosistionList)):
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.minerPosistionList[everyMiner], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.minerYpositionMiddleLevel - modifier, positions.currentResolution[1], positions.originalResolution[1]))
            mouseAndKeyboard.clickMouse()
        keyboard.release("left shift")
    except:
        keyboard.release("left shift") # should fix left shift getting stuck if causing an interrupt

def collectChestBelowMiddle():

    '''
    Function must be placed after it has checked once and 'tried' to collect chest.\n
    If yellow background is still there it means it's below middle level.\n
    '''

    for i in range(1, 3):
        iterateOverAllMinersOnAFloor(i * - 200)

def fastCollectChest(*args):
    bufflab.clickOneBuff(bufflab.lowestTierNuggetOfAttraction)
    generalFunctions.goToMrMineScreen()
    generalFunctions.goToSafeClickArea()
    amountOfIterations = 30
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.minerPosistionList[4] - positions.currentResolution[0] / 100 * 3, positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.minerYpositionMiddleLevel, positions.currentResolution[1], positions.originalResolution[1]))
    if args:
        amountOfIterations = args[0]
    for i in range(amountOfIterations):
        try:
            print("Fast collecting: " + str(i) + "/" + str(amountOfIterations))
            keyboard.press_and_release('space')
            keyboard.press("left shift")
            mouseAndKeyboard.clickMouse()
            keyboard.release("left shift") # should fix left shift getting stuck if causing an interrupt
        except KeyboardInterrupt:
            keyboard.release("left shift")
        except Exception as e:
            print(e)
            keyboard.release("left shift")

def fastCollectChestOld():
    generalFunctions.goToMrMineScreen()
    amountOfIterations = 30
    for i in range(amountOfIterations):
        try:
            print("Fast collecting: " + str(i) + "/" + str(amountOfIterations))
            keyboard.press_and_release('space')
            keyboard.press("left shift")
            for everyMiner in range(len(positions.minerPosistionList)):
                pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.minerPosistionList[everyMiner], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.minerYpositionMiddleLevel, positions.currentResolution[1], positions.originalResolution[1]))
                mouseAndKeyboard.clickMouse()
            keyboard.release("left shift") # should fix left shift getting stuck if causing an interrupt
        except KeyboardInterrupt:
            keyboard.release("left shift")
        except Exception as e:
            print(e)
            keyboard.release("left shift")

def checkIfRainShower():
    print("Checking for rain shower buff.")
    mouseAndKeyboard.pressButton('esc')
    generalFunctions.goToMrMineScreen()
    generalFunctions.goToSafeClickArea()
    rainShowerConfidence = 0.7 #0.7 works
    time.sleep(0.5)
    rainShower = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\general\\rainingchest.png", confidence = rainShowerConfidence)
    if rainShower:
        print(rainShower)
        print("Detected rain shower!")
        fastCollectChest(150)
    else:
        print("No rain shower detected.")
    mouseAndKeyboard.pressButton('space')

#fastCollectChest()