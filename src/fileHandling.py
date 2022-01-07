import os
import platform



'''
-------------------------------------------------------PROGRAMS-------------------------------------------------------
'''

#def archiveTXTfilesInknownIPs():

#def deleteTXTfilesInknownIPs():

def detectOS():
    #os detection
    splitBy = "\\"
    if str(platform.system()) == "Linux":
        splitBy = '/'
    elif str(platform.system()) == "Windows":
        splitBy = '\\'
    elif str(platform.system()) == "Darwin":
        #Darwin is macOS
        #I dont know what it's files is separeted by
        splitBy = '/'
    return splitBy

'''
-------------------------------------------------------FILES-------------------------------------------------------
'''

def checkIfFileExist(filePathAndName):
    '''
    Returns True if filename and file extension exists
    '''
    if os.path.isfile(filePathAndName):
        #File exist
        return True
    else:
        #File does not exist
        return False

def getPathToCurrentDir():
    
    '''
    Returns a string with the filepath to the directory the file was called from. \n

    Return example: /home/user/Documents/Program/Mr.Mine/src/
    '''

    pathInList = os.path.abspath(".")

    listWithPossiblePlaces = []
    fileToFind = os.path.basename(__file__)
    nameOfParentFolder = "src"

    for r,d,f in os.walk(pathInList): 
        #Gets all the places where the about.txt file could be located
        for files in f:
            if files == fileToFind:
                listWithPossiblePlaces.append(str(os.path.join(r,files)))

    splitBy = detectOS()

    actualPath = ""
    for i in range(len(listWithPossiblePlaces)):
        pathSplitted = listWithPossiblePlaces[i].split(splitBy)
        if pathSplitted[len(pathSplitted) - 1] == fileToFind and pathSplitted[len(pathSplitted) - 2] == nameOfParentFolder:
            stringConstruction = listWithPossiblePlaces[i].split(splitBy)
            for i in range(len(stringConstruction)):
                if stringConstruction[i] == fileToFind:
                    break
                actualPath = actualPath + stringConstruction[i] + splitBy

    return actualPath

def getAmountOfLinesInFile(filePathAndName):
    #nameOfFile needs to include the file extension and needs the entire path to the file
    #Example of string that can be passed as an argument
    #/home/scp092/Documents/Program/SSHBruteforce/src/usernames.txt

    file = open(filePathAndName, "r")
    line_count = 0

    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    return line_count

def makeDirectory(pathAndFolderName):
    if not checkIfFileExist(pathAndFolderName):
        #If true folder does not exist
        os.mkdir(pathAndFolderName)
    else:
        print("Folder already exists or error.")
    
def removeFile(filePathAndName):
    if os.path.exists(filePathAndName):
        os.remove(filePathAndName)
    else:
        print("Error: file: '" + filePathAndName + "' does not exist.")

'''
-------------------------------------------------------TXT HANDLING-------------------------------------------------------
'''

def readTXTFile(filePathAndName):

    '''
    Parameter should be filepath + filename + file extension
    Reads a txt file at specified location
    '''

    fileLine = open(filePathAndName)
    fileLines = fileLine.readlines()
    fileLine.close()
    return fileLines

def createFileInSpecifiedDir(filePathAndName):

    '''
    Creates a file in the specified directory
    Parameter should be filepath + name of file and file extension
    '''

    if not os.path.isfile(filePathAndName):
        #File does not exist, then creates the file
        f = open(filePathAndName, "x")
    else:    
        return -1
        #Else file already exists

def addTextToSpecifiedFile(filePathAndName, lineToAdd):
    
    '''
    Adds text to the specified file
    Does not add a linebreak to parameter string "lineToAdd"
    '''

    if os.path.isfile(filePathAndName):
        file_object = open(filePathAndName, 'a')
        # Append 'hello' at the end of file
        file_object.write(lineToAdd)
        # Close the file
        file_object.close()
    else:
        print("Could not write to specified file.")

def getLineNumberFromFile(filePathAndName, stringToSearchFor):

    '''
    Returns a list with all the places lineToSearchFor was equal to the index of the file
    Returns a list with integers
    '''

    file = readTXTFile(filePathAndName)
    splitList = []
    for line in file:
        splitList.append((line.split("\n"))[0])

    lineNumberList = []
    for i in range(len(file)):
        if str(stringToSearchFor) == str(splitList[i]):
            lineNumberList.append(i)
    
    return lineNumberList

def replaceLineInFile(filePathAndName, lineNumber, lineToAdd):

    '''
    Deletes old file and creates a new file with the wanted changes
    Remember that file has start index 0
    '''

    document = readTXTFile(filePathAndName)
    lineToAdd = lineToAdd + "\n"
    print(lineToAdd)
    for i in range(len(lineNumber)):
        document[lineNumber[i]] = lineToAdd
    
    removeFile(filePathAndName)
    createFileInSpecifiedDir(filePathAndName)
    for i in range(len(document)):
        addTextToSpecifiedFile(filePathAndName, document[i])

#replaceLineInFile("/home/scp092/Documents/Program/Mr.Mine/src/test.txt", getLineNumberFromFile("/home/scp092/Documents/Program/Mr.Mine/src/test.txt", "hola bro"), "inserta verdi")
#hei = getLineNumberFromFile("/home/scp092/Documents/Program/Mr.Mine/src/cfg/gamestage/gamestage.txt", "startCraftingFromRedGems = True;")
#print(hei)