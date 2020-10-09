import cv2, os

BLUE_COLOR = (255, 0, 0)
STROKE = 2


clf = cv2.CascadeClassifier("cascade\\haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while(not cv2.waitKey(20) & 0xFF == ord('p')):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(gray)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), BLUE_COLOR, STROKE)
        cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()