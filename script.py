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

#display all the chords used in the song
def displayChords(chords):
    print "\n"
    print "Chords used: "

    #display each chord used in the song
    for chordName, chord in chords.items():
        displayChord(chord)

#display one chord
def displayChord(chord):

    #can't display if notes not provided
    if chord['notes'] is None:
        return

    print ""
    print chord['name']

    if chord['notes'] is not None:
        for char in chord['notes']:
            print char


def main():
    #initial newline
    print ""

    #store each used chords. Key is the chord's name
    chords = dict()

    #parse and display each line
    for line in stdin:
        parsed = parse(line)
        displayLine(parsed)
        chords[parsed['chord']['name']] = parsed['chord']

    displayChords(chords)

    #final newlines
    print "\n"

main()
