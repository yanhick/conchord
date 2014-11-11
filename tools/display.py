#!/usr/bin/env python

from sys import stdin
from sys import stdout
from parser import parse
import argparse

argParser = argparse.ArgumentParser(description='Output pretty printed version of conchord input'
        'format from stdin Output each line to stdout. Output any error to stderr')

#display one line of conchord format
def displayLine(line):

    if 'label' in line and line['label'] is not None:
        stdout.write('\n' + line['label'] + '\n')

    if 'chord-name' in line and line['chord-name'] is not None:
        stdout.write(' |' + line['chord-name'] + '| ')

    if 'lyrics' in line and line['lyrics'] is not None:
        stdout.write(line['lyrics'])
        #don't start a new line unless the lyrics ends with a '.'
        if '.' in line['lyrics'][-1]:
            print ''

#display all the chords used in the song
def displayChords(chords):
    print '\n'
    print 'Chords used: '

    #display each chord used in the song
    for chordName, chord in chords.items():
        displayChord(chord)

#display one chord
def displayChord(chord):

    #can't display if name not provided
    if 'chord-name' not in chord or chord['chord-name'] is None:
        return

    #can't display if notes not provided
    if 'notes' not in chord or chord['notes'] is None:
        return

    print ''
    print chord['chord-name']

    zippedChord = zip(
            reversed(['e', 'a', 'd', 'g', 'b', 'E']),
            chord['notes'],
            chord['fingerings'] if 'fingerings' in chord and chord['fingerings'] is not None else [None for i in range(6)]
            )

    for string, note, fingering in zippedChord:
        line = list('------------------------')
        if note is not None:
            line[int(note)] = 'x' if fingering is None else fingering
        print string + ' ' + ''.join(line)

def main():
    #initial newline
    print ''

    #store each used chords. Key is the chord's name
    chords = dict()

    #parse and display each line
    for line in stdin:
        parsed = parse(line)
        typed = dict()
        for (field, item, errors) in parsed:
            typed[field] = item

        displayLine(typed)

        if 'chord-name' in typed:
            chords[typed['chord-name']] = typed

    displayChords(chords)

    #final newlines
    print '\n'

main()
