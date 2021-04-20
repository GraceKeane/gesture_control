import cv2
import time
import numpy as np
# Import module that I created to detect hand landmarks/points
import TrackingModule as tm
import math
# Import to connect this program to computer audio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Params
# Width and height of camera
wCam, hCam = 350, 350

# Check if camera is running properly
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
# Previous time
pTime = 0

# Only detect the hand if very certain it is a hand
detector = tm.handDetector(detectionCon=0.9)

tipIds = [4, 8, 12, 16, 20]

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
volRange = volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-20.0, None)
minVol = volRange[0]
maxVol = volRange[1]
# Setting initial volume to 0
vol = 0
volBar = 400; # Setting vol bar height to 400
volPercentage = 0;

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
        cv2.circle(img, (x1, y1), 10, (255, 255, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 255, 255), cv2.FILLED)
        # Create a line between the two fingers
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)

        # Put circle around the middle
        cv2.circle(img, (cx, cy), 12, (255, 255, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        #print(length)

        # Hand range is from 5 to 300
        # convert to vol range -65 to 0
        vol = np.interp(length, [50, 300], [minVol, maxVol])

        volBar = np.interp(length, [50, 300], [400, 150])
        # Assign the percentage the volume is at
        volPercentage = np.interp(length, [50, 300], [0, 100])

        print(int(length), vol)
        # Send volume to computer
        volume.SetMasterVolumeLevel(vol, None)

        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)


        # For loop for 4 long fingers
        for id in range(1, 5):
            # Look through fingers
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Print if fingers are up or down
        # by printing them in an array
        print(fingers)

        # Find how many fingers are up
        totalFingers = fingers.count(1)
        print(totalFingers)

        cv2.putText(img, f'Total Fingers Detected: {str(totalFingers)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 0), 1)

        if length<50:
            cv2.circle(img, (cx, cy), 15, (255, 0, 0))

    # Current time
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.imshow("Volume Control", img)
    cv2.waitKey(1)