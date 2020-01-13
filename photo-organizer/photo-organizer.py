#!/usr/bin/env python3
# File: photo manager
# Author: SNTagore (agenttiny@gmail.com)
# Date: 28/12/2019
# Description: To manage my photo library.  Will sort photos by country into the appropiate category.  Tested on photos from 2019 onwards
# Usage: Simply call this program FROM THE DIRECTORY WITH UNSORTED PHOTOS.  It will read the 'config.csv' file, generate the appropiate folders under ./output/sorted (IF THEY AREN'T THERE ALREADY) and sort the photos in here into them (IF THEY AREN'T IN THERE ALREADY).  Keep note, it does not duplicate files but creates symlinks so as to reduce space consumption.
# Version: 1.0.0


# CSV file used to dictate this program need to have the following 1st line:
# City, Year, file identifier, Beginning, Ending


## modify the following line to set the output folder name
#TODO: [C] Add a user prompt for the following line?
userPath = "photostorage-sorted"

#TODO: [C] make the system robust to unknown values in CSV file.
#TODO: [C] make the system robust to files from multiple cameras (different naming conventions)


import pandas as pd
import os
import subprocess
from os import walk

## Will load & format data
fileData = pd.read_csv('./config.csv', delimiter=', ', engine="python")
#TODO: [C] can I use this as a security check for a properly configured config?
fileData['Beginning'] = fileData['Beginning'].astype(int)
fileData['Ending'] = fileData['Ending'].astype(int)

## sets up the paths
pathHomeOrig = os.getcwd()
os.chdir("../")
pathHome = os.getcwd()
pathSorted = pathHome+'/'+userPath+'/'

if os.path.isdir(pathSorted) == False:
    os.makedirs(pathSorted)

for i in range(len(fileData["City"])):
    dataNomen = fileData.iloc[i, 2]
    dataNomen = dataNomen.replace(" ", "")
    dataStart = int(fileData.iloc[i, 3])
    dataEnd = int(fileData.iloc[i, 4])
    strCity = fileData.loc[i,"City"]
    strCity = strCity.replace(" ","_")
    strYear = fileData.iloc[i,1]
    fileName = strCity + '-' + strYear
    pathHomeFiles = pathSorted + fileName

    ## handles the directories
    ## makes new dir named as described in the config.csv
    if os.path.isdir(pathHomeFiles) == False:
        os.makedirs(pathHomeFiles)

    ## Sorts photos by making symlinks into the appropiate folder as described by config.csv
    #TODO: [A] needs to remove all broken symlinks too!
    #TODO: [C] This approach will most likely only work on linux.  Try to make it universal?
    for d in range(dataStart, dataEnd+1):
        something1 = pathHomeOrig+'/'+dataNomen+str(d)+"*"
        something2 = pathHomeFiles+'/'
        bashString = str('ln -s ' + something1 + ' ' + something2)
        subprocess.call(bashString, shell = True)

    ## Cleans up the directories and removes possible broken links
    f = []
    for (dirpath, dirnames, filenames) in walk(pathSorted):
        f.extend(dirnames)
        break
    for i in f:
        os.chdir(pathSorted+'/'+i)
        subprocess.call(["find -L . -name . -o -type d -prune -o -type l -exec rm {} +"], shell = True)
