#!/usr/bin/env python

from sys import stdin
from sys import stdout
from chord_replacer import replaceChord
from chord_replacer import getChords
import argparse

argParser = argparse.ArgumentParser(description='Replace chords from stdin by chords in provided files')
argParser.add_argument('files', help='the files containing the replacing chords.'
        'They must be valid conchord files', nargs="+")
args = argParser.parse_args()

filePaths = args.files

def main(filePaths):

    #get all chords from provided chord files
    chords = dict()
    for filePath in filePaths:
        chords = getChords([line for line in open(filePath)], chords)

    #replace chords in all stdin, line by line
    for line in stdin:
        stdout.write(replaceChord(line, chords))

main(filePaths)
