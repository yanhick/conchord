from functools import partial

#Parse and serialize format, line by line. Use as library from other scripts

#parse one line of conchord format, make sure to lint input first.
#Returns a tuple containing all parsing errors in the first element if any and the parsed
#line in the second
def parse(line):

    #split on tabs and clean
    data = map(lambda item: item.strip() if item.strip() != '' else None, line.split('\t'))

    #field names in order
    fields = ['label', 'chord-name', 'lyrics', 'notes', 'fingerings']
    lineAsDict = dict.fromkeys(fields)

    identity = lambda item: item
    parsers = [
        identity,
        identity,
        identity,
        parseNotesOrFingerings,
        parseNotesOrFingerings
        ]

    for (field, parser, item) in zip(fields, parsers, data):
        parsed =  parser(item)
        lineAsDict[field] = parsed

    errorChecks = [
        emptyLine,
        notesWithoutName,
        fingeringsWithoutNotes,
        partial(wrongNumberOfChars, 4, 'notes'),
        partial(wrongNumberOfChars, 5, 'fingerings'),
        partial(invalidChars, 6, 'notes'),
        partial(invalidChars, 7, 'fingerings'),
        mismatchedNotesAndFingerings,
        partial(endWithTab, line)
        ]

    errors = filter(None, map(lambda errorChecks: errorChecks(lineAsDict), errorChecks))
    return (errors, lineAsDict)

def parseNotesOrFingerings(items):
    if items is None:
        return None
    notes = map(lambda item: int(item) if item.isdigit() else item, list(items))
    return map(lambda item: None if item == '-' else item, notes)

def emptyLine(line):
    error = (1, 'Empty lines are not allowed')
    return error if filter(lambda key: line[key] is not None, line) == [] else None

def notesWithoutName(line):
    error = (2, 'Chord notes are provided but the chord name is missing')
    return error if line['notes'] is not None and line['chord-name'] is None else None

def fingeringsWithoutNotes(line):
    error = (3, 'Chord fingerings are provided but not the notes')
    return error if line['fingerings'] is not None and line['notes'] is None else None

def wrongNumberOfChars(errorCode, field, line):
    error = (errorCode, 'Chord ' + field + ' must have 6 characters')
    return error if line[field] is not None and len(line[field]) != 6 else None

def invalidChars(errorCode, field, line):
    error = (errorCode, 'Chord ' + field + ' has invalid character. Authorized characters are numbers or \'-\'')
    return error if line[field] is not None and filter(lambda item: isinstance(item, int) is False and item is not None, line[field]) != [] else None

def mismatchedNotesAndFingerings(line):
    if line['notes'] is None or line['fingerings'] is None:
        return None
    error = (8, 'The chord\'s fingerings must match the chord\'s notes')
    return error if filter(lambda (note, fingering): (note is None) != (fingering is None), zip(line['notes'], line['fingerings'])) != [] else None

def endWithTab(lineAsString, line):
    if lineAsString == '':
        return None

    error = (9, 'The line should not end with a tabulation')
    return error if lineAsString[-1] == '\t' else None



#serialize one line of conchord format. Use as library from other scripts.
#Returns a tuple containing all the serializations errors in the first element if any
#and the serialized string in the second
def serialize(data):

    default = lambda el: el if el != None else ''
    serializeNotesOrFingerings = lambda item: ''.join(map(default, item) if item is not None else '')
    serializers = [
            default,
            default,
            default,
            serializeNotesOrFingerings,
            serializeNotesOrFingerings
            ]

    fields = ['label', 'chord-name', 'lyrics', 'notes', 'fingerings']
    values = map(lambda field: data.get(field, None), fields)

    #remove all trailing None (which would be converted to tabs)
    for value in reversed(values):
        if value is None:
            values.pop()
        else:
            break

    serialized = '\t'.join(map(lambda (item, serializer): serializer(item), zip(values, serializers)))

    return ([], serialized)

