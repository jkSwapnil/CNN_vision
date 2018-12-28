#form __future__ import print_function
#from PIL import ImageGrab
import cv2 as cv
import numpy as np

vidcap = cv.VideoCapture('sample.mp4')
crop_img=None
success,image = vidcap.read()
#print(np.size(image,1))
face_cascade = cv.CascadeClassifier('/home/swapnil/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
count = 0;
print(int(vidcap.get(cv.CAP_PROP_FRAME_COUNT)))
print(int(vidcap.get(cv.CAP_PROP_FPS)))
while success:
	success,image = vidcap.read()
	image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	image = image[50:400, 320:650]
	faces = face_cascade.detectMultiScale(image)
	for (x,y,w,h) in faces:
		crop_img=image[int(y+0.9*h):int(y+1.7*h), int(x-0.2*w):int(x+1.5*w)]
		#image = cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
	#crop_img=cv.resize(crop_img, (32,32), interpolation = cv.INTER_AREA)

	if count%12==0:
		#cv.imwrite("frame%d.jpg" % count, image)
		cv.imwrite("%d.jpg" % count, crop_img)
	if cv.waitKey(10) == 27:
			break
	count += 1