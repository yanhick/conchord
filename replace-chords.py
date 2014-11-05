#!/usr/bin/env python

#Replace chords in stdin with one from a provided chord file

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


def serialize(data):
    line = str(data['chord']['name'] + '  ' + data['lyrics'])
    if data['chord']['notes'] is not None:
        line += str(data['chord']['notes'])
    return line

def serializeNotes(notes):
    print "todo"


def replaceChord(line, chords):
    data = parse(line)
    chordName = data['chord']['name']
    if chords[chordName] is not None:
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
        line = replaceChord(line, chords)
        stdout.write(line)

main()
