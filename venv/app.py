import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  

st.title("Real-Time Object Detection App")

if 'run_webcam' not in st.session_state:
    st.session_state.run_webcam = False

def run_webcam():
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()
    accuracy_placeholder = st.empty()

    while st.session_state.run_webcam:
        ret, frame = cap.read()
        if not ret:
            break
        
        
        results = model(frame)
        annotated_frame = results[0].plot()  
        
        # Check if there are any detections
        if len(results[0].boxes) > 0:
            # Get the confidence and class name of the first detection
            accuracy = results[0].boxes.conf[0] 
            class_id = int(results[0].boxes.cls[0]) 
            class_name = model.names[class_id] 
            
            accuracy_percentage = f"{accuracy * 100:.2f}%"  
            detection_info = f"{class_name} - {accuracy_percentage}"
        else:
            detection_info = "No detections"

        # Update the placeholders with the new frame and detection info
        frame_placeholder.image(annotated_frame, channels="BGR")
        accuracy_placeholder.write(f"Detection: {detection_info}")

    cap.release()


if st.button("Start Webcam"):
    st.session_state.run_webcam = True
    run_webcam()

if st.button("Stop Webcam"):
    st.session_state.run_webcam = False