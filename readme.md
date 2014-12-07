#Conchord
[![Build Status](https://travis-ci.org/yanhick/conchord.svg?branch=master)](https://travis-ci.org/yanhick/conchord)

A song and lyrics text format and tools for geeky songwriters.
Conchord is a line based format, with columns delimited by tabs.
It is designed to be easily manipulated with standard *nix tools.

##Spec

```
		The first line, if it only has the 3rd column is the song title
		The second line, if it only has the 3rd column is the song’s artist
		Any additional line with only the 3rd column until the songs begins is metadata
Intro:
		The first column, when it is the only one, is the part of the song (intro, verse, chorus...). It can be any arbitrary string
note:	The first column, when used with other columns can be any metadata relevant to this line
	C	The second column is the name of a chord
	Am	The third column are the lyrics which go with this chord.
	F	The 4th column represents the chord’s s guitar notes, from low to high E.	113211
	E	Open strings in chord’s notes are represented by a dash	 -221--
	E	If you’re feeling fancy, the chord suggested guitar fingerings for each string can be provided in the 5th column.	-221--	-231--
		Every column is optional, but empty lines are invalid
		You can use column optionality to represent instrumental parts of the songs:
Instrumental:
	C
	Am
	G
	F
Spoken:
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

