import cv2

print(cv2.__version__)

imagem = cv2.imread('imgs\\meus\\manu1.png')
imagem[25:175, 25:175] = (0, 0, 255)

cv2.imshow("Original", imagem)

cv2.waitKey()
