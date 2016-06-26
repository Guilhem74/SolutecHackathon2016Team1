#-*- coding: utf-8 -*-
from PIL.Image import *
from PIL import ImageFilter
from scipy import signal
from scipy import misc
from scipy import ndimage
import numpy as np
from PIL import ImageDraw


"""

Ensemble des fonctions de base utilisées dans le programme. Ces fonctions sont volontairement simple et monotaches pour pourvoir
 être réutilisés dans un maximun d'autres fonction, certaines ne sont même que des alias afin de simplifer la lecture du code.

"""


def Checkpoint(numero_du_point, CHECKPOINT):
	"""
	affiche un message annoncant le succes du point spécifie ("numero_du_point")
	"""
	if CHECKPOINT == True:
		print "######################### Le checkpoint n." + str(numero_du_point) + " est franchit avec succes #########################"


def Debug(msg, a_afficher, DEBUG):
	"""
	Affiche un message de debug si debug est a True sous la forme "msg", une chaine de caractere contenant l'explication
	associée a "a_afficher" qui est affiché ligne suivante.
	"""
	if DEBUG == True:
		print "--- " + msg + " --- " 
		print a_afficher


def Enregistre_Image(image, nom, IMAGES):
	"""
	Enregistre l'"image" fournie au format PIL avec le "nom" fourni au format png.
	"""
	if IMAGES == True :
		image.save(nom)


def Ouvrir_Image(chemin_fichier):
	"""
	Ouvre et retourne l'image indiqué par le "chemin_fichier" au format PIL.
	"""
	file = chemin_fichier
	image = open(file)
	return image


def Extraire_Bout_Image(image, depart_bout, taille_bout):
	"""
	Retourne une image de "taille_bout", un tuple contenant largeur et longueur extraite depuis "image", une image PIL, a partir du point
	de coordonne "depart_bout", un autre tuple.
	"""
	bout_image = new("RGB", (taille_bout), "blue")
	draw = ImageDraw.Draw(bout_image)
	del draw
	for x in range(bout_image.size[0]):
		for y in range(bout_image.size[1]):
			Image.putpixel(bout_image, (x, y), Image.getpixel(image, (x + depart_bout[0], y + depart_bout[1])))
	return bout_image


def Extraire_Calque_Image(image):
	"""
	Renvoi les 3~4 calques r,g,b,a de l'"image".
	"""
	r, g, b, a = image.split()  
	return r,g,b,a


def Extraire_Calque_Image_Sans_Alpha(image):
	"""
	Renvoi les 3~4 calques r,g,b,a de l'"image".
	"""
	r, g, b = image.split()  
	return r,g,b



def Transformer_Calque_Image_en_Array(calque_image):
	"""
	Retourne un array contenant les valeurs de couleur de pixel de "calque_image".
	"""
	array = np.zeros(calque_image.size)
	for x in range(calque_image.size[0]):
		for y in range(calque_image.size[1]):
			array[x, y] = Image.getpixel(calque_image, (x, y))
	return array


def Renvoyer_Centre_de_Masse(array):
	"""
	Renvoie les coordonnées du centre de masse de l'"array" envoyé sous forme d'entiers
	"""
	coordonnee_centre_de_masse = ndimage.measurements.center_of_mass(array)
	return (int(coordonnee_centre_de_masse[0]), int(coordonnee_centre_de_masse[1]))
	

def Inverser_Image(image, couleur1, couleur2):
	"""
	Inverse les "couleur1" et "couleur2" (format (r, g, b) )d'une "image" (format PIL) et retourne l'image inversée
	"""
	image_inverse = new("RGB", image.size, "blue")
	draw = ImageDraw.Draw(image_inverse)
	del draw
	for x in range(image.size[0]):
		for y in range(image.size[1]):
			if Image.getpixel(image, (x,y)) == couleur1:
				Image.putpixel(image_inverse, (x, y), couleur2)
			elif Image.getpixel(image, (x,y)) == couleur2:
				Image.putpixel(image_inverse, (x, y), couleur1)
	return image_inverse


def Appliquer_Filtre(matrice, filtre):
	"""
	Applique le "filtre", un array numpy a la matrice (array numpy) d'une image en faisant un produit de convolution
	"""
	matrice_resultat = signal.convolve2d(matrice, filtre)
	nbr_coeffs_dans_filtre = filtre.shape[0]*filtre.shape[1]
	matrice_resultat = matrice_resultat/nbr_coeffs_dans_filtre
	return matrice_resultat


