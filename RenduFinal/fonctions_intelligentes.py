#-*- coding: utf-8 -*-
from PIL.Image import *
from PIL import ImageFilter
from scipy import signal
from scipy import misc
from scipy import ndimage
import numpy as np
from PIL import ImageDraw
import sys
import pickle

from fonctions import *

liste_fichiers_macadam = ("base_macadam/macadam.png","base_macadam/macadam2.png","base_macadam/macadam3.png","base_macadam/macadam11.png","base_macadam/macadam22.png","base_macadam/macadam33.png")


def Former_Base_Donnee_Macadam(liste_fichiers_macadam):
	pixels_macadam = []
	for fichier in liste_fichiers_macadam:
		macadam = Ouvrir_Image(fichier)
		for x in range(macadam.size[0]):
			for y in range(macadam.size[1]):
				if not (Image.getpixel(macadam, (x,y)) in pixels_macadam):
					pixels_macadam.append(Image.getpixel(macadam, (x,y)))
	pickle.dump( pixels_macadam, open( "base_macadam.p", "wb" ) )

#Former_Base_Donnee_Macadam(liste_fichiers_macadam)


def Charger_Base_Macadam():
	pixels_macadam = pickle.load( open( "base_macadam.p", "rb" ) )
	return pixels_macadam


def Detecter_Macadam(pixels_macadam):
	for x in range(image_camera.size[0]):
		for y in range(image_camera.size[1]):
			if Image.getpixel(image_camera, (x,y)) in pixels_macadam:
				Image.putpixel(image_camera, (x, y), (0,255,0))
			else :
				Image.putpixel(image_camera, (x, y), (0,0,0))
	Enregistre_Image(image_camera, chemin_image_a_nettoyer,IMAGES)	















	
	
	
