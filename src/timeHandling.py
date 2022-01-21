from datetime import datetime
import dateAndTime

def checkIfTimeRightNowHasPassedArgumentTime(date, time):

    '''
    Compares if the date and time passed as an argument is in the past.\n 
    If true:
    returns true.
    \n
    Else:
    returns false.
    \n
    Parameters:\n
    dateCompared should be passed in the format YYYY-MM-DD. 
    dateCompared should be a string. 
    \n
    timeCompared should be passed in the format HH:MM:SS. 
    timeCompared should be a string.
    '''

    dateCompared = dateAndTime.getYearMonthDate(date)
    dateNow = dateAndTime.getYearMonthDate(dateAndTime.getDateToday())

    timeCompared = dateAndTime.getHoursMinutesSeconds(time)
    timeNow = dateAndTime.getHoursMinutesSeconds(dateAndTime.getCurrentTime())

    #Checking if year month or day is
    #print(dateCompared[0], dateNow[0])
    if dateCompared[0] < dateNow[0]:
        return True

    #print(dateCompared[1], dateNow[1])
    if dateCompared[0] <= dateNow[0] and dateCompared[1] < dateNow[1]:
        return True

    #print(dateCompared[2], dateNow[2])
    if dateCompared[0] <= dateNow[0] and dateCompared[1] <= dateNow[1] and dateCompared[2] < dateNow[2]:
        return True

    #Checking time
    #print(timeCompared[0], timeNow[0])
    if dateCompared[0] <= dateNow[0] and dateCompared[1] <= dateNow[1] and dateCompared[2] <= dateNow[2] and timeCompared[0] < timeNow[0]:
        return True
    
    #print(timeCompared[1], timeNow[1])
    if dateCompared[0] <= dateNow[0] and dateCompared[1] <= dateNow[1] and dateCompared[2] <= dateNow[2] and timeCompared[0] <= timeNow[0] and timeCompared[1] < timeNow[1]:
        return True

    #print(timeCompared[2], timeNow[2])
    if dateCompared[0] <= dateNow[0] and dateCompared[1] <= dateNow[1] and dateCompared[2] <= dateNow[2] and timeCompared[0] <= timeNow[0] and timeCompared[1] <= timeNow[1] and timeCompared[2] < timeNow[2]:
        return True

    return False

def scheduleTime():
    pass

print(checkIfTimeRightNowHasPassedArgumentTime("2022-01-07", "18:20:55"))