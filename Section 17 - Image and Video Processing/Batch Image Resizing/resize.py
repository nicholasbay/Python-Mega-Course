import cv2
import glob
import os
import re

read_path = 'Section 17 - Image and Video Processing/Batch Image Resizing/sample_images/*.jpg'
write_path = 'Section 17 - Image and Video Processing/Batch Image Resizing/resized_samples/'

for file in glob.glob(read_path):
    img = cv2.imread(file, 1)
    name = re.split('\.', os.path.basename(file))[0]
    
    resized_img = cv2.resize(img, (100, 100))
    
    cv2.imshow('resized_'+name, resized_img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    cv2.imwrite(write_path+'resized_'+name+'.jpg', resized_img)
    
    print("Save successful!")
