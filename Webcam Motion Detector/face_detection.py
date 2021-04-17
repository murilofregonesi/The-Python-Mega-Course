import cv2
import time

cascade_url = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_url)

# Capture video
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    if check:
        # Face detection
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)

        for face in faces:
            x, y, w, h = face
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        # Show image
        cv2.imshow('Frame', frame)
    
    key = cv2.waitKey(1)
    if key >= 0:
        break

video.release()
cv2.destroyAllWindows
