import cv2
import streamlit as st
import time

st.set_page_config(layout="wide")

# Define time
week_day = time.strftime("%A")
hours = time.strftime("%H:%M:%S")

st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text=week_day, org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=hours, org=(50, 100),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)
