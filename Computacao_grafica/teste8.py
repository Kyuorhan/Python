import cv2
import numpy as np

imgs = cv2.imread('imgs//meus//paulo1.jpg')
imgsCinza = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", imgs)
cv2.imshow("Cinza", imgsCinza)
cv2.waitKey()