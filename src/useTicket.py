import time
import pyautogui

import generalFunctions
import MrMineMath
import mouseAndKeyboard
import positionsAndResolution
import fileHandling

positions = positionsAndResolution.positions
fh = fileHandling

pressUseTickets = 756, 140

pressGoldChest = 1153, 639
pressNormalChest = 768, 639

def useTickets():

    '''
    Function to consume mr mine tickets before wasting them on scientists, since re rolling and forfeiting reward has yes button on the same pixel position.
    '''

    print("Going to ticket store")
    generalFunctions.goToFloorZero()
    time.sleep(positions.defaultDelay)

    nullTicketConfidence = 0.98 #Maybe needs adjusting
    firstRun = True
    dynamicString = ""
    for i in range(10):
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.minerPosistionList[7], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.minerYpositionMiddleLevel, positions.currentResolution[1], positions.originalResolution[1]))
        time.sleep(positions.defaultDelay)
        mouseAndKeyboard.clickMouse()
        time.sleep(0.5) # TEST
        nullTicketPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\general\\null_tickets.png", confidence = nullTicketConfidence)
        print(nullTicketPosition)
        if nullTicketPosition == None: #MEANS THERE IS TICKETS
            print("Detected tickets!")      
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(pressUseTickets[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(pressUseTickets[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            mouseAndKeyboard.clickMouse()
            #Clicking gold chest
            if firstRun:
                firstRun = False
                pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(pressGoldChest[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(pressGoldChest[1], positions.currentResolution[1], positions.originalResolution[1]))
                time.sleep(positions.defaultDelay)
                dynamicString = "golden chest"
            else:
                #Openenig normal chests
                pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(pressNormalChest[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(pressNormalChest[1], positions.currentResolution[1], positions.originalResolution[1]))
                time.sleep(positions.defaultDelay)
                dynamicString = "normal chest"
            print("Opening " + dynamicString + " with tickets...")
            mouseAndKeyboard.clickMouse()
            generalFunctions.clickChestInMiddleOfScreen()
        else:
            print("Zero tickets so skipping...")
            break
    print("Forst")
    mouseAndKeyboard.pressButton('esc')


def useTicketsBackup():

    '''
    Function to consume mr mine tickets before wasting them on scientists, since re rolling and forfeiting reward has yes button on the same pixel position.
    '''

    print("Going to ticket store")
    generalFunctions.goToFloorZero()
    time.sleep(positions.defaultDelay)

    nullTicketConfidence = 0.8 #Maybe needs adjusting
    firstRun = True
    dynamicString = ""
    for i in range(10):
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(positions.minerPosistionList[7], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(positions.minerYpositionMiddleLevel, positions.currentResolution[1], positions.originalResolution[1]))
        time.sleep(positions.defaultDelay)
        mouseAndKeyboard.clickMouse()
        ticketPosition = pyautogui.locateOnScreen(str(fh.getPathToCurrentDir()) + "images\\general\\null_tickets.png", confidence = nullTicketConfidence, grayscale = True)
        time.sleep(0.3) #TEST
        if ticketPosition != None:
            print("Already zero tickets so skipping...")
            break    
        pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(pressUseTickets[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(pressUseTickets[1], positions.currentResolution[1], positions.originalResolution[1]))
        time.sleep(positions.defaultDelay)
        mouseAndKeyboard.clickMouse()
        #Clicking gold chest
        if firstRun:
            firstRun = False
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(pressGoldChest[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(pressGoldChest[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            dynamicString = "golden chest"
        else:
            #Openenig normal chests
            pyautogui.moveTo(MrMineMath.convertToCurrentResolutionPosition(pressNormalChest[0], positions.currentResolution[0], positions.originalResolution[0]), MrMineMath.convertToCurrentResolutionPosition(pressNormalChest[1], positions.currentResolution[1], positions.originalResolution[1]))
            time.sleep(positions.defaultDelay)
            dynamicString = "normal chest"
        print("Opening " + dynamicString + " with tickets...")
        mouseAndKeyboard.clickMouse()
        generalFunctions.clickChestInMiddleOfScreen()
    mouseAndKeyboard.pressButton('esc')