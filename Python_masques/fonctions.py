from PIL.Image import *
import ImageFilter
from scipy import signal
from scipy import misc
from scipy import ndimage
import numpy as np
import ImageDraw

"""

Ensemble des fonctions de base utilisées dans le programme. Ces fonctions sont volontairement simple et monotaches pour pourvoir
 être réutilisés dans un maximun d'autres fonction, certaines ne sont même que des alias afin de simplifer la lecture du code.

"""


def Debug(msg, a_afficher):
	"""
	Affiche un message de debug si debug est a True sous la forme "msg", une chaine de caractere contenant l'explication
	associée a "a_afficher" qui est affiché ligne suivante.
	"""
	if DEBUG == True:
		print msg + " : " 
		print a_afficher


def Enregistre_Image(image, nom):
	"""
	Enregistre l'"image" fournie au format PIL avec le "nom" fourni au format png.
	"""
	image.save(nom, "PNG")


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
			Image.putpixel(image, (x, y), (calque[0]*array[x][y], claque[1]*array[x][y], calque[2]*array[x][y]))
	
	
