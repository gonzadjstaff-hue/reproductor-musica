import os
import asyncio
import flet as ft
from song import Song
from player import MusicPlayer

LAST_FOLDER_FILE = "last_folder.txt"


class MusicApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Reproductor de Música"
        self.page.bgcolor = ft.Colors.BLUE_900
        self.page.window_width = 800
        self.page.window_height = 400
        self.page.padding = 20

        self.player = MusicPlayer()

        # Widgets
        self.song_info = ft.Text("No hay canciones cargadas", color=ft.Colors.WHITE, size=18)
        self.current_time_text = ft.Text("00:00", color=ft.Colors.WHITE)
        self.duration_text = ft.Text("00:00", color=ft.Colors.WHITE)
        self.progress_bar = ft.ProgressBar(value=0.0, width=500, color=ft.Colors.WHITE)

        self.play_button = ft.IconButton(
            icon=ft.Icons.PLAY_ARROW,
            on_click=self.on_play_pause,
            icon_color=ft.Colors.WHITE
        )
        self.prev_button = ft.IconButton(
            icon=ft.Icons.SKIP_PREVIOUS,
            on_click=self.on_prev,
            icon_color=ft.Colors.WHITE
        )
        self.next_button = ft.IconButton(
            icon=ft.Icons.SKIP_NEXT,
            on_click=self.on_next,
            icon_color=ft.Colors.WHITE
        )

        self.volume_slider = ft.Slider(
            min=0, max=100, value=50, width=200, on_change=self.on_set_volume
        )

        # FilePickers
        self.folder_picker = ft.FilePicker(on_result=self.open_folder)
        self.file_picker = ft.FilePicker(on_result=self.open_file)
        self.page.overlay.extend([self.folder_picker, self.file_picker])

        self.setup_ui()
        self.try_load_last_folder()

        asyncio.create_task(self.update_progress())

    def setup_ui(self):
        open_folder_btn = ft.ElevatedButton(
            "Abrir carpeta",
            icon=ft.Icons.FOLDER_OPEN,
            on_click=lambda _: self.folder_picker.get_directory_path(
                initial_directory=os.path.expanduser("~"),
                dialog_title="Selecciona una carpeta con música"
            )
        )

        open_file_btn = ft.ElevatedButton(
            "Abrir canción",
            icon=ft.Icons.MUSIC_NOTE,
            on_click=lambda _: self.file_picker.pick_files(
                allowed_extensions=["mp3"],
                allow_multiple=False
            )
        )

        fila_reproductor = ft.Row(
            [self.current_time_text, self.progress_bar, self.duration_text],
            alignment=ft.MainAxisAlignment.CENTER
        )

        fila_controles = ft.Row(
            [self.prev_button, self.play_button, self.next_button, self.volume_slider],
            alignment=ft.MainAxisAlignment.CENTER
        )

        columna = ft.Column(
            [
                ft.Row([open_folder_btn, open_file_btn], alignment=ft.MainAxisAlignment.CENTER),
                self.song_info,
                fila_reproductor,
                fila_controles
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.page.add(columna)

    # ----------------- Eventos -----------------
    def on_play_pause(self, e):
        playing = self.player.play_pause()
        self.play_button.icon = ft.Icons.PAUSE if playing else ft.Icons.PLAY_ARROW
        self.page.update()

    def on_set_volume(self, e):
        self.player.set_volume(e.control.value)

    def on_next(self, e):
        self.player.next_song()
        self.update_song_info()
        self.play_button.icon = ft.Icons.PLAY_ARROW
        self.page.update()

    def on_prev(self, e):
        self.player.prev_song()
        self.update_song_info()
        self.play_button.icon = ft.Icons.PLAY_ARROW
        self.page.update()

    # ----------------- Abrir carpeta o archivo -----------------
    def open_folder(self, e: ft.FilePickerResultEvent):
        if e.path:
            self.load_folder(e.path)
            with open(LAST_FOLDER_FILE, "w", encoding="utf-8") as f:
                f.write(e.path)

    def open_file(self, e: ft.FilePickerResultEvent):
        if e.files:
            file = e.files[0].path
            self.player.playlist = [Song(file)]
            self.player.current_song_index = 0
            self.player.load_song(0)
            self.update_song_info()
            self.page.update()

    # ----------------- Utilidades -----------------
    def load_folder(self, path):
        self.player.playlist.clear()
        for file in os.listdir(path):
            if file.lower().endswith(".mp3"):
                self.player.playlist.append(Song(os.path.join(path, file)))
        if self.player.playlist:
            self.player.current_song_index = 0
            self.player.load_song(0)
            self.update_song_info()
        else:
            self.song_info.value = "No se encontraron archivos MP3"
        self.page.update()

    def try_load_last_folder(self):
        if os.path.exists(LAST_FOLDER_FILE):
            with open(LAST_FOLDER_FILE, "r", encoding="utf-8") as f:
                last_path = f.read().strip()
            if os.path.isdir(last_path):
                self.load_folder(last_path)

    def update_song_info(self):
        if self.player.playlist:
            song = self.player.playlist[self.player.current_song_index]
            self.song_info.value = song.title
            self.duration_text.value = self.format_time(song.duration)
            self.progress_bar.value = 0.0
            self.current_time_text.value = "00:00"
        else:
            self.song_info.value = "No hay canciones cargadas"
            self.duration_text.value = "00:00"
            self.progress_bar.value = 0.0
            self.current_time_text.value = "00:00"

    def format_time(self, seconds):
        minutes, seconds = divmod(int(seconds), 60)
        return f"{minutes:02d}:{seconds:02d}"

    async def update_progress(self):
        while True:
            if self.player.playlist and not self.player.is_paused:
                current_time = self.player.get_current_time()
                song = self.player.playlist[self.player.current_song_index]
                if song.duration > 0:
                    self.progress_bar.value = current_time / song.duration
                self.current_time_text.value = self.format_time(current_time)
                self.page.update()
            await asyncio.sleep(0.3)
