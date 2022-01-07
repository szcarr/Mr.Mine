import fileHandling

fh = fileHandling
pathToCurrentDir = fh.getPathToCurrentDir()
splitBy = fh.detectOS()

gameVersion = 0.6

def initialize():
    if not fh.checkIfFileExist(pathToCurrentDir + "cfg" + splitBy):

        '''
        If cfg folder does not exist the it creates the folder and adds folder user and game
        '''

        print("Could not find cfg directory in " + pathToCurrentDir)        
        print("Making cfg directory in " + pathToCurrentDir)

        fh.makeDirectory(pathToCurrentDir + "cfg")
        fh.makeDirectory(pathToCurrentDir + "cfg" + splitBy + "user")
        fh.makeDirectory(pathToCurrentDir + "cfg" + splitBy + "gamestage")

        fh.createFileInSpecifiedDir(pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt")
        fh.createFileInSpecifiedDir(pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt")

        #Adding values to userconfig.txt
        fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt", "{Mr.Mine script by szcarr Version " + str(gameVersion) + "}\n")

        fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt", "[Excavations]\n")
        fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "user" + splitBy + "userconfig.txt", "chooseHardDifficulty = False;\n")
        
        
        
        fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt", "{Mr.Mine script by szcarr Version " + str(gameVersion) + "}\n")

        fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt", "[Gem Forge]\n")
        fh.addTextToSpecifiedFile(pathToCurrentDir + "cfg" + splitBy + "gamestage" + splitBy + "gamestage.txt", "startCraftingFromRedGems = True;\n")


