import cv2
import glob
import os
import re

path = 'Section 17 - Image and Video Processing/Face Detection/*.jpg'

face_cascade = cv2.CascadeClassifier('Section 17 - Image and Video Processing/Face Detection/haarcascade_frontalface_default.xml')

for file in glob.glob(path):
    img = cv2.imread(file)
    name = re.split('\.', os.path.basename(file))[0]
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grey_img, scaleFactor=1.1, minNeighbors=5)

    # x: x-coordinate of top left corner of face
    # y: y-coordinate of top left corner of face
    # w: width of rectangular area containing face
    # h: height of rectangular area containing face
    for x, y, w, h in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

    print("Face detection for " + name + ".jpg is complete!")

    resized_img = cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))

    cv2.imshow('resized_'+name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
