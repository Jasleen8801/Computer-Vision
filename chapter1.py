import cv2
# print("Package imported")

# ******** Display an image ********
# img = cv2.imread("resources/lena.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# ******** Display a Video ********
# cap = cv2.VideoCapture("resources/test_video.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# ******** Display Webcam ********
cap = cv2.VideoCapture(0)
cap.set(3, 648)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
