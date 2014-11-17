from functools import partial

#Parse and serialize format, line by line. Use as library from other scripts

#parse one line of conchord format, make sure to lint input first.
#Returns a tuple containing all parsing errors in the first element if any and the parsed
#line in the second
def parse(line):

    #split on tabs and clean
    data = map(lambda item: item.strip() if item.strip() != '' else None, line.split('\t'))

    default = lambda item: ([], item)

    parsers = [
        default,
        default,
        default,
        partial(parseNotesOrFingerings, (2, 'Not the right number of strings for the notes')),
        partial(parseNotesOrFingerings, (3, 'Not the right number of strings for the fingerings'))
        ]

    fields = ['label', 'chord-name', 'lyrics', 'notes', 'fingerings']
    lineAsDict = dict.fromkeys(fields)

    errors = []
    for (field, parser, item) in zip(fields, parsers, data):
        (parsingErrors, parsed) =  parser(item)
        errors += parsingErrors
        lineAsDict[field] = parsed

    return (errors, lineAsDict)

def parseNotesOrFingerings(error, items):
    if items is None:
        return ([], None)

    items = map(lambda item: int(item) if item != '-' else None, list(items))
    if len(items) != 6:
        return ([error], items)
    return ([], items)

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

    serialized = '\t'.join(map(lambda (item, serializer): serializer(item), zip(values, serializers)))

    return ([], serialized + '\n')

