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
amountOfChestsToBeClicked = 20

def doAutoEverythingBySequence():
    #Main
    while True:
        mineFloors.collectChestsInMineImproved()
        gemCrafting.craftGems(amountOfGemsToCraft)
        #excavtions.scientists()
        sellMinerals.sellMinerals()
        metalDetector.collectNormalChestsFromMetalDetector()
        gemCrafting.craftGems(amountOfGemsToCraft)
        #excavtions.scientists()
        cave.collectCaveItems(amountOfChestsToBeClicked)
        sellMinerals.sellMinerals() #Do things before selling


'''
-------------------------MAIN PROGRAM-------------------------
'''
#convertValuesFromNewScreenToOld(1285, 976) # collect
#convertValuesFromNewScreenToOld(1285, 1028) # forfeiting reward
#convertValuesFromNewScreenToOld(760, 330) # scientist 1
#convertValuesFromNewScreenToOld(1015, 330) # scientist 2
#convertValuesFromNewScreenToOld(1256, 330) # scienttist 3
#convertValuesFromNewScreenToOld(1293, 305) # hard difficulty
#useTickets()