from lib.reading_time import *
import pytest

def test_for_200():
    text = ' '.join(["word" for i in range(0, 200)])
    result = reading_time(text) 
    assert result == 1.0


def test_for_400():
    text = ' '.join(["word" for i in range(0, 400)])
    result = reading_time(text) 
    assert result == 2.0


def test_for_500():
    text = ' '.join(["word" for i in range(0, 500)])
    result = reading_time(text) 
    assert result == 2.5

def test_for_empty():
    with pytest.raises(Exception) as e:
        reading_time('')
    error = str(e.value)
    assert error == 'Error'