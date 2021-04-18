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

detector = tm.handDetector()


# Check success
while True:
    success, img = cap.read()
    # Send open cv  image to detector
    img = detector.findHands(img)




    # Current time
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Frames per second
    cv2.putText(img, f'FPS: {int(fps)}', (40, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 3)


    cv2.imshow("Volume Control", img)
    cv2.waitKey(1)