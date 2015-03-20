#Conchord
[![Build Status](https://travis-ci.org/yanhick/conchord.svg?branch=master)](https://travis-ci.org/yanhick/conchord)

A song and lyrics text format and tools for geeky songwriters.
Conchord is a line based format, with columns delimited by tabs.
It is designed to be easily manipulated with standard *nix tools.

##Spec

Conchord is parsed in 2 passes:
- by line (horizontal parsing). This validates each line. The lines know
about chord, label, text... but don’t know the about the song’s structure or metadata.
- by file (vertical parsing). Once lines are validated, the file parser makes sense of line
data to understand the structure (verse, chorus...) and metadata (title, artist...) of the song

###Line format

```
label	A	this is my line text content	-221--	-231--
```
The columns in order are:
1. Label, can be any label qualifying the line. It is optional
  examples: Title, Chorus, Verse
  regex: [A-Za-z0-9]*
2. Chord name, optional
	examples: A, Am, C
	regex: [A-G][#b]?(m|sus|add9|dim|dom)?
3. Content, text content for the line (lyrics, song title or artist...). Mandatory
	examples: my lyric matching the line chord, title of the song
	regex: .*
4. Chord’s guitar notes, from low to High E.
	Open string can be represented by ‘-’, muted string by ‘x’, and non-strummed string by ‘o’. 
	Optional. The chord name must be provided.
	examples: 123456, -2345-, xx3456
	regex: [\-xo1-6]{6}
5. Chord’s fingerings, from low to High E. Open string can be represented by ‘-’.
	Optional. Chord’s guitar notes must be provided. Fingerings must match guitar notes (e.g, an open string can’t have a fingering)
	examples: -12345, --3--1
	regex: [\-1-5]

####Empty line
Empty lines are valid. They must only contain a newline char ‘\n’ (no tabs)

###File format

The file is separated into a metadata and content section. The sections are separated by 1 empty line

####Metadata
The first section of the document is the metadata. This section ends at the first empty line.
Each line must have a label and a content.
It can be any label.
The following labels are recognised by the parser:
- Title, the title of song
- Artist, author/interpret of the song. Can be a comma separated list if multiple artists
- Album, album where the song appeared
- Year, year of song released

Any other label is stored as metadata.
The Title and Artist lines are mandatory

####Content

#####Section line

If a line has only a label, it signals a new section of the song (e.g Intro, Verse, Chorus).
It can be only label.
The following labels are recognised by the parser:
- Intro
- Verse
- Chorus
- Bridge
- Instrumental
- Outro

The section will last until the next empty line.

#####Section numbering

Any section can be numbered by separating with a ‘-’.
Examples: Verse-1, Verse-2, Outro-1, Outro-2

#####Section pointers

To prevent duplication, typically of Chorus, the label can be reused

```
Chorus
		This is my chorus

Chorus	

Verse-2
```

#####Content line

Content line must have a content, all other field are optional.


##Spec

```
Title	The line with `Title` in its first column is the title of the song. The title is in the 3rd column. The
Artist	The second line, if it only has the 3rd column is the song’s artist
Album	   Any additional line with only the 3rd column until the songs begins is metadata
Year	The year of release

Intro
		The first column, when it is the only one, is the part of the song (intro, verse, chorus...). It can be any arbitrary string
note:	The first column, when used with other columns can be any metadata relevant to this line
	C	The second column is the name of a chord
	Am	The third column are the lyrics which go with this chord.
	F	The 4th column represents the chord’s s guitar notes, from low to high E.	113211
	E	Open strings in chord’s notes are represented by a dash	 -221--
	E	If you’re feeling fancy, the chord suggested guitar fingerings for each string can be provided in the 5th column.	-221--	-231--
		Every column is optional, but empty lines are invalid
		You can use column optionality to represent instrumental parts of the songs:

Instrumental
	C
	Am
	G
	F

Spoken
		or spoken parts:
		blablabla
		blablabla

Dependencies:
		The following dependencies exists between columns:
		if the chord’s notes are provided, then the chord name should be provided
		if the chors’s fingerings are provided, then the chord notes should be provided
End:
		That’s all folk !
```

##Tools

The following tools are provided:

* lint.py
Check the validity of a conchord file
* replace-chords.py
Replace or complete song chords using other conchord files

