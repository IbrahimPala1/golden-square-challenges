from lib.make_snippet import *

def test_if_string_is_no_word():
    result = make_snippet('')
    assert result == ''

def test_if_string_is_3_words(): 
    result = make_snippet('one two three')
    assert result == 'one two three'

def test_if_string_is_5_words(): 
    result = make_snippet('one two three four five')
    assert result == 'one two three four five'

def test_if_string_is_6_words(): 
    result = make_snippet('one two three four five six')
    assert result == 'one two three four five...'
def test_if_string_is_6_words(): 
    result = make_snippet('one two three four five six seven')
    assert result == 'one two three four five...'