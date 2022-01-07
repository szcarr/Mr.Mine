from datetime import datetime

'''
A simple file to handle dates
File is dependent on timeHandling.py
'''

def getCurrentTime():

    '''
    Returns a string with UTC time
    Can split time by ":" to get hours,minutes,seconds separately
    '''

    splitList = getUTCtime().split(" ")
    return splitList[1]

def getDateToday():

    '''
    Returns a string with today's date in the format YYYY-MM-DD
    '''

    splitList = getUTCtime().split(" ")
    return splitList[0]

def getHoursMinutesSeconds(time):

    '''
    Parameter should be in the format HH-MM-SS

    Returns a list with the time.
    Where each value is separated.
    Index 0 = Hours.
    Index 1 = Minutes.
    Index 2 = Seconds.
    '''
    timeList = []
    for unit in str(time).split(":"):
        timeList.append(round(float(unit)))

    return timeList


def getUTCtime():

    '''
    Returns a string with current date and time
    Can split string by " " to get date and time separately
    '''

    return str(datetime.utcnow())

def getYearMonthDate(date):

    '''
    Parameter should be in the format YYYY-MM-DD

    Returns a list with the date.
    Where each value is separated.
    Index 0 = Year.
    Index 1 = Month.
    Index 2 = Day.
    '''
    date = str(date).split("-")
    dateList = []
    for numbers in date:
        dateList.append(int(numbers))

    return dateList

