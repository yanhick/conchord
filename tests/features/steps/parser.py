import sys
from behave import *
from parser import parse
from parser import serialize

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

@given('I parse an empty line')
def step_impl(context):
    context.line = ''

@then('I should get error 1')
def step_impl(context):
    (errors, parsed) = parse(context.line)
    assert(errors[0][0] == 1)

@given('I parse a line with chords notes without a chord name')
def step_impl(context):
    context.line = 'label\t\tlyrics\t123456'

@then('I should get error 2')
def step_impl(context):
    (errors, parsed) = parse(context.line)
    assert(errors[0][0] == 2)

@given('I parse a line with chords fingerings without chords notes')
def step_impl(context):
    context.line = 'label\tA\tlyrics\t\t123456'

@then('I should get error 3')
def step_impl(context):
    (errors, parsed) = parse(context.line)
    assert(errors[0][0] == 3)

@given('I parse a line with chord\'s notes with invalid number of notes')
def step_impl(context):
    context.line = 'label\tA\tlyrics\t23456'

@then('I should get error 4')
def step_impl(context):
    (errors, parsed) = parse(context.line)
    assert(errors[0][0] == 4)

@given('I parse a line with chord\'s fingerings with invalid number of notes')
def step_impl(context):
    context.line = 'label\tA\tlyrics\t123456\t23456'

@then('I should get error 5')
def step_impl(context):
    (errors, parsed) = parse(context.line)
    assert(errors[0][0] == 5)

@given('I parse a line with chord\'s notes with invalid characters')
def step_impl(context):
    context.line = 'label\tA\tlyrics\tA23456'

@then('I should get error 6')
def step_impl(context):
    (errors, parsed) = parse(context.line)
    assert(errors[0][0] == 6)

@given('I parse a line with chord\'s fingerings with invalid characters')
def step_impl(context):
    context.line = 'label\tA\tlyrics\t123456\tA23456'

@then('I should get error 7')
def step_impl(context):
    (errors, parsed) = parse(context.line)
    assert(errors[0][0] == 7)

@given('I parse a line with chord\'s fingerings not matching the chords notes')
def step_impl(context):
    context.line = 'label\tA\tlyrics\t---123\t123---'

@then('I should get error 8')
def step_impl(context):
    (errors, parsed) = parse(context.line)
    assert(errors[0][0] == 8)

@given('I parse a line ending with a tab')
def step_impl(context):
    context.line = 'label\t'

@then('I should get error 9')
def step_impl(context):
    (errors, parsed) = parse(context.line)
    assert(errors[0][0] == 9)

@given('I serialize a valid line data structure')
def step_impl(context):
    context.data = {
            'lyrics': 'my lyrics',
            'chord-name': 'A',
            'notes': None,
            'fingerings': None,
            'label': None
        }

@then('I should get a string representation of it')
def step_impl(context):
    line = '\tA\tmy lyrics'
    print(serialize(context.data))
    assert(serialize(context.data)) == ([], line)

@given('I parse a valid line')
def step_impl(context):
    line = '\tA\tmy lyrics'
    context.data = parse(line)

@when('I serialize it')
def step_impl(context):
    context.line = serialize(context.data[1])

@then('I should get my initial line')
def step_impl(context):
    assert(context.line[1] == '\tA\tmy lyrics')
