from PIL.Image import *
import ImageFilter
from scipy import signal
from scipy import misc
from scipy import ndimage
import numpy as np
import ImageDraw


#axe horizontal
file = 'image_filtre_median.png'
camera = open(file)
for x in range(camera.size[0]):
	for y in range(camera.size[1]):
		if Image.getpixel(camera, (x,y)) == (0,255,0):
			Image.putpixel(camera, (x, y), (0,0,0))
		elif Image.getpixel(camera, (x,y)) == (0,0,0):
			Image.putpixel(camera, (x, y), (0,255,0))
camera.save("image_filtre_median_inverse.png")
longueur = camera.size[1]/6
image_horizontale = new("RGB", (camera.size[0],longueur), "blue")
draw = ImageDraw.Draw(image_horizontale)
del draw
for x in range(image_horizontale.size[0]):
	for y in range(image_horizontale.size[1]):
		Image.putpixel(image_horizontale, (x, y), Image.getpixel(camera, (x ,y)))
image_horizontale.save('image_horizontale_haut.jpg')
r,g,b = image_horizontale.split() 
array_image = np.zeros(image_horizontale.size)
for x in range(image_horizontale.size[0]):
	for y in range(image_horizontale.size[1]):
		array_image[x,y] = Image.getpixel(g, (x,y))
print array_image
coordonnee_centre_de_masse_haut = ndimage.measurements.center_of_mass(array_image)
print (int(coordonnee_centre_de_masse_haut[0]),int (coordonnee_centre_de_masse_haut[1]))
Image.putpixel(camera, (int(coordonnee_centre_de_masse_haut[0]),int (coordonnee_centre_de_masse_haut[1])), (255,0,0))


image_horizontale = new("RGB", (camera.size[0],longueur), "blue")
draw = ImageDraw.Draw(image_horizontale)
del draw
for x in range(image_horizontale.size[0]):
	for y in range(image_horizontale.size[1]):
		Image.putpixel(image_horizontale, (x, y), Image.getpixel(camera, (x ,y+5*longueur)))
image_horizontale.save('image_horizontale_bas.jpg')
r,g,b = image_horizontale.split() 
array_image = np.zeros(image_horizontale.size)
for x in range(image_horizontale.size[0]):
	for y in range(image_horizontale.size[1]):
		array_image[x,y] = Image.getpixel(g, (x,y))
coordonnee_centre_de_masse_bas = ndimage.measurements.center_of_mass(array_image)
Image.putpixel(camera, (int(coordonnee_centre_de_masse_bas[0]),int(coordonnee_centre_de_masse_bas[1] + longueur*5)), (255,0,0))


draw = ImageDraw.Draw(camera)
draw.line( (int(coordonnee_centre_de_masse_haut[0]),int (coordonnee_centre_de_masse_haut[1]))+ (int(coordonnee_centre_de_masse_bas[0]),int(coordonnee_centre_de_masse_bas[1] + longueur*5)), fill="red")
del draw
camera.save("centredemasse.png")
