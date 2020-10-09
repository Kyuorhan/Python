import cv2
import numpy as np
    #   Importa as Bibliotecas
face_cascade = cv2.CascadeClassifier("cascade\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("cascade\\haarcascade_eye.xml")
    #   Classificador de Detection de Face/eye - Facial/olho
imagem = cv2.imread('meus//joao1.jpeg')
    #   Uma Variavel pra ler uma Imagem
facesDetectadas = face_cascade.detectMultiScale(imagem)
eyeDetectadas = eye_cascade.detectMultiScale(imagem)
    #   Uma variavel importando coordenadas de escalas detection Face/eye
print(len(facesDetectadas))
print(facesDetectadas)
print(len(eyeDetectadas))
print(eye_cascade)
    # printar as coordenadas os pontos detetados faces/eye
for (x, y, w, h) in facesDetectadas:
    print(x, y, w, h)
    cv2.rectangle(imagem, (x,y), (x + w, y + h), (255, 155, 0), 2)
for (x, y, w, h) in eyeDetectadas:
    print(x, y ,w, h)
    cv2.rectangle(imagem, (x,y), (x + w, y + h), (255, 255, 0), 2)
    #   Onde são marcados as coordenadas dos paramentros (x,w,y,h) e a fonto da cor das coordenadas das bordas
img_scaled = cv2.resize(imagem, None, fx=0.75, fy=0.75)
    #   Escala da imagem - Resolução da imgs
cv2.imshow("scaleds", img_scaled)
cv2.waitKey()
