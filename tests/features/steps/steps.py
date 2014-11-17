import sys
from behave import *
from parser import parse

@given('I parse a valid line with chords and lyrics')
def step_impl(context):
    context.line = '\tAm\tmy lyrics'

@then('I should get a data structure representing the line')
def step_impl(context):
    assert(parse(context.line)) == ([], {
            'lyrics': 'my lyrics',
            'chord-name': 'Am',
            'notes': None,
            'fingerings': None,
            'label': None
        })

@given('I parse a line with a label')
def step_impl(context):
    context.line = 'label'

@then('I should get a data structure representing the label')
def step_impl(context):
    assert(parse(context.line)) == ([], {
            'lyrics': None,
            'chord-name': None,
            'notes': None,
            'fingerings': None,
            'label': 'label'
        })

@given('I parse a line with a chord name')
def step_impl(context):
    context.line = '\tE'

@then('I should get a data structure representing the chord name')
def step_impl(context):
    assert(parse(context.line)) == ([], {
            'lyrics': None,
            'chord-name': 'E',
            'notes': None,
            'fingerings': None,
            'label': None
        })

@given('I parse a line with chords notes')
def step_impl(context):
    context.line = '\tE\t\t-221--'

@then('I should get a data structure representing the notes')
def step_impl(context):
    assert(parse(context.line)) == ([], {
            'lyrics': None,
            'chord-name': 'E',
            'notes': [None, 2, 2, 1, None, None],
            'fingerings': None,
            'label': None
        })

@given('I parse a line with chord\'s fingerings')
def step_impl(context):
    context.line = '\tE\t\t-221--\t-123--'

@then('I should get a data structure representing the fingerings')
def step_impl(context):
    assert(parse(context.line)) == ([], {
            'lyrics': None,
            'chord-name': 'E',
            'notes': [None, 2, 2, 1, None, None],
            'fingerings': [None, 1, 2, 3, None, None],
            'label': None
        })
