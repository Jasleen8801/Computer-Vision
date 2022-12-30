import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# cv2.imshow("Image", img)
# cv2.waitKey(0)

# ******** Color the image ********  
img[:] = 255, 0, 0
# cv2.imshow("Blue image", img)
# cv2.waitKey(0)

# ******** Drawing a line ********  
# cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.imshow("Green line on black screen", img)
# cv2.waitKey(0)

# ******** Drawing a Rectangle ********  
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)
# cv2.imshow("Rectangle on Black screen", img)
# cv2.waitKey(0)

# ******** Drawing a Circle ********  
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
# cv2.imshow("Circle on black screen", img)
# cv2.waitKey(0)

# ******** Adding text on Image ********  
cv2.putText(img, "OPENCV", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150,0), 1)
cv2.imshow("Text on image", img)
cv2.waitKey(0)
