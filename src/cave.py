import time
import keyboard
import pyautogui
from MrMineFunctions import clickMouse

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution
import fileHandling
import re
import mineFloors

positions = positionsAndResolution.positions
fh = fileHandling

caveScreenRegion = (396, 194, 1115, 562) #1920x1080
caveScreenRegionDynamic = ( round(MrMineMath.convertToCurrentResolutionPosition(caveScreenRegion[0], positions.currentResolution[0], positions.originalResolution[0])),
                            round(MrMineMath.convertToCurrentResolutionPosition(caveScreenRegion[1], positions.currentResolution[1], positions.originalResolution[1])),
                            round(MrMineMath.convertToCurrentResolutionPosition(caveScreenRegion[2], positions.currentResolution[0], positions.originalResolution[0])),
                            round(MrMineMath.convertToCurrentResolutionPosition(caveScreenRegion[3], positions.currentResolution[1], positions.originalResolution[1])),
)

print(caveScreenRegionDynamic)

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
    mineFloors.checkIfRainShower()

def doCaves():
    caveTab = 971, 276
    caveColorList = ["red", "blue"]
    allNodes = ["rednodeundiscovered", "bluenodeundiscovered", "redtools", "bluetools", "chest", "goldchest", "redclock", "blueclock", "redmoneybag", "bluemoneybag", "redbuff", "bluebuff"]
    for potentialCaves in range(3):
        noFuelInCave = False
        generalFunctions.goToMrMineScreen()
        mouseAndKeyboard.pressButton('k')

        ymodifier = 58 * potentialCaves
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(caveTab[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(caveTab[1] + ymodifier, positions.currentResolution[1], positions.originalResolution[1]))
        keyboard.press('left shift')
        mouseAndKeyboard.clickMouse()
        keyboard.release('left shift')

        for allCaveColors in range(len(caveColorList)):
            if noFuelInCave:
                break
            node = caveColorList[allCaveColors]
            isCave = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\cave\\" + node + "detectcave.png", confidence = 0.7) #Checks if previous click actually clicked in on a cave
            print("Checking if in a " + node + " cave.")
            if isCave != None:
                print("Detected that it has clicked in a " + node + " cave.")
                mouseAndKeyboard.clickMouse()
                mouseAndKeyboard.clickMouse()
                for i in range(2): #Scrolls to the deepest part of the cave
                    pyautogui.scroll(-1000)
                #Next is scan for nodes
                for i in range(5):
                    if noFuelInCave:
                        break
                    tempList = []
                    pyautogui.moveTo(positions.currentResolution[0] * 0.50, positions.currentResolution[1] * 0.50)
                    pyautogui.scroll(110 * i)
                    print("Scrolling towards the 'entrance' of the cave")
                    allThingsInCave = []
                    for a in range(len(allNodes)): #For all types poi in cave
                        pyautogui.failSafeCheck()
                        crossout = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir() + "images\\cave\\xoutofsenddrone.png"), confidence = 0.8)
                        if crossout:
                            print("Crossing out")
                            pyautogui.moveTo(pyautogui.center(crossout))
                            mouseAndKeyboard.clickMouse()
                        pyautogui.moveTo(positions.currentResolution[0] * 0.50, positions.currentResolution[1] * 0.65)
                        time.sleep(0.5)
                        node = allNodes[a]
                        print(node)
                        caveNodes = tuple(pyautogui.locateAllOnScreen(str(fh.getPathToCurrentDir() + "images\\cave\\" + node + ".png"), confidence = 0.67, region = caveScreenRegionDynamic))
                        print("CaveNodes")
                        print(caveNodes)
                        #time.sleep(10)
                        tempList.clear()
                        for c in range(len(caveNodes)): #Adding all poi found to a singular list
                            myTuple = (caveNodes[c][0], caveNodes[c][1], caveNodes[c][2], caveNodes[c][3])
                            #print(myTuple)
                            #time.sleep(16)
                            allThingsInCave.append(myTuple) #x value
                        #print(tempList)
                        #allThingsInCave.append(tempList)
                    if allThingsInCave != None: #if allthingsInCave has atleast one variable
                        print("Allthingincaves")
                        print(allThingsInCave)
                        filteredNodes = filterByLargestXValue(filterNodes(allThingsInCave)) #Filters all poi by largest x value
                        #print("Filtered nodes:")
                        #print(filteredNodes)
                        #time.sleep(30)
                        for p in range(len(filteredNodes)): #For all cavenodes in that specific cave
                            #if p == 7:
                                #break
                            #print("Found " + node) #Inaccurate
                            pyautogui.moveTo(pyautogui.center(filteredNodes[p]))
                            print(filteredNodes[p])
                            #time.sleep(2)
                            mouseAndKeyboard.clickMouse()
                            basicdrone = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir() + "images\\cave\\basicdrone.png"), confidence = 0.67)
                            if basicdrone:
                                pyautogui.moveTo(pyautogui.center(basicdrone))
                                mouseAndKeyboard.clickMouse()
                            senddrone = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir() + "images\\cave\\senddrone.png"), confidence = 0.8)
                            if senddrone:
                                pyautogui.moveTo(pyautogui.center(senddrone))
                                mouseAndKeyboard.clickMouse()
                            nofuel = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir() + "images\\cave\\nofuel.png"), confidence = 0.8)
                            if nofuel:
                                noFuelInCave = True
                                break
                            crossout = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir() + "images\\cave\\xoutofsenddrone.png"), confidence = 0.8)
                            if crossout:
                                print("Crossing out")
                                pyautogui.moveTo(pyautogui.center(crossout))
                                mouseAndKeyboard.clickMouse()
    keyboard.release('left shift')

