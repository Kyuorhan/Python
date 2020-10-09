import numpy as np
import cv2
    #   Testando Imagns e analisando a Matriz
face_cascade = cv2.CascadeClassifier("cascade\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("cascade\\haarcascade_eye.xml")
    #   Classificador de Detection de Face/eye - Facial/olho
imagem = cv2.imread('imgs//meus//paulo1.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

face_Detectadas = face_cascade.detectMultiScale(imagemCinza)
eye_Detectadas = eye_cascade.detectMultiScale(imagemCinza)
print(len(face_Detectadas))         #   Quantas faces detectados
print(len(eye_Detectadas))          #   Quantos olhos detectados
print("----------------------")
print(face_Detectadas)              #   Marcação da Matriz da face detectado
print("----------------------")
print(eye_Detectadas)               #   Marcação da Matriz do olho