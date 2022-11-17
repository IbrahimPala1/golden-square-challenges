from lib.track import Track

def test_matches_on_full_title():
    track =  Track('cat', 'dog')
    assert track.matches('cat') == True

def test_matches_on_partial_title():
    track =  Track('cat list', 'dog')
    assert track.matches('cat') == True


def test_matches_on_partial_title():
    track =  Track('cat list', 'dog')
    assert track.matches('dog') == True