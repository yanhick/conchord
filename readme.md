#Conchord

A text based format to represent a song's chords and lyrics.

```
C  This is the beginning of the song,
Am  each line must have the chord in the first column and the lyrics in the second one.
G  Columns are separated by 2 spaces. Not 3. Certainly not 1, but 2.
F  Optionally, the chord guitar notes can be provided in the third column, from low to high E.  113211
E  Open strings are represented by a dash  -221--
E  If you’re feeling fancy, the chord suggested guitar fingering for each string can be provided in the 4th column.  -221--  -231--
```

* Empty lines are not allowed
* Metadata (song name, artist name...) are not included to preserve ease of parsing

That’s all folks !

##Tools

This format is designed to be easily manipulated using standard Unix tools (cat, grep, awk, less...)
The following additional tools are provided:

##Workflows


