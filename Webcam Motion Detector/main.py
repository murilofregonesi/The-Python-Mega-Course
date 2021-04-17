import cv2
from copy import copy
from datetime import datetime
import pandas as pd

background = None
video = cv2.VideoCapture(0)
status = []

while True:
    check, frame = video.read()
    
    if check:
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.GaussianBlur(frame_gray, (21,21), 0)

        if background is None:
            background = frame_gray
            status.append((0, datetime.now()))
            continue

        cv2.imshow('Frame', frame_gray)

        contrast = cv2.absdiff(frame_gray, background)
        contrast_threshould = cv2.threshold(contrast, 100, 255, cv2.THRESH_BINARY)[1]
        contrast_threshould = cv2.dilate(contrast_threshould, None, iterations=2)

        (cnts,_) = cv2.findContours(contrast_threshould, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        curr_status = 0
        for countour in cnts:
            if cv2.contourArea(countour) < 1000:
                continue
            
            (x,y,w,h) = cv2.boundingRect(countour)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            curr_status = 1

        # get status change
        if status[-1][0] != curr_status:
            status.append((curr_status, datetime.now()))

        cv2.imshow('Camera', frame)
        cv2.imshow('Contrast', contrast)
        cv2.imshow('Contrast Threshould', contrast_threshould)
    
    # quit
    key = cv2.waitKey(1)
    if key >= 0:
        if status[-1][0] == 1:
            status.append((1, datetime.now()))
        break

video.release()
cv2.destroyAllWindows

# export data
status_df = pd.DataFrame()
for i in range(1, len(status), 2):
    status_df = status_df.append({'start': status[i][1], 'finish': status[i+1][1]},
                                 ignore_index=True)

status_df.to_csv('status.csv')
