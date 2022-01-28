import pyautogui
import time

import fileHandling

exitProgram = False

modeList = {
    "exit": "exit | Exits current program | Syntax: exit",
    "sh": "sh | Prints settings help | Syntax: sh",
    "help": "help | Print all legal commands | Syntax: help",

}

'''
-------------------------MENU-------------------------
'''

def menu():
    firstRun = True
    while True:
        if exitProgram:
            break
        if firstRun:
            printSettingsHelp()
        print("> ", end="")
        mode = input()
        checkModes(mode)

def checkModes(mode):
    try:
        modeList = mode.split(" ")
        print(modeList)
        print(modeList[0])
        if modeList[0] == "sh":
            printSettingsHelp()
        elif modeList[0] == "help":
            printHelp()
        elif modeList[0] == "exit":
            exit()


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

def printSettingsHelp():
    print("========================SETTINGS========================")
    print("You are now in settings menu. To return to main either 'CTRL+C' or input 'exit'")
    print("")
    print("")