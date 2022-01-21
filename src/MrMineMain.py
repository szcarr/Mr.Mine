import pyautogui

import cave
import bufflab
import mineFloors
import gemCrafting
import excavtions
import metalDetector
import sellMinerals
import reactor
import trading

pyautogui.FAILSAFE = True

'''
When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort your program:
'''

amountOfGemsToCraft = 5
amountOfChestsToBeClicked = 10

def doAutoEverythingBySequence():
    #Main
    firstRun = True
    while True:
        reactor.reactorMain()
        gemCrafting.craftGems(amountOfGemsToCraft)
        trading.trade()
        excavtions.scientists()
        mineFloors.miningMain()
        cave.doCaves()
        gemCrafting.craftGems(amountOfGemsToCraft)
        trading.trade()
        excavtions.scientists()
        sellMinerals.sellMinerals()
        
        metalDetector.metalDetectorMain()
        gemCrafting.craftGems(amountOfGemsToCraft)
        excavtions.scientists()
        cave.collectCaveItems(amountOfChestsToBeClicked)
        bufflab.buffLab()
        sellMinerals.sellMinerals() #Do things before selling