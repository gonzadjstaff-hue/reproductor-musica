# 🎵 Reproductor de Música

Reproductor de música en **Python** con interfaz gráfica, desarrollado como proyecto de práctica.  
Permite explorar carpetas, reproducir canciones en formato MP3 y manejar listas de reproducción.

## 🚀 Características
- Interfaz gráfica con **Flet**.
- Reproducción de música con **Pygame.mixer**.
- Control de canciones: Play, Pause, Stop, Next, Previous.
- Guardado de la última carpeta utilizada.
- Selección de canción individual o carpeta completa.
- Cambio de tema visual (oscuro/claro).
- Empaquetado en **.exe** con instalador creado en **Inno Setup**.

## 🛠️ Tecnologías y Librerías

### Lenguaje
- Python 3.13

### Framework
- [Flet](https://flet.dev) → interfaz gráfica

### Librerías
- **pygame** → reproducción de audio  
- **mutagen** → metadatos de archivos MP3  
- **asyncio** → manejo de concurrencia  
- **Pillow** → conversión de iconos (.png → .ico)  

### Herramientas
- **PyInstaller** → generar ejecutable portable  
- **Inno Setup** → crear instalador con icono y atajos  
- **Git & GitHub** → control de versiones  

## 📦 Instalación

### Desde código fuente
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/gonzadjstaff-hue/reproductor-musica.git
   cd reproductor-musica
2. Instalar dependencias:
   pip install -r requirements.txt

3. Ejecutar el programa:
   python main.py

### Instalador para Windows
Si solo querés usar el programa, ejecutá:
   Setup-ReproductorMusica.exe
y seguí los pasos del instalador.

## 👨‍💻 Autor
**Gonzalo Garcez**  
- [LinkedIn](https://www.linkedin.com/in/gonzalo-javier-garcez/)  
- [GitHub](https://github.com/gonzadjstaff-hue)
