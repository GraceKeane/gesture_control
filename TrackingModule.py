"""
    @author Grace Keane

    Class that maps a landmark to a specific area on the hand.
    Used for Hand Gesture Sound Control.
"""

import cv2
import mediapipe as mp
import time

# Visualisation
class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5 ):
        # Create an object and object will have its own var
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # Detect a part of the hand
        self.mpHands = mp.solutions.hands
        # Creating an object of hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        # Draw hand on hand
        self.mpDraw = mp.solutions.drawing_utils

    # Detection function
    def findHands(self, img, draw=True):
        # Convert color because hands class only uses RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Precess hand frame constantly
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                # Check index number of hand using id and landmark
                if draw:
                    # Drawing hand position and landmarks
                    self.mpDraw.draw_landmarks(img, handLms,
                                                self.mpHands.HAND_CONNECTIONS)
        return img

    # Finding position of landmarks
    def findPosition(self, img, handNo=0, draw=True):
        # Creating the landmark list to return
        lmList = []
        if self.results.multi_hand_landmarks:
            # Which hand?
            # Point to the hand number
            myHand = self.results.multi_hand_landmarks[handNo]
            # Get all landmarks in that hand and put in a list
            for id, lm in enumerate(myHand.landmark):
                # Using x and y to find landmark on the hand
                h, w, c = img.shape
                # Find position of the center of hand (cx & cy)
                # Landmark of x * width & landmark of y * height
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

                # By default draw is true
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        # Return the list of land marks
        return lmList
def main():
    # Previous time
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

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

if __name__ == "__main__":
    main()