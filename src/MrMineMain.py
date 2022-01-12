import pyautogui
import keyboard
import time

import MrMineMath
import cave
import bufflab
import mineFloors
import gemCrafting
import excavtions
import metalDetector
import sellMinerals

pyautogui.FAILSAFE = True

'''
When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort your program:
'''

amountOfGemsToCraft = 5
amountOfChestsToBeClicked = 10

def doAutoEverythingBySequence():
    #Main
    while True:
        mineFloors.collectChestsInMineImproved()
        gemCrafting.craftGems(amountOfGemsToCraft)
        excavtions.scientists()
        sellMinerals.sellMinerals()
        metalDetector.collectNormalChestsFromMetalDetector()
        metalDetector.collectGoldChestsFromMetalDetector()
        gemCrafting.craftGems(amountOfGemsToCraft)
        excavtions.scientists()
        cave.collectCaveItems(amountOfChestsToBeClicked)
        bufflab.buffLab()
        sellMinerals.sellMinerals() #Do things before selling

'''
-------------------------MAIN PROGRAM-------------------------
'''