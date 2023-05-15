import cv2
import numpy as np

cap = cv2.VideoCapture(1)
while True:
    ret, capturing = cap.read()
    hsv = cv2.cvtColor(capturing, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv, (7, 7), 0)
    edge = cv2.Canny(blur, 100, 100)

    # Make it in a way that only shows the shapes and blacks out everything else
    ret, thresh1 = cv2.threshold(edge, 220, 255, cv2.THRESH_BINARY)
    cv2.imshow('Original', capturing)
    cv2.imshow('Edges', thresh1)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
