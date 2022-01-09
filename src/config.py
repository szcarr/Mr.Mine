import fileHandling
import os

fh = fileHandling
pathToCurrentDir = fh.getPathToCurrentDir()
splitBy = fh.detectOS()

gameVersion = 0.6

print(pathToCurrentDir)

def initialize():
    try:
        if not fh.checkIfFileExist(pathToCurrentDir + "cfg" + splitBy):

            '''
            If cfg folder does not exist the it creates the folder and adds folder user and game
            '''

            print("Could not find cfg directory in " + pathToCurrentDir)        
            print("Making cfg directory in " + pathToCurrentDir)

            fh.makeDirectory(pathToCurrentDir + "cfg" + splitBy)
            fh.makeDirectory(pathToCurrentDir + "cfg" + splitBy + "user")
            fh.makeDirectory(pathToCurrentDir + "cfg" + splitBy + "gamestage")

            fh.createFileInSpecifiedDir(pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt")
            fh.createFileInSpecifiedDir(pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt")

            #Adding values to userconfig.txt
            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt", "{Mr.Mine script by szcarr Version " + str(gameVersion) + "}\n")

            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt", "[General]\n")
            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt", "amountOfChestsToBeClicked = 10;\n")

            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt", "[Excavations]\n")
            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt", "chooseHardDifficulty = False;\n")

            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt", "[Metal Detector]\n") #Dont know
            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt", "temp = True;\n") #Dpnt know

            #Adding values to userconfig.txt
            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt", "{Mr.Mine script by szcarr Version " + str(gameVersion) + "}\n")

            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt", "[Gem Forge]\n")
            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt", "startCraftingFromRedGems = True;\n")
    except FileExistsError:
        print("Error creating file. File already exists.")