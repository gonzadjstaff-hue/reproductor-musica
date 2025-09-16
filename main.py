import flet as ft
from ui import MusicApp

async def main(page: ft.Page):
    MusicApp(page)

ft.app(target=main)
