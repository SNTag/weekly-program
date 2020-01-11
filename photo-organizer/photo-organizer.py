#!/usr/bin/env python3
# File: photo manager
# Author: SNTagore (agenttiny@gmail.com)
# Date: 28/12/2019
# Description: To manage my photo library.  Will sort photos by country into the appropiate category.  Tested on photos from 2017 onwards
# Usage: Simply call this program FROM THE DIRECTORY WITH UNSORTED PHOTOS.  It will read the 'readme.md' file, generate the appropiate folders under ../photostorage-jpg (IF THEY AREN'T THERE ALREADY) and sort the photos in here into them (IF THEY AREN'T IN THERE ALREADY)


import pandas as pd
import os
import subprocess

# TODO: Add confirmation message for the directory to be run from.
## Setting the dir for now
# TODO: highlight the line below
os.chdir("/media/iDropbox/Dropbox/photos/photography/processing-tools/input/test-data/")

## Will load & format data
fileData = pd.read_csv('readme.csv', delimiter=', ', engine="python")
fileData['Beginning'] = fileData['Beginning'].astype(int)  # can I use this as a security check for a properly configured readme?
fileData['Ending'] = fileData['Ending'].astype(int)
## handles the directories
## makes new dir named as described in the readme.csv
# TODO: Confirm that wd is set to the directory it is run from when running from shell
pathOrig = os.getcwd()
pathData = "/media/iDropbox/Dropbox/photos/photography/processing-tools/input/sorted/"
for i in range(len(fileData["City"])):
    strCity = fileData.iloc[i,0]
    strCity = strCity.replace(" ","_")
    strYear = fileData.iloc[i,1]
    pathModif = pathData + '/' + strCity + strYear
    if os.path.isdir(pathModif) == False:
        os.makedirs(pathModif)


#----------|sort pics|----------#
# TODO

for i in range(len(fileData["City"])):
    dataNomen = fileData.iloc[i, 2]
    dataNomen = dataNomen.replace(" ", "")
    dataStart = int(fileData.iloc[i, 3])
    dataEnd = int(fileData.iloc[i, 4])
    strCity = fileData.loc[i,"City"]
    strCity = strCity.replace(" ","_")
    x = str(dataStart + 1)

    for d in range(dataStart, dataEnd):
        if dataStart != ' NA':
            dataStart = dataStart - 1
            if dataEnd != ' NA':
                subprocess.call(['ln','-s',pathOrig+dataNomen+x,pathData+dataNomen+x], shell = False)
                x = str(int(x) + 1)
