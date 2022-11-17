class MusicListening():
    def __init__(self):
        self.lists = []
    def add(self, tracks):
        if tracks == '':
            pass
        else:
            self.lists.append(tracks)
    def list_tracks(self):
        return self.lists
