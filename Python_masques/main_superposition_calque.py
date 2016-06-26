#-*- coding: utf-8 -*-
from PIL.Image import *
import ImageFilter
from scipy import signal
from scipy import misc
from scipy import ndimage
import numpy as np
import ImageDraw
import sys

from fonctions import *

"""
Code pour superposer le calque genere précedement à l'image capte par la camera
"""

# On ouvre la photo de la camera
print str(sys.argv)
chemin_acces_photo = sys.argv[1]
image_cible = Ouvrir_Image(chemin_acces_photo)

numero_camera = int(sys.argv[2])

# On ouvre le calque
calque = Ouvrir_Image("calque" + str(numero_camera) + ".png")

# On supperpose le calque 
for x in range(image_cible.size[0]):
	for y in range(image_cible.size[1]):
		if Image.getpixel(calque, (x,y)) == (0, 255, 0):
			Image.putpixel(image_cible, (x, y), (0,255,0))
Enregistre_Image(image_cible, chemin_acces_photo,True)	
