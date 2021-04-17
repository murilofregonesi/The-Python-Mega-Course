import cv2
from copy import copy

background = None
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    
    if check:
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.GaussianBlur(frame_gray, (21,21), 0)

        if background is None:
            background = frame_gray
            continue

        cv2.imshow('Frame', frame_gray)

        contrast = cv2.absdiff(frame_gray, background)
        contrast_threshould = cv2.threshold(contrast, 150, 255, cv2.THRESH_BINARY)[1]
        contrast_threshould = cv2.dilate(contrast_threshould, None, iterations=2)

        (cnts,_) = cv2.findContours(contrast_threshould, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for countour in cnts:
            if cv2.contourArea(countour) < 1000:
                continue
            
            (x,y,w,h) = cv2.boundingRect(countour)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        cv2.imshow('Camera', frame)
        cv2.imshow('Contrast', contrast)
        cv2.imshow('Contrast Threshould', contrast_threshould)
    
    key = cv2.waitKey(1)
    if key >= 0:
        break

video.release()
cv2.destroyAllWindows
