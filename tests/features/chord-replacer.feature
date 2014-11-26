Feature: Replace/fill chord definition from a conchord file using other conchord files

    Scenario: Replacing chords

		Given I have a valid conchord line with no notes and fingerings
		When I have a data stucture representing chords with notes and fingerings
		Then I should be able to fill the notes and fingerings of the file

		Given I have a valid conchord file with chord name, notes and fingerings
		Then I should get a data structure representing those chords
