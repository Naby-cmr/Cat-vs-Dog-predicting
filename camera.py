# we take photos with the webcams
import cv2
import streamlit as st



st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
count = 0
while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    cv2.imwrite("photos/frame%d.jpg" % count, frame) # save frame as JPEG file in photos folder
    count += 1
else:
    st.write('Stopped')







