from functools import partial

#Parse and serialize format, line by line. Use as library from other scripts

#parse one line of conchord format, make sure to lint input first.
#Returns a tuple containing all parsing errors in the first element if any and the parsed
#line in the second
def parse(line):

    #split on double spaces and clean
    data = map(lambda item: item.strip() if item.strip() != '-' else None, line.split('  '))

    default = lambda field, item: (field, item, [])

    parsers = [
        partial(default, 'label'),
        partial(default, 'chord-name'),
        partial(default, 'lyrics'),
        partial(parseNotesOrFingerings, 'notes', (2, 'Not the right number of strings for the notes')),
        partial(parseNotesOrFingerings, 'fingerings', (3, 'Not the right number of strings for the fingerings'))
        ]

    return map(lambda (item, parser): parser(item), zip(data, parsers))

def parseNotesOrFingerings(field, errors, items):
    items = map(lambda item: item if item != '-' else None, list(items))
    if len(items) != 6:
        return (field, items, [error])
    return (field, items, [])

#serialize one line of conchord format. Use as library from other scripts.
#Returns a tuple containing all the serializations errors in the first element if any
#and the serialized string in the second
def serialize(data):

    default = lambda el: el if el != None else '-'
    serializeNotesOrFingerings = lambda item: ''.join(map(default), item)
    serializers = [
            default,
            default,
            default,
            serializeNotesOrFingerings,
            serializeNotesOrFingerings
            ]

    return '  '.join(map(lambda ((field, item, errors), serializer): serializer(item), zip(data, serializers)))
