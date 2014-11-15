Feature: Parsing and serializing conchord format

    Scenario: parse a line with a chord and lyrics
        Given I parse a valid line with chords and lyrics
        Then I should get a data structure representing the line
