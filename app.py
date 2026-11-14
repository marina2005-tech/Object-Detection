import cv2
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import tempfile

def convert_to_rgb(image):
    return (cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

st.title("Object Detection Project")

video_file=st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if video_file is not None:
    tfile=tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    tfile.close()


    col1,col2=st.columns(2)
    with col1:
        st.header("Foreground Image")
        st_frame1=st.empty()

    with col2:
        st.header("Tracked Objects")
        st_frame2=st.empty()


    captures=cv2.VideoCapture(tfile.name)

    bg_subtraction=cv2.createBackgroundSubtractorMOG2()


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

        st_frame1.image(fg_img,caption="Foreground Image")
        st_frame2.image(convert_to_rgb(frame),caption="Tracked Objects")

  
    captures.release()


