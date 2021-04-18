import cv2
import time
import numpy as np
# Import module that I created to get hand landmarks/points
import TrackingModule as tm

# Params
# Width and height of camera
wCam, hCam = 640, 480

# Check if camera is running properly
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
# Previous time
pTime = 0

# Only detect the hand if very certain it is a hand
detector = tm.handDetector(detectionCon=0.9)


# Check success
while True:
    success, img = cap.read()
    # Send open cv  image to detector
    img = detector.findHands(img)
    # Get position
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # Getting landmark 4 and 8 -> var for top of thumb and
        # index finger
        print(lmList[4], lmList[8])
        # Create a circle around the two fingers

        # Get x and y positions of two fingers
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        # Get center of the line
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # Take in img, position, radius, color, fill
        cv2.circle(img, (x1, y1), 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 0), cv2.FILLED)
        # Create a line between the two fingers
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        # Put circle around the middle
        cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)





    # Current time
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Frames per second
    cv2.putText(img, f'FPS: {int(fps)}', (40, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 3)


    cv2.imshow("Volume Control", img)
    cv2.waitKey(1)