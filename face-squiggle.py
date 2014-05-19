import sys, os
#from PIL import Image
from SimpleCV import *
from SimpleCV import ImageClass
from random import randint




def facesquiggle(pic):
	faces = pic.findHaarFeatures("haarcascade_frontalface_alt2.xml")
	for f in faces:
		red = randint(245,255)
		green = randint(245,255)
		blue = randint(245,255)
		facewidth = f.width()
		facex = f.x - f.width()/2
		facey = f.y - f.height()/2
		pic.dl().selectFont('helvetica')
		pic.drawText('FACE', facex, facey, (red,green,blue), facewidth/2)

	
				#was using this to draw my own image over detected features (decided to let the computer draw and further remove myself, more procedural)
				#sqg = Image("sqg.png") #needs to be in the same directory
				#sqgmask = sqg.createAlphaMask(hue=1)
				#sqgmask = sqg.createBinaryMask(color1=(0, 0, 0),color2=(5,5,5))
				#print sqg.height


				#for f in faces:
					#facewidth = f.width()
					#faceheight = f.height()
					#facex = f.x
					#facey = f.y
					#sqgx = f.x - f.width()/2
					#sqgy = f.y - f.height()/2
					#facesqg = sqg.adaptiveScale((facewidth, faceheight))
					#sqgmaskscaled = sqgmask.adaptiveScale((facewidth, faceheight))
					#print facesqg.height
					#simplecv only method 
					#pic = pic.blit(facesqg,pos=(sqgx,sqgy))
					#This is a PIL version which has support for transparent .png
					#pic = PIL.paste(sqg, (facesqg, sqgx, sqgy), mask=facesqg) 
	#points = pic.findFeatures("harris", 1000)
	#for p in points:
	#	red = randint(1,255)
	#	green = randint(1,255)
	#	blue = randint(1,255)
	#	p.draw((red, green, blue))

	corners = pic.findCorners()
	for c in corners:
		red = randint(1,255)
		green = randint(1,255)
		blue = randint(1,255)
		c.draw((red, green, blue))

	points = pic.findFeatures("harris", 500)
	for p in points:
		red = randint(1,255)
		green = randint(1,255)
		blue = randint(1,255)
		pointx = p.x
		pointy = p.y
		p.draw((red,green,blue))	

	savestring = str(sys.argv[1])
	savestring = savestring.lstrip('cv_two/selfie')
	savestring = "selfie%s" % (savestring)


	pic.save("cv_three/%s" % (savestring))
	print "Finished turning %s into %s" % (sys.argv[1],savestring)



def main():
	pic = Image(sys.argv[1])
	facesquiggle(pic)


if __name__ == "__main__":
  main()