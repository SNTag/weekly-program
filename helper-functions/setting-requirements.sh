#!/bin/bash
# File: setting-requirements
# Author: SNTagore (agenttiny@gmail.com)
# Date: 14/01/2020
# Description: Will make a list of requirements for each program.
# Usage: run bash on this script to update the requirements for all folders.

#TODO: [B] add a 'inotify' function

## Will set up the automatic process for each folder.
BASEDIR=$(dirname "$0")
echo $BASEDIR
cd $BASEDIR && cd ../
for D in */; do
    ## will generate and format requirements.txt.
    echo $D
	[ -f requirements.txt ] && rm requirements.txt
	grep -R 'import' *.py >> requirements.txt
	sed -i 's/^.*import //' requirements.txt
	sed -i 's/ as .*//' requirements.txt
done



# cd $SCRIPT
# pwd
