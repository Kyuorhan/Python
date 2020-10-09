        # Importa biblioteca Opencv e numpy
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("cascade\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("cascade\\haarcascade_eye.xml")

Webcam = cv2.VideoCapture(0)

while(not cv2.waitKey(20) & 0xFF == ord('p')):
        ret, frame = Webcam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray)
        eye = eye_cascade.detectMultiScale(gray)
        for (x, y, w, h) in face:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 155, 0), 2)
        for (x, y, w, h) in eye:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (155, 155, 0), 2)

        scaled = cv2.resize(frame, None, fx=1.55, fy=1.55)
        cv2.imshow('frame', scaled)
        print(len(face))
        print(face)
        print(len(eye))
        print(eye)

cap.release()
cv2.destroyAllWindows()



