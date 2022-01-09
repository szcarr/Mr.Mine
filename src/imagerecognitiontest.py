import pyautogui
import PIL

import fileHandling
import generalFunctions

fh = fileHandling

#print(pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\cave\\bluecaveentrance.png", confidence = 0.8))

generalFunctions.goToMrMineScreen()
for i in range(500):
    pyautogui.scroll(-10)