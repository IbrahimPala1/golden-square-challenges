from lib.diary_entry import DiaryEntry

def test_formats_with_title_and_contents():
   diary = DiaryEntry('Title', 'Contents')
   result = diary.format()
   assert result == "Title: Contents"

def test_returns_number_of_words():
   diary = DiaryEntry('Title', 'Contents')
   result = diary.count_words()
   assert result == 2

def test_reading_time():
   diary = DiaryEntry('Title', 'Contents and such things')
   result = diary.reading_time(2)
   assert result == 2

def test_reading_time_for_more():
   diary = DiaryEntry('Title', 'Contents and such things and others')
   result = diary.reading_time(2)
   assert result == 3

def test_user_can_read_in_the_number_of_minutes():
   diary = DiaryEntry('Title', 'Contents and such things and others')
   result = diary.reading_chunk(4, 2)
   assert result == 'yes user can read in the required number of minutes'

def test_user_cannot_read_in_the_number_of_minutes():
   diary = DiaryEntry('Title', 'Contents and such things and others also other things and then others')
   result = diary.reading_chunk(4, 2)
   assert result == 'You havent got enough time to read all'