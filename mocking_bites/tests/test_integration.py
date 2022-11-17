from lib.music_library import MusicLibrary
from lib.track import Track
import pytest

def test_adds_and_lists_tracks():
    library = MusicLibrary()
    track_1 = Track('My Title 1', 'My artits 1')
    track_2 = Track('My Title 2', 'My artits 2')
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]

def test_adds_and_lists_track():
    library = MusicLibrary()
    track_1 = Track('Dog', 'Cat')
    track_2 = Track('Frog', 'Toad')
    library.add(track_1)
    library.add(track_2)
    assert library.search('Dog') == [track_1]



