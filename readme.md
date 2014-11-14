#Conchord

A song and lyrics text format and tools for geeky songwriters.

```

		Conchord is a line based format, with columns delimited by tabs
		It is designed to be easily manipulated with standard *nix tools
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
	C
	Am
	G
	F
		or spoken parts:
		blablabla
		blablabla
Dependencies:
		The following dependencies exists between columns:
		if the chord’s notes are provided, then the chord name should be provided
		if the chors’s fingerings are provided, then the chord notes should be provided
Misc:
		There is no definition for metadata (song name, artist...). It can be put in the first or third column or in the name of the file
		That’s all folk !
```

##Tools

The following tools are provided:

* display.py
Print a prettier version of a conchord file
* lint.py
Check the validity of a conchord file
* replace-chords.py
Replace or complete song chords using other conchord files

