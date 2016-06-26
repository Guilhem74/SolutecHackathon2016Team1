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

liste_fichiers_macadam = ("base_macadam/macadam.png",)


# Filtre d'augmentation du contraste (ce filtre (avec ce jeux de coeffs) augmente 7 fois le contraste)
filtre_contraste = np.array([[0, 0, 0, 0, 0],[0, 0, -1, 0, 0],[0, -1, 5, -1, 0],[0, 0, -1, 0, 0], [0, 0, 0, 0, 0]])


def Former_Base_Donnee_Macadam(liste_fichiers_macadam):
	pixels_macadam = []
	for fichier in liste_fichiers_macadam:
		macadam = Ouvrir_Image(fichier)
		for x in range(macadam.size[0]):
			for y in range(macadam.size[1]):
				if not (Image.getpixel(macadam, (x,y)) in pixels_macadam):
					pixels_macadam.append(Image.getpixel(macadam, (x,y)))
	pickle.dump(pixels_macadam, open( "base_macadam.p", "w" ) )

Former_Base_Donnee_Macadam(liste_fichiers_macadam)

"""
def Charger_Base_Macadam():
	pixels_macadam = pickle.load( open( "base_macadam.p", "r" ) )
	return pixels_macadam


def Detecter_Macadam(pixels_macadam, image, chemin):
	for x in range(image.size[0]):
		for y in range(image.size[1]):
			if Image.getpixel(image, (x,y)) in pixels_macadam:
				Image.putpixel(image, (x, y), (0,255,0))
			else :
				Image.putpixel(image, (x, y), (0,0,0))
	Enregistre_Image(image, chemin, True)
	return image	



def Nettoyer_image(image, sortie_median, sortie_finale):
	filtre_median = Genere_Filtre_Median(19, 0.1)

	# chargement du calque de l'image et transformation de l'image en array
	image_a_nettoyer = Ouvrir_Image(chemin_image_a_nettoyer)
	calques_image_a_nettoyer = Extraire_Calque_Image(image_a_nettoyer)
	array_image_a_nettoyer = Transformer_Calque_Image_en_Array(calques_image_a_nettoyer[1])

	# Application du filtre median
	array_nettoye = Appliquer_Filtre(array_image_a_nettoyer, filtre_median)
	image_nettoyee = Transforme_Array_en_Image(array_nettoye,(0,1,0))
	Enregistre_Image(image_nettoyee, sortie_median, True)	

	#Tentatives (désespérees) d'éliminer le bruit
	# Optionnel application d'un filtre pour augmenter le contraste, on normalise par 10 au lieu de 25 pour forcer un contraste fort
	array_nettoye_contraste = Appliquer_Filtre_Normalisation(array_nettoye, filtre_contraste, 1)
	for numero_du_passage in range(21):
		array_nettoye_contraste = Appliquer_Filtre_Normalisation(array_nettoye_contraste, filtre_contraste, 1)
		array_nettoye_contraste = Appliquer_Filtre(array_nettoye_contraste, filtre_median)
	image_nettoyee_contraste = Transforme_Array_en_Image(array_nettoye_contraste,(0,1,0))
	#Enregistre_Image(image_nettoyee_contraste, chemin_image_nettoyee_contraste, IMAGES)

	# Conversion de l'image en vert OU noir
	calques_image_nettoyee_contraste = Extraire_Calque_Image_Sans_Alpha(image_nettoyee_contraste)
	image_noir_ou_vert = Binarisation_Couleur_Image(calques_image_nettoyee_contraste[1], seuil_difference_noir_vert)
	Enregistre_Image(image_noir_ou_vert, sortie_finale, True)



image = Ouvrir_Image("exemples_source/camera1.png")
image = Detecter_Macadam(Charger_Base_Macadam(), image, "raisonnement_visuel/1/1_coloriage.png")
Nettoyer_image(image, "raisonnement_visuel/1/2_median.png", "raisonnement_visuel/1/3_serie_median_contraste.png")


"""








	
	
	
