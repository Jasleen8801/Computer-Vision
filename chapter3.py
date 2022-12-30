import cv2
import numpy as np

img = cv2.imread("resources/lambo.png")
# cv2.imshow("Image", img)
# cv2.waitKey(0)

# print(img.shape) 

# ******** Resizing an Image ********  
imgResize = cv2.resize(img, (300, 200))
# cv2.imshow("Resize image", imgResize)
# cv2.waitKey(0)
# print(imgResize.shape)

# ******** Cropping an Image ********  
imgCropped = img[0:200, 200:500]
# cv2.imshow("Cropped image", imgCropped)
# cv2.waitKey(0)
