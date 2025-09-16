from PIL import Image


png_file = "icono.png"
ico_file = "icono.ico"


img = Image.open(png_file)

img = img.resize((256, 256))  
img.save(ico_file)

print("✅ Icono convertido y guardado como:", ico_file)
