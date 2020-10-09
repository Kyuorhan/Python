import cv2
import numpy as np
    #   Importa as Bibliotecas
face_cascade = cv2.CascadeClassifier("cascade\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("cascade\\haarcascade_eye.xml")
    #   Classificador de Detection de Face/eye - Facial/olho
imagem = cv2.imread('imgs//meus//paulo1.jpg')
    #   Uma Variavel pra ler uma Imagem
facesDetectadas = face_cascade.detectMultiScale(imagem)
eyeDetectadas = eye_cascade.detectMultiScale(imagem)
    #   Uma variavel importando classificador para Detection Face/eye
print(len(facesDetectadas))
print(facesDetectadas)
print(len(eyeDetectadas))
print(eye_cascade)

for (x, y, w, h) in facesDetectadas:
    print(x, y, w, h)
    cv2.rectangle(imagem, (x,y), (x + w, y + h), (255, 155, 0), 2)
for (x, y, w, h) in eyeDetectadas:
    print(x, y ,w, h)
    cv2.rectangle(imagem, (x,y), (x + w, y + h), (255, 255, 0), 2)
    #   Onde são marcados os paramaetros de Detection das coordenadas
img_scaled = cv2.resize(imagem, None, fx=0.65, fy=0.65)
cv2.imshow("scaleds", img_scaled)
cv2.waitKey()
