#!/usr/bin/env python

#Replace chords in stdin with one from a provided chord files

from sys import stdin
from sys import stdout
from sys import argv
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
        (errors, data) = parse(line)
        chordName = data['chord']['name']
        chords[chordName] = data['chord']

    return chords

def main(filePath):

    chords = getChords(filePath)
    for line in stdin:
        (errors, line) = replaceChord(line, chords)
        stdout.write(line)

filePath = argv[1]
main(filePath)
