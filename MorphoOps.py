import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.imread("./Shape.png")
gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
median = cv2.medianBlur(gray, 3)
ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# kernel = np.ones((3,3),np.uint8)
# print(kernel)
# erosion = cv2.erode(threshold, kernel, iterations=1)
# dilation = cv2.dilate(erosion, kernel, iterations=1)
# opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)

# plt.hist(cap.flat, bins=100, range=(0,255))
# plt.show()

cv2.imshow("Original image", cap)
# cv2.imshow("OTSU Image",threshold)
# cv2.imshow("Eroded image", erosion)
# cv2.imshow("Dilated image", dilation)
# cv2.imshow("Opened image", opening)
cv2.imshow("Median Image", median)
cv2.imshow("OTSU Image",threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()