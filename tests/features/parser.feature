Feature: Parsing and serializing conchord format

    Scenario: Parsing

        Given I parse a valid line with chords and lyrics
        Then I should get a data structure representing the line

        Given I parse a line with a label
        Then I should get a data structure representing the label

        Given I parse a line with a chord name
        Then I should get a data structure representing the chord name

        Given I parse a line with chords notes
        Then I should get a data structure representing the notes

        Given I parse a line with chord's fingerings
        Then I should get a data structure representing the fingerings

    Scenario: Parsing errors

        Given I parse an empty line
        Then I should get error 1

        Given I parse a line with chords notes without a chord name
        Then I should get error 2

        Given I parse a line with chords fingerings without chords notes
        Then I should get error 3

        Given I parse a line with chord's notes with invalid number of notes
        Then I should get error 4

        Given I parse a line with chord's fingerings with invalid number of notes
        Then I should get error 5

        Given I parse a line with chord's notes with invalid characters
        Then I should get error 6

        Given I parse a line with chord's fingerings with invalid characters
        Then I should get error 7

        Given I parse a line with chord's fingerings not matching the chords notes
        Then I should get error 8

        Given I parse a line ending with a tab
        Then I should get error 9

    Scenario: Serializing

        Given I serialize a valid line data structure
        Then I should get a string representation of it

    Scenario: Parsing and serializing

        Given I parse a valid line
        When I serialize it
        Then I should get my initial line
