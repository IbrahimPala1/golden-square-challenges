from lib.diary import Diary, DiaryEntry

def test_number_of_words_in_the_contents_for_diary_entry():
    diary = DiaryEntry('Shopping', 'apples and oranges')
    assert diary.count_words() == 3

def test_two_words_read_in_a_minute():
    diary = DiaryEntry('Shopping', 'apples and oranges alike')
    assert diary.reading_time(2) == 2

def test_if_entries_go_on_to_entries_list():
    entry = DiaryEntry('hiphop', 'hiphop is a interesting music genre')
    entry_list = Diary()
    entry_list.add(entry)
    assert entry_list



