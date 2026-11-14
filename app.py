import cv2
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Object Detection Project")
def convert_to_rgb(image):
    return (cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

bg_subtraction=cv2.createBackgroundSubtractorMOG2()
captures=cv2.VideoCapture(r"C:\Users\hp\Downloads\vtest.avi")

while captures.isOpened():
    ret,frame=captures.read()
    if not ret:
        break

    fg_img=bg_subtraction.apply(frame)
    (contours,_)=cv2.findContours(fg_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for co in contours:
        if cv2.contourArea(co)>500:
            x,y,w,h=cv2.boundingRect(co)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Foreground",fg_img)
    cv2.imshow("Video",frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
         break
captures.release()
cv2.destroyAllWindows()

