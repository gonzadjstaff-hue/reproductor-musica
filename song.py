import os
from mutagen.mp3 import MP3

class Song:
    def __init__(self, filename):
        self.filename = filename
        self.title = os.path.splitext(os.path.basename(filename))[0]
        self.duration = self.get_duration()

    def get_duration(self):
        try:
            audio = MP3(self.filename)
            return audio.info.length
        except Exception:
            return 0
