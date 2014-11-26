from behave import *
from chord_replacer import replaceChord
from chord_replacer import getChords

@given('I have a valid conchord line with no notes and fingerings')
def step_impl(context):
    context.line = '\tA\tLyrics'

@when('I have a data stucture representing chords with notes and fingerings')
def step_impl(context):
    context.data = {'A': {'notes': [1,2,3,4,5,6], 'fingerings':[1,2,3,4,5,6]}}

@then('I should be able to fill the notes and fingerings of the file')
def step_impl(context):
    assert(replaceChord(context.line, context.data) == '\tA\tLyrics\t123456\t123456\n')

@given('I have a valid conchord file with chord name, notes and fingerings')
def step_impl(context):
    context.chdfile = '\tA\tlyrics\t123456\t123456\n'

@then('I should get a data structure representing those chords')
def step_impl(context):
    assert(getChords([context.chdfile], dict()) == {
            'A': {'notes': [1, 2, 3, 4, 5, 6], 'fingerings': [1, 2, 3, 4, 5, 6]}
        })
