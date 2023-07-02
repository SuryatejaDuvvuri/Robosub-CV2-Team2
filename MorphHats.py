import cv2
import numpy as np

# img = cv2.imread("./Shape.png")
img = cv2.VideoCapture(0)

while True:
    ret, capturing = img.read()
    gray = cv2.cvtColor(capturing, cv2.COLOR_BGR2GRAY)
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10,10))
    # blackHat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
    
    # _, threshold = cv2.threshold(blackHat, 30, 255, cv2.THRESH_BINARY)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13,5))
    
    # opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    # closing = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
    # blackHat = cv2.morphologyEx(threshold, cv2.MORPH_BLACKHAT, kernel)
    
    tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
    cv2.imshow("Opening image", cv2.Canny(tophat, 100,200))
    
    # cv2.imshow("Top hat", tophat)
    # cv2.imshow("Closing image", closing)
    if(cv2.waitKey(1) == ord('q')):
        break
img.release()
cv2.destroyAllWindows()
