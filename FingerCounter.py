import cv2
import time
import HandTracking as ht

wCam, hCam = 640, 480

# Turn on video
cap = cv2.VideoCapture(0)
# Set size
cap.set(3, wCam)
cap.set(4, hCam)

detector = ht.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]


while True:
    success, img = cap.read()
    cv2.imshow("Finger Counter", img)
    # 1 min delay
    cv2.waitKey(1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    #print(lmList)

    if len(lmList) != 0:
        # Using finger marks to determine
        # how many fingers are up / down

        # If point 8 is less than point 6 -> hand open
        if lmList[8][2] < lmList[6][2]:
            print("Index finger open")
        else:
            print("Not open")

