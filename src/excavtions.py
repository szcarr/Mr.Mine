import time
import pyautogui
import keyboard

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution
import useTicket

positions = positionsAndResolution.positions

#Scientists
scientistCollectButton = 963, 732
scientistForfeitReward = 963, 771
scientistTabOne = 570, 248
scientistTabTwo = 761, 248
scientistTabThree = 942, 248
scientistHardDifficulty = 1199, 722
scientistRelicInvetoryFullOkButton = 968, 172
scientistForfeitRewardYesButton = 969, 200
scientistCancelTicketPurchase = 970, 229
scientistsList = [scientistTabOne, scientistTabTwo, scientistTabThree]

def scientists():
    #NOT DONE
    useTicket.useTickets()
    generalFunctions.goToMrMineScreen()
    time.sleep(positions.defaultDelay)
    keyboard.press_and_release('k') #GOINNG TO SAFE SCREEN FIRST
    time.sleep(positions.defaultDelay)
    keyboard.press_and_release('shift+s')
    time.sleep(positions.defaultDelay)
    textString = "Collecting rewards from scientists "
    for i in range(2):
        if i > 0:
            textString = "Queueing new tasks for scientists "
        for x in range(len(scientistsList)):#amount of scientists
            print(textString + str(x + 1) + "/" + str(len(scientistsList)) + "...")
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistsList[x][0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistsList[x][1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistHardDifficulty[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistHardDifficulty[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistCollectButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistCollectButton[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistRelicInvetoryFullOkButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistRelicInvetoryFullOkButton[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            time.sleep(positions.defaultDelay)
            generalFunctions.clickChestInMiddleOfScreen()
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistForfeitReward[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistForfeitReward[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            time.sleep(positions.defaultDelay)
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistForfeitRewardYesButton[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistForfeitRewardYesButton[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            #next is forfeiting
    time.sleep(positions.defaultDelay)
    pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(scientistCancelTicketPurchase[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(scientistCancelTicketPurchase[1], positions.currentResolution[1], positions.originalResolution[1]))
    time.sleep(positions.defaultDelay)
    mouseAndKeyboard.clickMouse()
    time.sleep(positions.defaultDelay)
    mouseAndKeyboard.pressButton('esc')