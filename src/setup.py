import os

import fileHandling
import positionsAndResolution

fh = fileHandling
positions = positionsAndResolution.positions

def downloadDependencies():
    stringToLookFor = "hasInstalledModules = False;"
    if fh.stringInFileExists(positions.userconfigFile, stringToLookFor):
        os.system("pip install keyboard")
        os.system("pip install pyautogui")
        os.system("pip install opencv-python")
        os.system("pip install Pillow")
        fh.replaceLineInFile(positions.userconfigFile, fh.getLineNumberFromFile(positions.userconfigFile, stringToLookFor), "hasInstalledModules = True;\n")