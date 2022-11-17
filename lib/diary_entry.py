class DiaryEntry():
    def __init__(self, title, contents):
        self.title = title 
        self.contents = contents 

    def format(self):
        return self.title + ": " + self.contents 

    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        words = self.contents.split()
        return len(words) / wpm

    def reading_chunk(self, wpm, minutes):
        words = self.contents.split()
        if len(words) / wpm < minutes:
           return 'yes user can read in the required number of minutes'
        else:
            return 'You havent got enough time to read all'

