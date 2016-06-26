#-*- coding: utf-8 -*-
from PIL.Image import *
import ImageFilter
from scipy import signal
from scipy import misc
from scipy import ndimage
import numpy as np
import ImageDraw

from fonctions import *

"""

Code principal :
	-> prend une image et colorie en vert tout les pixels dans sa base de donnee sol (1)
	-> nettoie l'image en appliquant un filtre median (2)
	-> determine l'axe de la rue en par découpage en tranche, detection des centres de masses, puis regression lineaire (3)
	-> élargissement de la "zone rue" autours de l'axe determiné a l'étape d'avant, generation du "calque rue" (4)
	-> détermination de la "zone place de parking" autours de part et d'autre de la zone rue (5)
	-> élimination du reste de l'image avec un "calque trotoires/murs" (6)

"""

"""
					--- Options du script ---
"""

# Affichage des messages de debug
DEBUG = True

# Affichage des checkpoints
CHECKPOINT = True




"""
					--- Déclaration des variables ---
"""
# Chemin image camera
chemin_image_camera = "camera.png"

# Chemin "base de donnee" pixels sol
chemin_pixels_macadam = "macadam2.png"

# Chemin image a nettoyer
chemin_image_a_nettoyer = "1_noirOUvert"

# Chemin image nettoyee
chemin_image_nettoyee = "2_noirETvert_nettoye"

# Chemin image nettoyee avec droite
chemin_image_nettoyee_avec_droite = "3_noirETvert_nettoye_avec_droite"


# Precision du découpage en tranche de l'étape 3
nombre_de_tranches = 7



"""
					--- Code ---
"""
Checkpoint(0, CHECKPOINT)


#									(1)
# prend une image et en colorie en vert tout les pixels dans sa base de donnee sol
image_camera = Ouvrir_Image(chemin_image_camera)

# création de la base de données pixel macadam
image_pixels_macadam = Ouvrir_Image(chemin_pixels_macadam)
pixels_macadam = []
#On parcours l'image pixel par pixel, si un pixel n'est pas dans la pixels_macadam, on l'ajoute a la liste
for x in range(image_pixels_macadam.size[0]):
	for y in range(image_pixels_macadam.size[1]):
		if not (Image.getpixel(image_pixels_macadam, (x,y)) in pixels_macadam):
			pixels_macadam.append(Image.getpixel(image_pixels_macadam, (x,y)))
Debug("liste des pixels", pixels_macadam, DEBUG)

#coloration en vert des pixels de l'image qui sont reference dans pixel macadam, noir pour le reste
for x in range(image_camera.size[0]):
	for y in range(image_camera.size[1]):
		if Image.getpixel(image_camera, (x,y)) in pixels_macadam:
			Image.putpixel(image_camera, (x, y), (0,255,0))
		else :
			Image.putpixel(image_camera, (x, y), (0,0,0))
Enregistre_Image(image_camera, chemin_image_a_nettoyer)	

Checkpoint(1, CHECKPOINT)




#							(2)
# nettoie l'image en appliquant un filtre median

# generation du filtre median (on prend arbitrairement un ordre 19)
filtre_median = Genere_Filtre_Median(19, 0.1)

# chargement du calque de l'image et transformation de l'image en array
image_a_nettoyer = Ouvrir_Image(chemin_image_a_nettoyer)
calques_image_a_nettoyer = Extraire_Calque_Image(image_a_nettoyer)
array_image_a_nettoyer = Transformer_Calque_Image_en_Array(calques_image_a_nettoyer[1])

# Application du filtre
array_nettoye = Appliquer_Filtre(array_image_a_nettoyer, filtre_median)
image_nettoyee = Transforme_Array_en_Image(array_nettoye,(0,1,0))
Enregistre_Image(image_nettoyee, chemin_image_nettoyee)	

Checkpoint(2, CHECKPOINT)



#							(3)
# determine l'axe de la rue en par découpage en tranche, detection des centres de masses, puis regression lineaire (3)

liste_centre_masse = []
image_nettoyee = Ouvrir_Image(chemin_image_nettoyee)

# On decoupe l'image en tranche
for tranche in range(nombre_de_tranches):
	depart_tranche = (0, tranche*(image_nettoyee.size[1]/nombre_de_tranches))
	taille_tranche = (image_nettoyee.size[0], image_nettoyee.size[1]/nombre_de_tranches)
	tranche_image = Extraire_Bout_Image(image_nettoyee, depart_tranche, taille_tranche)
	#Pour chaque tranche on calcul le centre de masse et on l'ajoute a la liste
	calque_tranche = Extraire_Calque_Image_Sans_Alpha(tranche_image)
	array_tranche = Transformer_Calque_Image_en_Array(calque_tranche[1])
	liste_centre_masse.append(Renvoyer_Centre_de_Masse(array_tranche))
Debug("liste centre de masse", liste_centre_masse, DEBUG)
# On effectue la regression lineaire et on trace sur l'image
coeff_a, coeff_b = Regression_Lineaire(liste_centre_masse)
Trace_Droite(image_nettoyee, coeff_a, coeff_b)
Enregistre_Image(image_nettoyee, chemin_image_nettoyee_avec_droite)







