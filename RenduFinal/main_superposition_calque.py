#-*- coding: utf-8 -*-
from PIL.Image import *
from PIL import ImageFilter
from scipy import signal
from scipy import misc
from scipy import ndimage
import numpy as np
from PIL import ImageDraw
import sys

from fonctions import *

"""
Code pour superposer le calque genere précedement à l'image capte par la camera

!!!!!!!!!!!!!!!!!!!!!!! Attention a l'offset, il faudra verifier qu'il est toujours bon dan sla derniere version
"""

# On ouvre la photo de la camera

chemin_acces_photo = sys.argv[1]
image_cible = Ouvrir_Image(chemin_acces_photo)
#image_cible = image_cible.rotate(-90)
#image_cible.save("asuprimer.png")

print( sys.argv)

numero_camera = int(sys.argv[2])
#numero_camera=1
# On ouvre le calque
calque = Ouvrir_Image("CAM/calque" + str(numero_camera) + ".png")

	
# On supperpose le calque 
for x in range(image_cible.size[0]):
	for y in range(image_cible.size[1]):
		if Image.getpixel(calque, (x+9 , y+9 )) == (0, 255, 0):
			Image.putpixel(image_cible, (x, y), (0,255,0))
image_cible.save("cible.png")
Enregistre_Image(image_cible, chemin_acces_photo, True)

