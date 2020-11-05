# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:41:02 2020

@author: tripprakhar
"""
import cv2
#import face_recognition
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
input_movie = cv2.VideoCapture(r'D:/deepfake/DFdata/cxttmymlbn.mp4',0)
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter('video1111.mov',-1, 25.0, (640,480))

frame_number = 0

while True:
    #grab frames
    ret, frame = input_movie.read()
    frame_number += 1
    
    #end when video ends
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=5)
    for(x,y,w,h) in faces:
        roi_color = frame[y:y+h, x:x+w, :]
    roi_color = cv2.resize(roi_color, (640, 480)) 
    output_movie.write(roi_color)
    print("saving frame {} / {}".format(frame_number, length))


input_movie.release()
output_movie.release()
cv2.destroyAllWindows()