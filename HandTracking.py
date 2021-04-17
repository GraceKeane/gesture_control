import cv2
import mediapipe as mp
import time

# Assigning camera
cap = cv2.VideoCapture(0)

while True:
    # Load and run webcam
    success, img = cap.read()
    cv2.imshow("Gesture Recognition", img)
    cv2.waitKey(1)