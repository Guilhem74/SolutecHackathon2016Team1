#-*- coding: utf-8 -*-
from PIL.Image import *
from PIL import ImageFilter
from scipy import signal
from scipy import misc
from scipy import ndimage
import numpy as np
from PIL import ImageDraw
import sys
import time

from fonctions import *
chemin_acces_photo = "CAM/Camera1.jpg"
image_cible = Ouvrir_Image(chemin_acces_photo)
image_cible = image_cible.rotate(-90)
image_cible.save("CAM/Camera1.jpg")
time.sleep(1)
chemin_acces_photo = "CAM/Camera2.jpg"
image_cible = Ouvrir_Image(chemin_acces_photo)
image_cible = image_cible.rotate(-90)
image_cible.save("CAM/Camera2.jpg")
time.sleep(1)
chemin_acces_photo = "CAM/Camera3.jpg"
image_cible = Ouvrir_Image(chemin_acces_photo)
image_cible = image_cible.rotate(-90)
image_cible.save("CAM/Camera3.jpg")
time.sleep(1)
