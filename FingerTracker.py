import cv2
import mediapipe as mp
import time
import TrackingModule as tm

# Processed single fingers and added to list


# Previous time
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = tm.handDetector()

while True:
    # Load and run webcam
    success, img = cap.read()
    # Send image detector
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    # If nothing found - length of list is 0
    if len(lmList) != 0:
        # Print value of list at any index
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Print frame rate to screen
    cv2.putText(img, str(int(fps)), (10, 70), cv2.QT_FONT_BLACK, 1,
                (255, 0, 255), 3)

    # Run open cv
    cv2.imshow("Gesture Recognition", img)
    # Allow camera to continue running
    cv2.waitKey(1)