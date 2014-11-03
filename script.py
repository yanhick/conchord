#!/usr/bin/env python

from sys import stdin
from sys import stdout
from sys import exit

def displayLine(parsed):
    stdout.write(" |" + parsed['chord']['name'] + "| " + parsed['lyrics'])
    if "." in parsed['lyrics'][-1]:
        print ""

def parse(line):
    data = line.split("  ")
    if len(data) < 2:
        exit('Missing chord name or lyrics in: ' + line)
    name = data[0].strip()
    lyrics = data[1].strip()
    if len(data) > 2:
        notes = data[2].strip()
        if len(notes) != 6:
            exit('Not the right number of strings for the notes: ' + notes)
    else:
        notes = None
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

def main():
    for line in stdin:
        parsed = parse(line)
        displayLine(parsed)
    print ""

main()
