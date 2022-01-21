from datetime import datetime

def getUTCtime():

    '''
    Returns a string with current date and time
    Can split string by " " to get date and time separately
    '''

    return str(datetime.utcnow())

def getDateToday():

    '''
    Returns a string with today's date
    Can split the date to get YYYY-MM-DD
    '''

    splitList = getUTCtime().split(" ")
    return splitList[0]

def getCurrentTime():

    '''
    Returns a string with UTC time (HH:MM:SS)
    Can split time by ":" to get hours,minutes,seconds separately
    '''

    splitList = getUTCtime().split(" ")
    return splitList[1]

def scheduleTimeAndDate(timeToAdjust, hours, minutes, seconds):

    '''
    Can pass hours as an integer value, hours = 11
    Can pass minutes as an integer value, minutes = 42
    Can pass seconds as an integer value, seconds = 23    
    '''

    timeList = [hours, minutes, seconds]
    timeToAdjust = str(timeToAdjust).split(":")
    print(timeToAdjust)
    for i in range(len(timeToAdjust)):
        timeToAdjust[i] = int(timeToAdjust[i]) + timeList[i]

    maxLimit = [24, 60, 60]
    for i in range(len(timeToAdjust) - 1, -1, -1):
        while timeToAdjust[i] > maxLimit[i]:
            try:
                timeToAdjust[i] - maxLimit[i]
                timeToAdjust[i - 1] + 1
            except:
                pass

    scheduledTime = ""
    myFunnyVariable = ":"
    print(timeToAdjust)
    for i in range(len(timeToAdjust)):
        if i == len(timeToAdjust) - 1:
            myFunnyVariable = ""
        print(str(timeToAdjust[i]), str(timeList[i]))
        scheduledTime = scheduledTime + str(int(timeToAdjust[i]) + int(timeList[i]) + myFunnyVariable)

    print(scheduledTime)

print(scheduleTimeAndDate(getCurrentTime(), 0, 20, 0))