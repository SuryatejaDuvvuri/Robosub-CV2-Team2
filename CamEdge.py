import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(1)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("U-H", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 180, 180, nothing)

while True:
    ret, capturing = cap.read()
    hsv = cv2.cvtColor(capturing, cv2.COLOR_BGR2HSV)
    lower_h = cv2.getTrackbarPos("L-H", "Trackbars")
    lower_s = cv2.getTrackbarPos("L-S", "Trackbars")
    lower_v = cv2.getTrackbarPos("L-V", "Trackbars")
    upper_h = cv2.getTrackbarPos("U-H", "Trackbars")
    upper_s = cv2.getTrackbarPos("U-S", "Trackbars")
    upper_v = cv2.getTrackbarPos("U-V", "Trackbars")
    
    
    low = np.array([lower_h,lower_s,lower_v]) # hsv low format
    up = np.array([upper_h,upper_s,upper_v])
    mask = cv2.inRange(hsv,low,up)
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.erode(mask, kernel)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        mask = cv2.drawContours(capturing, [cnt], 0, (0, 255, 0), 3)
    blur = cv2.GaussianBlur(hsv, (7, 7), 0)
    edge = cv2.Canny(blur, 30, 150)
    md = np.median(edge)
    

    # Make it in a way that only shows the shapes and blacks out everything else
    # ret, thresh1 = cv2.threshold(edge, 220, 255, cv2.THRESH_BINARY)
    # cv2.imshow('Original', capturing)
    # cv2.imshow('Edges', thresh1)
    # cv2.imshow("Frame",capturing)
    cv2.imshow("edges",edge)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