def Appliquer_Filtre_Normalisation(matrice, filtre, coeff_normalisation):
	"""
	Applique le "filtre", un array numpy a la matrice (array numpy) d'une image en faisant un produit de convolution
	en fixant le coeff de normalisation
	"""
	matrice_resultat = signal.convolve2d(matrice, filtre)
	nbr_coeffs_dans_filtre = filtre.shape[0]*filtre.shape[1]
	matrice_resultat = matrice_resultat/coeff_normalisation
	# Securite en cas de coeff de normalisation insuffisasnte
	for x in range(matrice_resultat.shape[0]):
		for y in range(matrice_resultat.shape[1]):
			if matrice_resultat[x][y] > 255:
				matrice_resultat[x][y] = 255
	return matrice_resultat


def Transforme_Array_en_Image(array, calque):
	"""
	Prend un "array" et le transforme en image au format PIL. La couleur est appliqué au calque indiqué par 
	calque au format (0,1,0) pour écrire sur le calque vert par exemple
	"""
	image = new("RGB", array.shape, "blue")
	draw = ImageDraw.Draw(image)
	del draw
	for x in range(array.shape[0]):
		for y in range(array.shape[1]):
			Image.putpixel(image, (x, y), (int(calque[0]*array[x][y]), int(calque[1]*array[x][y]), int(calque[2]*array[x][y])))
	return image


def Genere_Filtre_Median(ordre, coeff_central):
	"""
	Génere un array correspondant à un filtre median de l'ordre precise
	"""
	if ordre%2 == 0:
		ordre = ordre+1
	array = np.ones((ordre,ordre))
	array[ordre/2][ordre/2]
	return array
	

def Regression_Lineaire(liste_points):
	"""
	Effectue une regression linéaire sur l'ensemble des points de "liste_points" et recherche une droite de la forme y = a.x + b
	et retourne	les coefficients a et b
	"""
	liste_points_x = []
	liste_points_y = []
	for point in liste_points:
		liste_points_x.append(point[0])
		liste_points_y.append(point[1])
	array_points_x = np.asarray(liste_points_x)
	array_points_y = np.asarray(liste_points_y)
	array_pour_regression = np.vstack([array_points_x, np.ones(len(array_points_x))]).T
	coeff_a, coeff_b = np.linalg.lstsq(array_pour_regression, array_points_y)[0]
	return coeff_a, coeff_b
	
	
def Trace_Droite(image, coeff_a, coeff_b):
	"""
	Trace une droit d'équation y = "coeff_a" * x + "coeff_b" sur l'"image"
	"""
	draw = ImageDraw.Draw(image)
	draw.line((0, coeff_b) + (image.size[0], image.size[0]*coeff_a + coeff_b), fill="red")
	del draw
	return image
	
	
def Binarisation_Couleur_Image(calque_image, seuil):
	"""
	Transforme une image ne noir et une couleur en noir ou la couleur. 
	"""
	image_binaire = new("RGB", calque_image.size, "blue")
	draw = ImageDraw.Draw(image_binaire)
	del draw
	for x in range(calque_image.size[0]):
		for y in range(calque_image.size[1]):
			if Image.getpixel(calque_image, (x,y)) > seuil :
				Image.putpixel(image_binaire, (x, y), (0, 255, 0))
			else :
				Image.putpixel(image_binaire, (x, y), (0, 0, 0))
	return image_binaire
	

def Nombre_Pixels_Noir_Bande(image_binaire, point_de_depart, distance, largeur_bande):
	"""
	Determine le nombre de pixels verts dans une bande situe a "distance" du "point_de_depart"
	"""
	nombre_de_pixels_noir = 0
	haut_bande_y = point_de_depart[1]-largeur_bande/2
	for pixel in range(largeur_bande):
#		if haut_bande_y + pixel > image_binaire.size[1]:
#			bande_y = image_binaire.size[1]
#		else :
#			bande_y = haut_bande_y + pixel
		if Image.getpixel(image_binaire, (point_de_depart[0] + distance, haut_bande_y + pixel)) == (0, 0, 0):
			nombre_de_pixels_noir = nombre_de_pixels_noir + 1
	return nombre_de_pixels_noir
	
