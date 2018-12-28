
import sys
import cv2
import os
import glob
# Get user supplied values
cascade = cv2.CascadeClassifier('/home/swapnil/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')

cropImages=[]
img_dir = "/home/swapnil/Desktop/project/train/Collar/"

data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
crop=[]
for f1 in files:
    img = cv2.imread(f1,0) 
    data.append(img)
i=0
for f2 in data:
    faces=[]
    faces = cascade.detectMultiScale(
        f2,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE )
    print(i)    
    if faces != () and len(faces)==1:   
        for (x, y, w, h) in faces:
            
            #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            f2=f2[int(y+0.8*h):int(y+1.5*h), int(x-0.2*w):int(x+1.5*w)]
            
            cropImages.append(f2)
            
            if len(f2[0])!=0 :                
                f2=cv2.resize(f2,(32,32))
                name='img_'+ str(2*i+1) + '.jpg'
                cv2.imwrite(name, f2)
                #cv2.imwrite(r"/home/swapnil/Desktop/dummy/V_%i.jpg"%i,f2)
                crop.append(f2)
            i=i+1
