#-*- coding: utf-8 -*-
from PIL.Image import *
import ImageFilter
from scipy import signal
from scipy import misc
from scipy import ndimage
import numpy as np
import ImageDraw
import sys

file = 'Camera3.png'
camera = open(file)

mask = new("RGB", camera.size, "blue")
draw = ImageDraw.Draw(mask)
del draw
for x in range(mask.size[0]):
	for y in range(mask.size[1]):
		if Image.getpixel(camera, (x,y)) == (0,255,0):
			Image.putpixel(mask, (x, y), (0,255,0))
		else :
			Image.putpixel(mask, (x, y), (0,0,0))
mask.save("mask3.png", "PNG")
