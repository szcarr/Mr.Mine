import pyautogui
import keyboard
import time

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution
import useTicket
import fileHandling as fh
import mineFloors

positions = positionsAndResolution.positions
relicTab = 1139, 249

relicTrashCan = 962, 765

relics = ["bullseye"]

confidenceOfRelics = {
    "bullseye": 0.95
}

def deleteRelics():

    '''
    Deletes unwanted relics.
    '''

    generalFunctions.goToMrMineScreen()
    generalFunctions.goToSafeClickArea()
    keyboard.press_and_release('shift+s')
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(relicTab[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(relicTab[1], positions.currentResolution[1], positions.originalResolution[1]))
    mouseAndKeyboard.clickMouse()
    time.sleep(0.5)
    for i in range(len(relics)):
        image = relics[i]
        relicExists = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir() + "images\\relics\\" + image + ".png"), confidence = confidenceOfRelics.get(image))
        if relicExists:
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(relicTrashCan[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(relicTrashCan[1], positions.currentResolution[1], positions.originalResolution[1]))
            mouseAndKeyboard.clickMouse()
            pyautogui.moveTo(relicExists)
            


#deleteRelics()