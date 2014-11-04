#!/usr/bin/env python

#Checks if stdin is valid openchord and output a pretty printed version on stdout

from sys import stdin
from sys import stdout

#parse one line of open chord format, make sure to lint input first
def parse(line):

    #split on double spaces
    data = line.split("  ")

    name = data[0].strip()
    lyrics = data[1].strip()

    #check if chord's notes are provided
    if len(data) > 2:
        notes = map(lambda note: note if note != "-" else None, list(data[2].strip()))
    else:
        notes = None

    #check if chord's fingerings are provided
    if len(data) > 3:
        fingerings = map(lambda fingering: fingering if fingering != "-" else None, list(data[3].strip()))
    else:
        fingerings = None

    return {
            'chord': {
                'name': name,
                'notes': notes,
                'fingerings': fingerings
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

    zippedChord = zip(
            ['e', 'a', 'd', 'g', 'b', 'E'],
            chord['notes'],
            chord['fingerings'] if chord['fingerings'] is not None else [None for i in range(6)]
            )

    for string, note, fingering in zippedChord:
        line = list("------------------------")
        if note is not None:
            line[int(note)] = 'x' if fingering is None else fingering
        print "".join(line)

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
