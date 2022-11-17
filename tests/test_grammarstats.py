from lib.grammarstats import GrammarStats
import pytest

def test_sentence_punctuation_good():
    grammar = GrammarStats()
    result = grammar.check('Hello world.')
    assert result == True

def test_sentence_punctuation_bad():
    grammar = GrammarStats()
    result = grammar.check('Hello world,')
    assert result == False

def test_sentence_punctuation_good_with_exclamation():
    grammar = GrammarStats()
    result = grammar.check('Hello world!')
    assert result == True
    
def test_empty_text():
    grammar = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar.check('')
    error = str(e.value)
    assert error == 'Error'

def test_checks_one_correct_text():
    grammar = GrammarStats()
    grammar.check("Hello world!")
    x = grammar.percentage_good()
    assert x == 100

def test_checks_one_correct_text():
    grammar = GrammarStats()
    grammar.check("Hello world,")
    x = grammar.percentage_good()
    assert x == 0

def test_checks_one_correct_one_incorrect():
    grammar = GrammarStats()
    grammar.check("Hello world,")
    grammar.check("Hello world!")
    x = grammar.percentage_good()
    assert x == 50

def test_checks_two_correct_one_incorrect():
    grammar = GrammarStats()
    grammar.check("Hello world.")
    grammar.check("Hello world,")
    grammar.check("Hello world!")
    x = grammar.percentage_good()
    assert x == 67



   
