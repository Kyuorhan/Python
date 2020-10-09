import cv2
#   Colocar uma escala na imagem
imagem = cv2.imread('imgs//meus//paulo1.jpg')

img_scaled = cv2.resize(imagem, None, fx=0.55, fy=0.55)
cv2.imshow("Original", imagem)
cv2.imshow("Escala", img_scaled)
cv2.waitKey()


