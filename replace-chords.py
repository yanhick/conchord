#!/usr/bin/env python

#Replace chords in stdin with one from a provided chord file

from sys import stdin
from sys import stdout
from parser import parse
from parser import serialize

def replaceChord(line, chords):
    (errors, data) = parse(line)
    chordName = data['chord']['name']
    if chordName in chords:
        data['chord'] = chords[chordName]
    return serialize(data)

def getChords(path):
    chords = dict()
    lines = [line.strip() for line in open(path)]
    for line in lines:
        chord = getChord(line)
        chords[chord['name']] = chord

    return chords

def getChord(line):
    data = line.split('  ')

    name = data[0]
    notes = data[2]
    fingerings = data[3] if len(data) == 3 else None

    return {
            'name': name,
            'notes': notes,
            'fingerings': fingerings
            }


def main():

    chords = getChords('chords')
    for line in stdin:
        (errors, line) = replaceChord(line, chords)
        stdout.write(line)

main()
