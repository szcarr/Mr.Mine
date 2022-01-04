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
    Returns a string with UTC time
    Can split time by ":" to get hours,minutes,seconds separately
    '''

    splitList = getUTCtime().split(" ")
    return splitList[1]

def alarm(hours, minutes, seconds):
    pass

print(getDateToday())