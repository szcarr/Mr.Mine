import pyautogui
import keyboard
import time

import mouseAndKeyboard
import fileHandling as fh
import generalFunctions
import MrMineMath
import positionsAndResolution

positions = positionsAndResolution.positions

inventory = (406, 282, 761, 180)

inventoryX = MrMineMath.convertToCurrentResolutionPosition(inventory[0], positions.currentResolution[0], positions.originalResolution[0])
inventoryY = MrMineMath.convertToCurrentResolutionPosition(inventory[1], positions.currentResolution[1], positions.originalResolution[1])
inventoryWidth = MrMineMath.convertToCurrentResolutionPosition(inventory[2], positions.currentResolution[0], positions.originalResolution[0])
inventoryHeight = MrMineMath.convertToCurrentResolutionPosition(inventory[3], positions.currentResolution[1], positions.originalResolution[1])

dynamicInventory = (inventoryX, inventoryY, inventoryWidth, inventoryHeight)

reactorCraft = 666, 160 # converted
fuelrodTab = 601, 230
redMaxRod = 614, 298
greenMaxRod = 447, 373
blueMaxRod = 697, 373
grayMaxRod = 531, 451
purpleRod = 614, 451

craftButton = 1196, 997
cancelButton = 966, 224

fuelRodList = ["red", "green", "blue", "gray", "purple"]

reactorScreenRegion = (755, 285, 600, 600) #1920x1080
reactorScreenRegionDynamic = ( round(MrMineMath.convertToCurrentResolutionPosition(reactorScreenRegion[0], positions.currentResolution[0], positions.originalResolution[0])),
                            round(MrMineMath.convertToCurrentResolutionPosition(reactorScreenRegion[1], positions.currentResolution[1], positions.originalResolution[1])),
                            round(MrMineMath.convertToCurrentResolutionPosition(reactorScreenRegion[2], positions.currentResolution[0], positions.originalResolution[0])),
                            round(MrMineMath.convertToCurrentResolutionPosition(reactorScreenRegion[3], positions.currentResolution[1], positions.originalResolution[1])),
)

confidenceOfFuelRods = {
    "red": 0.86,
    "green": 0.86,
    "blue": 0.86,
    "gray": 0.86,
    "purple": 0.86,
}

confidenceOfEmptyFuelRods = {
    "red": 0.7,
    "green": 0.7,
    "blue": 0.7,
    "gray": 0.7,
    "purple": 0.7,
}

def craftFuelRods():

    '''
    Crafts the most valuable fuel rods first.
    '''
    generalFunctions.goToMrMineScreen()
    mouseAndKeyboard.pressButton('r')
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(reactorCraft[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(reactorCraft[1], positions.currentResolution[1], positions.originalResolution[1]))
    mouseAndKeyboard.clickMouse()
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(fuelrodTab[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(fuelrodTab[1], positions.currentResolution[1], positions.originalResolution[1]))
    mouseAndKeyboard.clickMouse()

    fuelRodList = [redMaxRod, greenMaxRod, blueMaxRod, grayMaxRod, purpleRod]

    for i in range(len(fuelRodList) - 1, -1, -1):
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(fuelRodList[i][0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(fuelRodList[i][1], positions.currentResolution[1], positions.originalResolution[1]))
        mouseAndKeyboard.clickMouse()
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(craftButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(craftButton[1], positions.currentResolution[1], positions.originalResolution[1]))
        for i in range(8):
            mouseAndKeyboard.clickMouse()

def reactorMain():
    craftFuelRods()
    lookForAndPlaceFuelRods()

def lookForAndPlaceFuelRods():
    for i in range(len(fuelRodList)):
        generalFunctions.goToMrMineScreen()
        mouseAndKeyboard.pressButton('r')
        imageString = fuelRodList[i]
        print("Looking for " + imageString + " fuel rod.")
        time.sleep(0.5)
        emptyfuelrodPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\reactor\\" + imageString + "fuelrodempty.png", confidence = confidenceOfEmptyFuelRods.get(imageString), region = reactorScreenRegionDynamic)
        #
        print(emptyfuelrodPosition)
        #time.sleep(5)
        try:
            if emptyfuelrodPosition != None: #For alle positions on screen
                print("Found " + imageString + " fuelrod in reactor.")
                print("Trying to find a match in inventory...")
                #time.sleep(5)
                #print(r)
                #if emptyfuelrodPosition != None:
                inventoryfuelrodPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\reactor\\" + imageString + "fuelrodinventory.png", confidence = confidenceOfFuelRods.get(imageString)) #region = (dynamicInventory[0], dynamicInventory[1], dynamicInventory[2], dynamicInventory[4])
                #print(inventoryfuelrodPosition)
                #time.sleep(5)
                if inventoryfuelrodPosition != None: #Checks if it has item of similar color in inventory before clicking
                    print("Found similar fuelrod in inventory.")
                    print("Replacing burnt fuel rod with new one.")
                    pyautogui.moveTo(pyautogui.center(emptyfuelrodPosition))
                    #time.sleep(5)
                    keyboard.press('left shift')
                    mouseAndKeyboard.clickMouse()
                    print(inventoryfuelrodPosition)
                    pyautogui.moveTo(pyautogui.center(inventoryfuelrodPosition))
                    #time.sleep(5)
                    mouseAndKeyboard.clickMouse()
                else:
                    print("Did not find similar fuel rod in inventory.")
                    break
        except KeyboardInterrupt:
            keyboard.release('left shift')
            print("error")
        except Exception as e:
            print(e)
        keyboard.release('left shift')
        generalFunctions.goToSafeClickArea()
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(cancelButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(cancelButton[1], positions.currentResolution[1], positions.originalResolution[1]))
        mouseAndKeyboard.clickMouse()

#lookForAndPlaceFuelRods()