import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

# ******** Converting to gray image ********
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Image", imgGray)
# cv2.waitKey(0)

# ******** Blurring an image ********
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# cv2.imshow("Blur Image", imgBlur)
# cv2.waitKey(0)

# ******** Edge Detector on Image ********
imgCanny = cv2.Canny(img, 150, 200)
# cv2.imshow("Edge Detector", imgCanny)
# cv2.waitKey(0)

# ******** Image Dilation ********
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# cv2.imshow("Image Dilation", imgDilation)
# cv2.waitKey(0)

# ******** Image Eroded ******** 
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
cv2.imshow("Image Eroded", imgEroded)
cv2.waitKey(0)
