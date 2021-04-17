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

# Previous time
pTime = 0
cTime = 0

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
            # Check index number of hand using id and landmark
            for id, lm in enumerate(handLms.landmark):
                # Test to see id and landmark
                # Using x and y to find landmark on the hand
                #print(id, lm)
                h, w, c = img.shape
                # Find position of the center of hand (cx & cy)
                # Landmark of x * width & landmark of y * height
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)

                cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)



                print(id, cx, cy)

            # Drawing hand position and landmarks
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # Print frame rate to screen
    cv2.putText(img, str(int(fps)), (10, 70), cv2.QT_FONT_BLACK, 1,
                (255, 0, 255), 3)

    # Run open cv
    cv2.imshow("Gesture Recognition", img)
    # Allow camera to continue running
    cv2.waitKey(1)