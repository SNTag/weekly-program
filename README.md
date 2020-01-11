# weekly-program

## Description

A repository where I'll be adding programs as part of my new-years resolution: 1-2 programs a week in any language.  Preferably R, Python, or Bash.

# P1: photo-organizer

I dump all of my photos into one folder.  Using my travelling notes on when we went where in the file 'config.csv' (which is in the same folder as the photos), folders will be generated in an output location named by the city, country, and year.  symlinks to the original photos will be made inside each folder, creating a low-effort photo-organizer.

**WARNING:** Works only on linux for the time being.

##  To Use:

1. First modify the variable 'userPath' to the name of the desired output folder.  This folder has to be at path '../'.  If it does not exist, it will create one for you. 
2. Run from the directory with the unsorted photos.
