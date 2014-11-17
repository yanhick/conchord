Feature: Parsing and serializing a conchord file and extracting semantic values from it

    Scenario: Parsing

        Given I parse a valid conchord file with title
        Then I should get a data structure representing the file with title

        Given I parse a valid conchord file with artist name
        Then I should get a data stucture representing the file with artist name

        Given I parse a valid conchord file with song part:
        Then I should get a data structure representing the song part

        Given I parse a valid conchord file with additional metadata
        Then I should get a data structure representing those metadata
