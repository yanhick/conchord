#!/usr/bin/env python

from sys import stdin
from sys import stdout
from parser import parse
import argparse

argParser = argparse.ArgumentParser(description='Output pretty printed version of conchord input'
        'format from stdin Output each line to stdout. Output any error to stderr')

#display one line of conchord format
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
        (errors, parsed) = parse(line)
        displayLine(parsed)
        chords[parsed['chord']['name']] = parsed['chord']

    displayChords(chords)

    #final newlines
    print "\n"

main()
