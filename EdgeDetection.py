import cv2
import numpy as np

img = cv2.imread('./Cars0.png')
cv2.imshow('Original', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 10, 3, 3)
# kernel = np.ones((15, 15), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
eroded = cv2.erode(gray.copy(), None)

cv2.imshow("Eroded", eroded)
blackHat = cv2.morphologyEx(eroded, cv2.MORPH_BLACKHAT, kernel)
topHat = cv2.morphologyEx(blackHat, cv2.MORPH_TOPHAT, kernel, iterations = 3)
cv2.imshow("Top Hat", topHat)
cv2.imshow("Black hat", blackHat)

eroded = cv2.erode(topHat.copy(), None)


cv2.imshow("Eroded after blackHat", eroded)
# blur = cv2.blur(eroded, ksize=(3, 3))
# cv2.imshow("blur", blur)
# cv2.rectangle(eroded, (100, 100), (500, 500), (0, 255, 0), 3)
# cv2.imshow("Eroded after blackHat", eroded)
cv2.waitKey(0)