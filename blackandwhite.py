"""
Program: blackandwhite.py
Author: Chris 10/13/2020

***NOTE: the images.py module MUST be in the same directory as this file for this code to work properly!!***

Program will display the orig image and then convert it to pure black and white.
"""

from images import Image

def main():
	filename = input("Please enter the filename you wish to use (Must be a GIF file) >>")
	image = Image(filename)
	print("Close the image window to continue.")
	#draw orig image file
	image.draw()
	#indicate that the next phase is happening
	print("Processing image...")
	#send orig file data into the blackandwhite function
	blackAndWhite(image)
	print("Close the new image window to quit.")
	#draws the black and white version of the image
	image.draw()

def blackAndWhite(image):
	"""	Converts the argument image to pure black and white based on its orig pixel color """
	blackPixel = (0, 0, 0)
	whitePixel = (255, 255, 255)
	#for loops to handle the row major travesal of the pixels
	for y in range(image.getHeight()):
		for x in range(image.getWidth()):
			(r, g, b) = image.getPixel(x, y)
			average = (r + g + b) // 3
			#if the average is low, its a dark color, we convert it to pure black
			if average < 128:
				image.setPixel(x, y, blackPixel)
			else:
				image.setPixel(x, y, whitePixel)

#global call to the main() function
main()				



