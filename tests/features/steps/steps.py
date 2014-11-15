import sys
from behave import *
from parser import parse

@given('I parse a valid line with chords and lyrics')
def step_impl(context):
    context.line = '\tAm\tmy lyrics'

@then('I should get a data structure representing the line')
def step_impl(context):
    print parse(context.line)
    assert(parse(context.line)) == ([], {
            'lyrics': 'my lyrics',
            'chord-name': 'Am',
            'notes': None,
            'fingerings': None,
            'label': None
        })

