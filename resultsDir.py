import os
import subprocess
# from sharedData import newDirName
# from sharedData import resultDirectory
# from sharedData import dirPrefix
import sharedData


def getCount():
    global newDirName,dirPath
    # Get a list of files in the resultDirectory
    dirList = os.listdir(sharedData.resultDirectory)

    # Check if files exist
    if not dirList:
        # No files found, create Scan1.txt
        sharedData.newDirName = sharedData.dirPrefix + "1" 
        # + fileExtension
    else:
        # Directories found, find the highest scan number
        
        scanNumber=0
        for dirName in dirList:
            if dirName.startswith(sharedData.dirPrefix):
                scanNumber+=1
                
        highestScanNumber = scanNumber if scanNumber>0 else 0
        
        # Create the new file with the next scan number
        sharedData.newScanNumber = highestScanNumber + 1
        
        sharedData.newDirName = sharedData.dirPrefix + "_"+str(sharedData.newScanNumber) + "_" + sharedData.dateOfScan
        print("Results will be saved in "+sharedData.newDirName+" under the Results directory.\n")

        subprocess.check_output(["mkdir", "Results/"+sharedData.newDirName]).decode()
    # Create the new file
    sharedData.dirPath = os.path.join(sharedData.resultDirectory, sharedData.newDirName)
