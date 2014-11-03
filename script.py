#!/usr/bin/env python

#Checks if stdin is valid openchord and output a pretty printed version on stdout

from sys import stdin
from sys import stdout
from sys import exit

#parse one line of open chord format, stop on any error
def parse(line):

    #split on double spaces
    data = line.split("  ")

    if len(data) < 2:
        exit('Missing chord name or lyrics in: ' + line)

    name = data[0].strip()
    lyrics = data[1].strip()

    #check if chord's notes are provided
    if len(data) > 2:
        notes = data[2].strip()
        if len(notes) != 6:
            exit('Not the right number of strings for the notes: ' + notes)
    else:
        notes = None

    #check if chord's fingering is provided
    if len(data) > 3:
        fingering = data[3].strip()
        if len(fingering) != 6:
            exit('Not the right number of strings for the fingering: ' + fingering)
    else:
        fingering = None

    return {
            'chord': {
                'name': name,
                'notes': notes,
                'fingering': fingering
                },
            'lyrics': lyrics
            }

#display one line of open chord format
def displayLine(parsed):
    stdout.write(" |" + parsed['chord']['name'] + "| " + parsed['lyrics'])

    #don't start a new line unless the lyrics ends with a "."
    if "." in parsed['lyrics'][-1]:
        print ""

def main():
    #initial newline
    print ""

    #parse and display each line
    for line in stdin:
        parsed = parse(line)
        displayLine(parsed)

    #final newlines
    print "\n"

main()
