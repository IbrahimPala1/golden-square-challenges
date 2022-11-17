from lib.grammar import *
import pytest

def test_for_capital_and_fullstop():
    result = grammar('Hello, welcome home.')
    assert result == True

def test_for_capital_and_no_fullstop():
    result = grammar('Hello, welcome home,')
    assert result == False

def test_for_capital_and_no_fullstop():
    result = grammar('hello, welcome home.')
    assert result == False

def test_for_capital_and_question_mark():
    result = grammar('Hello, welcome home?')
    assert result == True

def test_for_capital_and_exclamation_mark():
    result = grammar('Hello, welcome home!')
    assert result == True
def test_for_capital_w_and_exclamation_mark():
    result = grammar('Wow, welcome home!')
    assert result == True

def test_for_error():
    with pytest.raises(Exception) as e:
        grammar('')
    error = str(e.value)
    assert error == 'Error'