# Program to find a size(resolution) of a image

import PIL
from PIL import Image
import PIL.Image

img  = PIL.Image.open("C:/Users/ASUS/OneDrive/Pictures/HD-wallpaper-tony-stark-iron-man-iron-man-tony-stark-thumbnail.jpg")
width , height = img.size

print(width,"x",height)