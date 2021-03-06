import time
import pyautogui

import MrMineMath
import fileHandling

fh = fileHandling

pathToCurrentDir = fh.getPathToCurrentDir()
splitBy = fh.detectOS()

# 0,0       X increases -->
# +---------------------------+
# |                           | Y increases
# |                           |     |
# |   1920 x 1080 screen      |     |
# |                           |     V
# |                           |
# |                           |
# +---------------------------+ 1919, 1079

#Values got at 1920 x 1080 screen


'''
---------------------------------------------------MINER-INFO---------------------------------------------------
'''

'''
    Mr mine needs to be in "fullscreen" then you can get the coords for

    These values are gotten at 1920x1080 screen
    New values need to be converted from your main screen to 1920x1080 screen
    ## IF you have 1920x1080 main screen
    ## THEN you can use those values without converting them
    See MrMineMath.py -> convertToCurrentResolutionPosition() function for more details
'''

'''
---------------------------------------------------1920x1080---------------------------------------------------
'''
class positions:
    def getMainMonitorSize():
        monitorRes = str(pyautogui.size())
        monitorRes = monitorRes.split(",")
        actualSize = [] 
        for i in range(len(monitorRes)):
            valueSplitted = str(monitorRes[i].split("=")[1])
            valueSplitted = valueSplitted.split(")")
            actualSize.append(int(valueSplitted[0])) #Dirty little 116 iq move

        #print for debug
        print("Using monitor size " + str(actualSize[0]) + "x" + str(actualSize[1]))

        return tuple(actualSize)

    #File
    userconfigFile = pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt"
    gamestageFile = pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt"
    
    #Resolution
    currentResolution = getMainMonitorSize()
    originalResolution = 1920, 1080

    #General
    menuDoubleClick = 935, 175

    doubleArrowTop = 110, 200
    oneArrowDown = 107, 906

    clickChestInMiddleOfScreen = 969, 557

    middleRowBottomLeft = 158, 476
    middleRowTopRight = 1334, 183 #1334 x

    lowerThreeRowsBottomLeft = 122, 475
    lowerThreeRowsTopRight = middleRowTopRight[0], (middleRowTopRight[1] * 3)

    #Delay
    defaultDelay = 0 #For testing use 1.5 seconds else 0.00000000000000001

    #Miner position
    minerYpositionMiddleLevel = 608
    minerYpositionLowestLevel = 975
    minerPosistionList = [
        190,
        329,
        470,
        609,
        746,
        885,
        1017,
        1163,
        1295, 
        1434,
    ]

    #Minefloors spots to skip #NOT IN USE
    mineFloorsThatIsDifferentToMiners = [
        20,
        45
    ]

    #Monster
    firstRow = [[631, 653], [840, 653], [1050, 653]]
    secondRow = [[631, 702], [840, 702], [1050, 702]]
    thirdRow = [[631, 752], [840, 752], [1050, 752]]
    forthRow = [[631, 802], [840, 802], [1050, 802]]

    allRows = [firstRow, secondRow, thirdRow, forthRow]

    #Chests
    amountOfChestsToBeClicked = 10


def convertValuesFromNewScreenToOld(x, y):
    print(MrMineMath.convertToCurrentResolutionPosition(x, 1920, 2560), end=" ")
    print(MrMineMath.convertToCurrentResolutionPosition(y, 1920, 2560))

def getCurrentPosition():
    while True: 
        print(pyautogui.position())
        time.sleep(1)

def getScreenResoution():
    return pyautogui.size()


'''
---------------------------------------------------2560x1440---------------------------------------------------
'''