def filterNodes(allCords): 
    #Evil hack
    '''
    Filters values from list that are very close to each other
    Argument passed is expected to be a tuple with a list with 4 integers as elements
    '''

    growthFactorDeviation = 0.05 #Can change but 0.05 seems to work fine
    filteredList = []
    for x in range(len(allCords)):
        if not filteredList:
            filteredList.append(allCords[x])
            continue
        if filteredList[len(filteredList) - 1][0] * (1 - growthFactorDeviation) > allCords[x][0] or filteredList[len(filteredList) - 1][1] * (1 + growthFactorDeviation) < allCords[x][1]:
            filteredList.append(allCords[x])
    return filteredList

def filterByLargestXValue(inputListe):

    '''
    Expected arg is a list with a list with quadruple integers as elements to its parent list
    [[442, 660, 230, 100], [424, 653, 232, 101]]
    Returns the same list but the list in the list is now filtered after its first element in the list by largest value
    '''

    filtrertListe = []
    indexSkipList = []
    skipIndex = 0
    while len(filtrertListe) != len(inputListe):
        largestXValueNow = 0
        xyListe = []
        for y in range(len(inputListe)): #For kvart element i liste. som er endå ei liste
            skip = False
            for x in range(len(indexSkipList)):
                if indexSkipList[x] == y:
                    skip = True
            if skip:
                continue
            if inputListe[y][0] > largestXValueNow: #Sjekkar for kvart element om kva som er størst
                largestXValueNow = inputListe[y][0]
                skipIndex = y
                yValueOfX = inputListe[y][1]
                wValueOfX = inputListe[y][2]
                hValueOfX = inputListe[y][3]
            #print(largestXValueNow)
        xyListe.append(largestXValueNow)
        xyListe.append(yValueOfX)
        xyListe.append(wValueOfX)
        xyListe.append(hValueOfX)
        filtrertListe.append(xyListe)
        indexSkipList.append(skipIndex)

    return filtrertListe      

def doCavesOld():
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
        caveNodes = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\cave\\bluecaveentrance.png", confidence = 0.8, region=(middleRowBottomLeftXValue, middleRowBottomLeftYValue, middleRowTopRightXValue, middleRowTopRightYValue))

        caveList = [redCaveCenter, caveNodes]
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
        nodeColorList = ["red", "blue"]
        for c in range(len(nodeColorList)):
            color = nodeColorList[c]
            caveNodes = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\cave\\" + color + "nodeundiscovered.png", confidence = 0.8, region=(middleRowBottomLeftXValue, middleRowBottomLeftYValue, middleRowTopRightXValue, middleRowTopRightYValue))
            if caveNodes != None:
                for p in range(len(caveNodes)):
                    caveNodes[p]

#doCaves()