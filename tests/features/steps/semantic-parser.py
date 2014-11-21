from behave import *
from semantic_parser import parse

@given('I parse a valid conchord file with title')
def step_impl(context):
    context.chdfile = '\t\tMy title\n'

@then('I should get a data structure representing the file with title')
def step_impl(context):
    assert(parse(context.chdfile) == ([], {
        'title': 'My title',
        'artist': None,
        'parts': [],
        'meta': [],
        'lines': [([], {
            'lyrics': 'My title',
            'chord-name': None,
            'notes': None,
            'fingerings': None,
            'label': None
            })]
        }))

@given('I parse a valid conchord file with artist name')
def step_impl(context):
    context.chdfile = '\t\tMy title\n\t\tMy artist\n'

@Then('I should get a data stucture representing the file with artist name')
def step_impl(context):
    assert(parse(context.chdfile) == ([], {
        'title': 'My title',
        'artist': 'My artist',
        'parts': [],
        'meta': [],
        'lines': [([], {
            'lyrics': 'My title',
            'chord-name': None,
            'notes': None,
            'fingerings': None,
            'label': None
            }), ([], {
            'lyrics': 'My artist',
            'chord-name': None,
            'notes': None,
            'fingerings': None,
            'label': None
            })]
        }))

@given('I parse a valid conchord file with song part')
def step_impl(context):
    context.chdfile = 'My Part'

@Then('I should get a data structure representing the song part')
def step_impl(context):
    assert(parse(context.chdfile) == ([], {
            'title': None,
            'artist': None,
            'parts': [('My Part', (0, 0))],
            'meta': [],
            'lines': [([], {
                'lyrics': None,
                'chord-name': None,
                'notes': None,
                'fingerings': None,
                'label': 'My Part'
                })]
        }))

@given('I parse a valid conchord file with additional metadata')
def step_impl(context):
    context.chdfile = '\t\tMy title\n\t\tMy artist\n\t\tMy meta'

@Then('I should get a data structure representing those metadata')
def step_impl(context):
    assert(parse(context.chdfile) == ([], {
            'title': 'My title',
            'artist': 'My artist',
            'parts': [],
            'meta': ['My meta'],
            'lines': [([], {
                'lyrics': 'My title',
                'chord-name': None,
                'notes': None,
                'fingerings': None,
                'label': None
                }), ([], {
                'lyrics': 'My artist',
                'chord-name': None,
                'notes': None,
                'fingerings': None,
                'label': None
                }), ([], {
                'lyrics': 'My meta',
                'chord-name': None,
                'notes': None,
                'fingerings': None,
                'label': None
                })]
        }))

