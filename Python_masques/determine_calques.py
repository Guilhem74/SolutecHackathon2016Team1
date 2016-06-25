#-*- coding: utf-8 -*-

from PIL.Image import *
import ImageFilter
from scipy import signal
from scipy import misc
import numpy as np
import ImageDraw


DEBUG = True

# Définitions de fonctions

# Affiche des informations utile pour le debug si DEBUG est a true
def debug(msg,a_afficher):
	if DEBUG == True:
		print msg + " : " 
		print a_afficher




# ouverture image camera
file = 'camera.png'
camera = open(file)


# ouverture échantillon de sol
file  = 'macadam.png'
macadam = open(file)

# création de la base de données pixel macadam
pixels_macadam = []
for x in range(macadam.size[0]):
	for y in range(macadam.size[1]):
		if not (Image.getpixel(macadam, (x,y)) in pixels_macadam):
			pixels_macadam.append(Image.getpixel(macadam, (x,y)))
debug("liste des pixels", pixels_macadam)


# détection des pixels "macadam" dans l'image et passage de l'image en noir OU vert
for x in range(camera.size[0]):
	for y in range(camera.size[1]):
		if Image.getpixel(camera, (x,y)) in pixels_macadam:
			Image.putpixel(camera, (x, y), (0,255,0))
		else :
			Image.putpixel(camera, (x, y), (255,255,255))
camera.save('noirOUvert.jpg')	


# Définition du filtre median pour "nettoyer" l'image 
matrice_median = np.array([[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,0.1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1]])

# mise en forme de l'image comme array numpy (on ne prend que le calque vert)
r,g,b,a = camera.split() 
array_camera_vert = np.zeros(camera.size)
for x in range(camera.size[0]):
	for y in range(camera.size[1]):
		array_camera_vert[x,y] = Image.getpixel(r, (x,y))
# produit de convolution
convol = signal.convolve2d(array_camera_vert,matrice_median)
convol = convol/9
debug("convolution effectue",convol)

# création d'une image vide dans laquelle on met l'image apres etre passe par le filtre médian
image_filtre_median = new("RGB", camera.size, "blue")
draw = ImageDraw.Draw(image_filtre_median)
del draw
for x in range(camera.size[0]):
	for y in range(camera.size[1]):
		Image.putpixel(image_filtre_median, (x, y), (0,int(convol[x][y]),0))
image_filtre_median.save("image_filtre_median.png", "PNG")


# creation d'une image avec la rue en vert
file = 'camera.png'
camera = open(file)
file = 'image_filtre_median.png'
image_filtre_median = open(file)
for x in range(camera.size[0]):
	for y in range(camera.size[1]):
		if not (Image.getpixel(image_filtre_median, (x,y))[1] ==  255):
			Image.putpixel(camera, (x, y), (0,255,0))
camera.save('couleurOUvert.jpg')

