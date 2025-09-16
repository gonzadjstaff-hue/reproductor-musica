import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.playlist = []
        self.current_song_index = 0
        self.is_paused = True
        self.volume = 0.5
        pygame.mixer.music.set_volume(self.volume)

    def load_song(self, index):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[index].filename)

    def play_pause(self):
        if not self.playlist:
            return False
        if pygame.mixer.music.get_busy() and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
        else:
            if self.is_paused:
                if pygame.mixer.music.get_pos() == -1:
                    self.load_song(self.current_song_index)
                pygame.mixer.music.play()
                self.is_paused = False
        return not self.is_paused

    def next_song(self):
        if not self.playlist:
            return
        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        self.load_song(self.current_song_index)
        self.is_paused = True  # 👈 no arranca sola

    def prev_song(self):
        if not self.playlist:
            return
        self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
        self.load_song(self.current_song_index)
        self.is_paused = True  # 👈 no arranca sola

    def set_volume(self, value):
        self.volume = value / 100
        pygame.mixer.music.set_volume(self.volume)

    def get_current_time(self):
        pos = pygame.mixer.music.get_pos() / 1000
        return max(pos, 0)
