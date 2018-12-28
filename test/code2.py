import cv2 as cv
import numpy as np
import os

path="/home/swapnil/Desktop/project/test/"

for i in range(24):
	name= path + str(i+1) + '.jpg'
	print(name)
	image= cv.imread(name)
	image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	image = cv.resize(image, (32, 32), interpolation = cv.INTER_AREA)
	#print(h,b)
	im_name='img_'+ str(i+1) + '.jpg'
	cv.imwrite(im_name,image)