from parser import parse as parseLine


#Parse a whole file of conchord format, extracting semantic such as title from
#the content and position of files
def parse(conchordFile):
    lines = map(parseLine, conchordFile.splitlines())
    return ([], {
            'title': getTitle(lines),
            'artist': getArtist(lines),
            'lines': lines,
            'parts': getRangedParts(getParts(lines)),
            'meta': getMeta(lines)
        })

#The song title is the first line of the file if it only contains lyrics
def getTitle(lines):
    if lines == []:
        return None

    firstLine = lines[0][1]
    return firstLine['lyrics'] if hasOnlyField('lyrics', firstLine) else None

#The song artist is the first line of the file if it only contains lyrics
def getArtist(lines):
    if lines == [] or len(lines) < 2:
        return None

    if getTitle(lines) is None:
        return None

    secondLine = lines[1][1]
    return secondLine['lyrics'] if hasOnlyField('lyrics', secondLine) else None

#The song meta are all lines after title and artist which contains only lyrics
#until the line where the song begins
def getMeta(lines):
    if lines == [] or len(lines) < 3:
        return []

    if getTitle(lines) is None:
        return []

    if getArtist(lines) is None:
        return []

    idx = 2
    length = len(lines)
    meta = []
    while idx < length:
        line = lines[idx][1]
        idx += 1
        if hasOnlyField('lyrics', line):
            meta.append(line['lyrics'])
        else:
            break
    return meta

#get all the parts of the song(intro, verse, chorus...)
#A line is considered a song part if it only contains a label
def getParts(lines):
    parts = []
    for idx, line in enumerate(lines):
        if hasOnlyField('label', line[1]):
            parts.append((idx, line[1]['label']))
    return parts

#Add the range (begin and end line number) for each part of the song
def getRangedParts(parts):
    length = len(parts)
    rangedParts = []
    for idx, (start, name) in enumerate(parts):
        if idx + 1 < length:
            (nextStart, nextName)= parts[idx + 1]
            rangedParts.append((name, (start, nextStart)))
        else:
            rangedParts.append((name, (start, start)))
    return rangedParts

#Wether a line has only the specified field at a non-None value
def hasOnlyField(field, line):
    filteredLine = dict((k, v) for k, v in line.iteritems() if v)
    return filteredLine.keys() == [field]
