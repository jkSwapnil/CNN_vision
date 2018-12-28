import cv2 as cv
import numpy as np
import os

path1="/home/swapnil/Desktop/project/train/Collar/"
path2="/home/swapnil/Desktop/project/train/V_neck/"

face_cascade = cv.CascadeClassifier('/home/swapnil/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')

for i, name in enumerate(os.listdir(path1)):
	image= cv.imread(path1+name)
	image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	#detecting face and croping the image fpr collar
	faces = face_cascade.detectMultiScale(image)
	for (x,y,w,h) in faces:
		#image=image[int(y+0.9*h):int(y+1.7*h), int(x-0.2*w):int(x+1.5*w)]
		#image = cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
		pass
	image = cv.resize(image, (32, 32), interpolation = cv.INTER_AREA)
	im_name='img_'+ str(2*i+2) + '.jpg'
	cv.imwrite(im_name,image)

for i, name in enumerate(os.listdir(path2)):
	image= cv.imread(path2+name)
	image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	#detecting face and croping the image fpr V_neck
	faces = face_cascade.detectMultiScale(image)
	for (x,y,w,h) in faces:
		image=image[int(y+0.9*h):int(y+1.7*h), int(x-0.2*w):int(x+1.5*w)]
		pass
	image = cv.resize(image, (32, 32), interpolation = cv.INTER_AREA)
	im_name='img_'+ str(2*i+1) + '.jpg'
	cv.imwrite(im_name,image)