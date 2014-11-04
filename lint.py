#!/usr/bin/env python

#Check validity of stdin until EOF. Exit with 0 and no message if valid

from sys import stdin
from sys import exit

def lint(line):
    #split on double spaces
    data = line.split("  ")

    if len(data) < 2:
        exit('Missing chord name or lyrics in: ' + line)

    #check if chord's notes are provided
    if len(data) > 2:
        notes = list(data[2].strip())
        if len(notes) != 6:
            exit('Not the right number of strings for the notes: ' + notes)

    #check if chord's fingerings are provided
    if len(data) > 3:
        fingerings = list(data[3].strip())
        if len(fingerings) != 6:
            exit('Not the right number of strings for the fingerings: ' + fingerings)

#lint each line until EOF
for line in stdin:
    lint(line)
