import numpy as np
import cv2

print(cv2.__version__)

imagem = cv2.imread('imgs//meus//paulo1.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

img_scaled = cv2.resize(imagem, None, fx=0.35, fy=0.35)
img_scaled_cinza = cv2.resize(imagemCinza, None, fx=0.55, fy=0.55)
cv2.imshow("Original", img_scaled)
cv2.imshow("Cinza", img_scaled_cinza)
cv2.waitKey()