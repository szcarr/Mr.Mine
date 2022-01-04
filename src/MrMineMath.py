import pyautogui

def convertToCurrentResolutionPosition(actualPositionOnScreen, resolution, resolutionCompared):
    '''
    actualPositionOnScreen is the value of either the x or y value on the screen

    Too convert old position to new you would use this formula

    actualPositionOnScreen = 670
    resolution = 2560
    resolutionCompared = 1920

    resolution * (actualPositionOnScreen / resolutionCompared)

    converts the value gotten at a 1920 screen to 2560 screen relative to its pixel placement in growth factor

    -----------------------------------------------------------------------------

    Too convert new position to old you would do this 

    actualPositionOnScreen = 670
    resolution = 1920
    resolutionCompared = 2560

    resolution * (actualPositionOnScreen / resolutionCompared)
    
    '''

    position = resolution * (actualPositionOnScreen / resolutionCompared) #Evil hacks
    return position
