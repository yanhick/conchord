from parser import parse
from parser import serialize

#functions to get and replace chords in conchord data structures

#repace chord struct in parsed stdin line
def replaceChord(line, chords):
    (errors, data) = parse(line)

    if data['chord-name'] is None:
        return line

    chordName = data['chord-name']
    if chords.get(chordName, None) is not None:
        for key, value in chords[chordName].items():
            data[key] = value

    (errors, serialized) = serialize(data)
    return serialized

#parse all chords in a chord file and add them to
#chord dict. Overrides any previous chord with the same
#name
def getChords(lines, chords):
    for line in lines:
        (errors, data) = parse(line)
        if data['chord-name'] is not None:
            keys = ['notes', 'fingerings']
            chord = dict()
            for key in keys:
                if key in data and data[key] is not None:
                    chord[key] = data[key]
            chords[data['chord-name']] = chord

    return chords

