#!/usr/bin/env python

from sys import stdin
from sys import stdout
from parser import parse
from parser import serialize
import argparse

argParser = argparse.ArgumentParser(description='Replace chords from stdin by chords in provided files')
argParser.add_argument('files', help='the files containing the replacing chords.'
        'They must be valid conchord files', nargs="+")
args = argParser.parse_args()

filePaths = args.files

#repace chord struct in parsed stdin line
def replaceChord(line, chords):
    (errors, data) = parse(line)

    if 'chord-name' not in data or data['chord-name'] is None:
        return line

    chordName = data['chord-name']
    if chordName in chords:
        for key, value in chords.items():
            data[key] = value

    (errors, serialized) = serialize(data)
    return serialized

#parse all chords in a chord file and add them to
#chord dict. Overrides any previous chord with the same
#name
def getChords(path, chords):
    lines = [line.strip() for line in open(path)]
    for line in lines:
        (errors, data) = parse(line)
        if 'chord-name' in data:
            keys = ['notes', 'fingerings']
            chord = dict()
            for key in keys:
                if key in data and data[key] is not None:
                    chord[key] = data[key]

    return chords

def main(filePaths):

    #get all chords from provided chord files
    chords = dict()
    for filePath in filePaths:
        chords = getChords(filePath, chords)

    #replace chords in all stdin, line by line
    for line in stdin:
        stdout.write(replaceChord(line, chords))

main(filePaths)
