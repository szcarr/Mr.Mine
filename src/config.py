import fileHandling
import positionsAndResolution

fh = fileHandling
positions = positionsAndResolution.positions

pathToCurrentDir = fh.getPathToCurrentDir()
splitBy = fh.detectOS()

programVersion = 0.7

print(pathToCurrentDir)

def initialize():
    try:
        if not fh.checkIfFileExist(pathToCurrentDir + "cfg"):

            '''
            If cfg folder does not exist the it creates the folder and adds folder user and game
            '''

            print("Could not find cfg directory in " + pathToCurrentDir)        
            print("Making cfg directory in " + pathToCurrentDir)

            fh.makeDirectory(pathToCurrentDir + "cfg" + splitBy)
            fh.makeDirectory(pathToCurrentDir + "cfg" + splitBy + "user")
            fh.makeDirectory(pathToCurrentDir + "cfg" + splitBy + "gamestage")

            fh.createFileInSpecifiedDir(positions.userconfigFile)
            fh.createFileInSpecifiedDir(positions.gamestageFile)

            #Adding values to userconfig.txt
            fh.addTextToSpecifiedFile(positions.userconfigFile, "{Mr.Mine script by szcarr Version " + str(programVersion) + "}\n")

            fh.addTextToSpecifiedFile(positions.userconfigFile, "[General]\n")
            fh.addTextToSpecifiedFile(positions.userconfigFile, "amountOfChestsToBeClicked = 10;\n")
            fh.addTextToSpecifiedFile(positions.userconfigFile, "goldchestDetection = False;\n")

            fh.addTextToSpecifiedFile(positions.userconfigFile, "[Excavations]\n")
            fh.addTextToSpecifiedFile(positions.userconfigFile, "chooseHardDifficulty = False;\n")

            fh.addTextToSpecifiedFile(positions.userconfigFile, "[Metal Detector]\n") #Dont know
            fh.addTextToSpecifiedFile(positions.userconfigFile, "compressToGoldChest = False;\n") #Dpnt know

            #Adding values to gamestage.txt
            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt", "{Mr.Mine script by szcarr Version " + str(programVersion) + "}\n")

            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt", "[Gem Forge]\n")
            fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt", "startCraftingFromRedGems = True;\n")

    except FileExistsError:
        print("Error creating file. File already exists.")