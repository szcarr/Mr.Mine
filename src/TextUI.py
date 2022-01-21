import pyautogui
import time

import MrMineMain
import config
import setup
import mineFloors

try:
    config.deleteCFGdir()
except:
    pass
config.initialize()
setup.downloadDependencies()

'''
This is the main file
'''

exitProgram = False

modeList = {
    "getc": "getc | Prints current XY value of mouse position | CTRL+C to escape | Syntax: getc",
    "help": "help | Prints all legal commands | Syntax: help",
    "doall": "doall | Does everything there is to do in Mr.Mine | Syntax: doall",
    "exit": "exit | Exits current program | Syntax: exit",
    "rescfg": "rescfg | Resets config folder | Syntax: rescfg",
    "fastc": "fastc | Fast collects chest | Syntax: fastc"
}

'''
-------------------------MENU-------------------------
'''

def menu():
    while True:
        if exitProgram:
            break
        printHelp()
        print("> ", end="")
        mode = input()
        checkModes(mode)

def checkModes(mode):
    try:
        modeList = mode.split(" ")
        print(modeList)
        print(modeList[0])
        if modeList[0] == "getc":
            printCurrentMousePosition()
        elif modeList[0] == "help":
            printHelp()
        elif modeList[0] == "exit":
            exit()
        elif modeList[0] == "doall":
            MrMineMain.doAutoEverythingBySequence()
        elif modeList[0] == "rescfg":
            config.deleteCFGdir()
            config.initialize()
        elif modeList[0] == "fastc":
            mineFloors.fastCollectChest()
    except KeyboardInterrupt:
        print("Keyboard interrupt.")
    except Exception as e:
        print(e)

def exit():
    global exitProgram
    exitProgram = True
    print("Exiting...")

'''
-------------------------GENERAL HELPERS-------------------------
'''

def printHelp():
    keysForModeList = list(modeList.keys())
    counter = 0
    print("\n-------------------------HELP-------------------------")
    for key in keysForModeList:
        counter += 1
        print(str(counter) + ": " + str(modeList.get(key)))

def printCurrentMousePosition():
    xValue = 0
    yValue = 0
    try:
        while True:
            xValue = pyautogui.position()[0]
            yValue = pyautogui.position()[1]
            print(pyautogui.position())
            time.sleep(1)
    except KeyboardInterrupt:
        print("Converted value: " + str(xValue * 0.75) + ", " + str(yValue * 0.75))

'''
-------------------------MAIN PROGRAM-------------------------
'''

#print(pyautogui.KEYBOARD_KEYS) #LEGAL KEYS

menu()