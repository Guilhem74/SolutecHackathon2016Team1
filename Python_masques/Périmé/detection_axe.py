from PIL.Image import *
import ImageFilter
from scipy import signal
from scipy import misc
import numpy as np
import ImageDraw

poids_vert_vertical = 0
poids_vert_horizontal = 0


# detection de l'axe de la rue
#axe vertical
file = 'image_filtre_median.png'
camera = open(file)
largeur = camera.size[0]/3
image_verticale = new("RGB", (largeur,camera.size[1]), "blue")
draw = ImageDraw.Draw(image_verticale)
del draw
for x in range(image_verticale.size[0]):
	for y in range(image_verticale.size[1]):
		Image.putpixel(image_verticale, (x, y), Image.getpixel(camera, (x + largeur,y)))
		if Image.getpixel(camera, (x + largeur,y))[1] == 255:
			poids_vert_vertical = poids_vert_vertical + 1
image_verticale.save('image_verticale.jpg')



#axe horizontal
file = 'image_filtre_median.png'
camera = open(file)
longueur = camera.size[1]/3
image_horizontale = new("RGB", (camera.size[0],longueur), "blue")
draw = ImageDraw.Draw(image_horizontale)
del draw
for x in range(image_horizontale.size[0]):
	for y in range(image_horizontale.size[1]):
		Image.putpixel(image_horizontale, (x, y), Image.getpixel(camera, (x ,y+ longueur)))
		if Image.getpixel(camera, (x,y+longueur))[1] == 255:
			poids_vert_horizontal = poids_vert_horizontal + 1
image_horizontale.save('image_horizontale.jpg')



print "verticale : " + str(poids_vert_vertical)
print image_verticale.size
print "horizontal : " + str(poids_vert_horizontal)
print image_horizontale.size
