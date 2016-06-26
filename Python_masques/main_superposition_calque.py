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
print str(sys.argv)
chemin_acces_photo = sys.argv[1]
image_cible = Ouvrir_Image("CAM/" + chemin_acces_photo)
image_cible = image_cible.rotate(-90)

numero_camera = int(sys.argv[2])

# On ouvre le calque
calque = Ouvrir_Image("CAM/calque" + str(numero_camera) + ".png")

# On supperpose le calque 
for x in range(image_cible.size[0]):
	for y in range(image_cible.size[1]):
		if Image.getpixel(calque, (x + 165, y + 165)) == (0, 255, 0):
			Image.putpixel(image_cible, (x, y), (0,255,0))
Enregistre_Image(image_cible, chemin_acces_photo, True)	
