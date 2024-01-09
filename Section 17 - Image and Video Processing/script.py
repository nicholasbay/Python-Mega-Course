import cv2

# 1: Read image in colour
# 0: Read image in greyscale
# -1: Read image including alpha channel
img = cv2.imread('Section 17 - Image and Video Processing/galaxy.jpg', 0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Galaxy", resized_img)
cv2.waitKey(0)
cv2.destroyWindow("Galaxy")

cv2.imwrite('Section 17 - Image and Video Processing/galaxy_resized.jpg', resized_img)
print("Save successful!")