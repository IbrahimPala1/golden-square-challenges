from lib.music_listening import *

def test_empty_list():
    music  = MusicListening()
    assert music.list_tracks() == []

def test_one_music_track():
    music = MusicListening()
    music.add('justin bieber')
    assert music.list_tracks() == ['justin bieber']

def test_two_music_track():
    music = MusicListening()
    music.add('justin bieber')
    music.add('billy jean')
    assert music.list_tracks() == ['justin bieber', 'billy jean']

def test_three_music_track():
    music = MusicListening()
    music.add('justin bieber')
    music.add('billy jean')
    music.add('drake')
    assert music.list_tracks() == ['justin bieber', 'billy jean', 'drake']

def test_empty_list_and_string():
    music  = MusicListening()
    music.add('')
    assert music.list_tracks() == []


