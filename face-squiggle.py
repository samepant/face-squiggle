import sys, os
from SimpleCV import Color
from SimpleCV import *

def facedetect(pic):
	faces = pic.findHaarFeatures("haarcascade_frontalface_alt2.xml")
	for f in faces:
		print "Face located at " + str(f.coordinates())
	faces.draw(Color.GREEN)
	pic.save("face_detect.jpg")


def main():
	pic = Image(sys.argv[1])
	facedetect(pic)


if __name__ == "__main__":
  main()