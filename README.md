# weekly-program: Y2020

Author: SNTag
started on: 01-11th-2020

## Description

A repository where I'll be adding programs as part of my new-years resolution: 1-2 programs a week in any language.  Preferably R, Python, or Bash.  This does not have to mean that at the end of the year, I'll have 52 programs.  It means that I will have worked on x programs, some getting notable revisions to make them better as I learn.

# Helper-Functions

language: bash

scripts that I'm using to help organize this yearly goal.

# P1: photo-organizer

language: python

I dump all of my photos into one folder.  Using my travelling/event notes on when we went where in the file 'config.csv' (which is in the same folder as the photos), folders will be generated in an output location named by the city, country, and year.  symlinks to the original photos will be made inside each folder, creating a low-effort photo-organizer.

**WARNING:** Works only on linux for the time being.

##  To Use:

1. Modify (in the script) the variable 'userPath' to the name of the desired output folder.  This folder has to be at path '../'.  If it does not exist, it will create one for you.
2. Run from the directory with the unsorted photos.

# P2: sudoku

language: python

Working on learning pyqt5.  It will come in handy for a number of projects I plan to do downstream.  This program will display a sudoku grid and enable the user to solve it.  It is inspired by a similar project I saw on reddit.
