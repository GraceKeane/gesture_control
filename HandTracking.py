# Gesture UI Development
# Grace Keane - G00359990
# Using Open Cv to control computer features

#--- Imports

import cv2
import mediapipe as mp
import time

#--- Assigning

# Assigning camera
cap = cv2.VideoCapture(0)
# Detect a part of the hand
mpHands = mp.solutions.hands
# Creating an object of hands
hands = mpHands.Hands()
# Draw hand on hand
mpDraw = mp.solutions.drawing_utils

while True:
    # Load and run webcam
    success, img = cap.read()
    # Convert color because hands class only uses RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Precess hand frame constantly
    results = hands.process(imgRGB)

    # Detect if theres a hand -> testing
    print(results.multi_hand_landmarks)

    # If a hand or multi hands detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms)


    cv2.imshow("Gesture Recognition", img)
    # Allow camera to continue running
    cv2.waitKey(1)