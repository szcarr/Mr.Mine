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
        excavtions.excavationsMain()
        sellMinerals.sellMinerals()
        mineFloors.miningMain()
        trading.trade()
        cave.doCaves()
        gemCrafting.craftGems(amountOfGemsToCraft)
        trading.trade()
        excavtions.excavationsMain()
        sellMinerals.sellMinerals()
        
        metalDetector.metalDetectorMain()
        trading.trade()
        gemCrafting.craftGems(amountOfGemsToCraft)
        excavtions.excavationsMain()
        cave.collectCaveItems(amountOfChestsToBeClicked)
        bufflab.buffLabMain()
        trading.trade()
        sellMinerals.sellMinerals() #Do things before selling