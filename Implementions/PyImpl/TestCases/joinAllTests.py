

import os 

testsFolder = os.path.dirname(os.path.realpath(__file__))

filesInThisFolder = os.listdir(testsFolder)

allCombinedFilesContentFile = "__all.py"
allCombinedFilesContent = ""
blacklistedTestFiles = ["_atoms.py", "_all.py", "__all.py"]
testFilesExtension = "py"

for x in range(10):
    for file in filesInThisFolder:
        if file[0] == "_" and file[-2::] == testFilesExtension and file not in blacklistedTestFiles:
            readFile = open(f"{testsFolder}\\{file}" ,"r")
            allCombinedFilesContent += f"\n\n################################# {file} Tests: ###########################\n{readFile.read()}"
            readFile.close()
    allCombinedFilesContent += "\n\n\n"

allCombinedFile = open(f"{testsFolder}\\{allCombinedFilesContentFile}" ,"a+")
allCombinedFile.write(allCombinedFilesContent)
print(testsFolder, allCombinedFilesContent)