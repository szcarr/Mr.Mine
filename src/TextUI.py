import pyautogui
import keyboard
import time
#import MrMineFunctions

exitProgram = False

modeList = {
    "getC": "GetCurrentPosition | Prints current XY value of mouse position | CTRL C to escape | Syntax: getc",
    "help": "Help | Prints all legal commands | Syntax: help",
    "exit": "Exit | Exits current program | Syntax: exit"
}

#runTime = time.process_time()

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