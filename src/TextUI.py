import pyautogui
import time

import MrMineMain
import config
import setup

config.initialize()
setup.downloadDependencies()

'''
This is the main file
'''

exitProgram = False

modeList = {
    "getc": "GetCurrentPosition | Prints current XY value of mouse position | CTRL+C to escape | Syntax: getc",
    "help": "Help | Prints all legal commands | Syntax: help",
    "doall": "Automatic Everything | Does everything there is to do in Mr.Mine | Syntax: doall",
    "exit": "Exit | Exits current program | Syntax: exit"
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
    except:
        print("Error in selecting mode")

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
    while True:
        print(pyautogui.position())
        time.sleep(1)
'''
-------------------------MAIN PROGRAM-------------------------
'''

#print(pyautogui.KEYBOARD_KEYS) #LEGAL KEYS

menu()