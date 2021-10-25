import pygame, time, os
pygame.init()
pygame.mixer.init()
# Creamos en una variable la ruta de nuestro archivo
musica = os.path.join(os.getcwd(), "sonidos", "music.mp3")
# validamos que el archivo exista si es a si lo lanzamos si no damos un error
if os.path.isfile(musica):
	pygame.mixer.music.load(musica)
	pygame.mixer.music.play()
	time.sleep(250)
else:
	print("El archivo no se encontró.")