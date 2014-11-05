#Parse and serialize format, line by line. Use as library from other scripts

#parse one line of conchord format, make sure to lint input first.
#Returns a tuple containing all parsing errors in the first element if any and the parsed
#line in the second
def parse(line):

    errors = list()

    #split on double spaces
    data = line.split("  ")

    if len(data) < 2:
        errors.append((1, 'Missing chord name or lyrics'))
        name = None
        lyrics = None
    else:
        name = data[0].strip()
        lyrics = data[1].strip()

    #check if chord's notes are provided
    if len(data) > 2:
        notes = map(lambda note: note if note != "-" else None, list(data[2].strip()))
        if len(notes) != 6:
            errors.append((2, 'Not the right number of strings for the notes'))
    else:
        notes = None

    #check if chord's fingerings are provided
    if len(data) > 3:
        fingerings = map(lambda fingering: fingering if fingering != "-" else None, list(data[3].strip()))
        if len(fingerings) != 6:
            errors.append((3, 'Not the right number of strings for the fingerings'))
    else:
        fingerings = None

    return (errors, {
            'chord': {
                'name': name,
                'notes': notes,
                'fingerings': fingerings
                },
            'lyrics': lyrics
            })

#serialize notes or fingerings structures
def serializeNotes(notes):
    return ''.join(map(lambda note: note if note != None else "-", notes))

#serialize one line of conchord format. Use as library from other scripts.
#Returns a tuple containing all the serializations errors in the first element if any
#and the serialized string in the second
def serialize(data):
    line = data['chord']['name'] + '  ' + data['lyrics']
    notes = data['chord']['notes']
    fingerings = data['chord']['fingerings']
    if notes is not None: line += '  ' + serializeNotes(notes)

    #fingerings use same syntax as notes
    if fingerings is not None: line += '  ' + serializeNotes(fingerings)
    return (list(), line + '\n')

