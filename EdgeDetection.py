import cv2
import numpy as np

img = cv2.imread('./Shape.png')
edge_img = cv2.Canny(img,100,200)
cv2.imshow('Detected edges', edge_img)
cv2.waitKey(0)