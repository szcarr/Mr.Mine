import time
import pyautogui
import positionsAndResolution

positions = positionsAndResolution.positions

def clickMouse():
    #print("Clicking mouse")
    pyautogui.click()
    time.sleep(positions.defaultDelay)

def pressButton(button):
    #button is a string
    #example: button = "s"
    print("Pressing button " + button + "...")
    pyautogui.press(button)
    time.sleep(positions.defaultDelay)