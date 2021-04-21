"""
    @author Grace Keane

    SnakeControl - Class which develops the OpenCv game control frame and also
    enables and defines gestures to be used in Snake application.

    This class imports my class SnakeKeys to get a handle on the
    keyboard functionality used to link to the gestures in
    this class (SnakeControl.py)
"""

# Necessary Imports needed

# Used to Convert and process image data into arrays
import numpy as np
# Used for Capturing real time video and image processing
import cv2
# Lets Python scripts control the mouse and keyboard to automate
# interactions with other applications.
import pyautogui
# Import the SnakeKeys.py class -> Needed for snake key actions
from SnakeKeys import up, left, down, right
from SnakeKeys import PressKey, ReleaseKey

# Write the range of lower and upper boundaries of the "blue" object after converting it to hsv region
# Colors set in HSV format -> Required for Open Cv
blueLower = np.array([50, 50, 50])
blueUpper = np.array([180, 180, 155])
# Declare a variable to capture the real time video of our webcam
video = cv2.VideoCapture(0);

# Set the initial values for parameter to use them later in the code
current_key = set()
# Set radius of circle for covering the object
radius_of_circle = 15
# Set window size of grabbed frame
window_size = 160
# Loop until OpenCV window is not closed
while True:
    keyPressed = False
    keyPressed_lr = False
    # Grab the current frame from webcam
    _, control_frame = video.read()
    height, width = control_frame.shape[:2]

    # https://docs.opencv.org/3.1.0/d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1
    '''GaussianBlur	(	InputArray 	src,
                        OutputArray 	dst,
                        Size 	ksize,
                        double 	sigmaX,
                        double 	sigmaY = 0,
                        int 	borderType = BORDER_DEFAULT)	'''

    control_frame = cv2.resize(control_frame, dsize=(600, height))
    blur_frame = cv2.GaussianBlur(control_frame, (11, 11), 0)
    hsv_value = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)

    # Create a cover for object so that it is able to detect the object easily without any
    # distraction by other details of image
    cover = cv2.inRange(hsv_value, blueLower, blueUpper)
    # Erode the masked output
    cover = cv2.erode(cover, None, iterations=2)
    # Dilate the resultant image
    cover = cv2.dilate(cover, None, iterations=2)

    # Divide the frame into two halves one for up and down keys
    # and other half is for left and right keys by using indexing
    left_cover = cover[:, 0:width // 2, ]
    right_cover = cover[:, width // 2:, ]

    # Function to extract the contours from the list
    def extract_contour(contours):
        if len(contours) == 2:
            contours = contours[0]
        elif len(contours) == 3:
            contours = contours[1]
        else:
            raise Exception("Error when detecting")
        return contours

    # Contours in the left and right frame to find the shape outline of the object for left side
    contour_l = cv2.findContours(left_cover.copy(),
                                 cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)
    # Extract from contour_l
    contour_l = extract_contour(contour_l)
    left_centre = None

    # CHAIN_APPROX_SIMPLE is for detecting only main point of contour instead of all boundary point
    # https://docs.opencv.org/3.4/d9/d8b/tutorial_py_contours_hierarchy.html
    contour_r = cv2.findContours(right_cover.copy(),
                                 cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)
    # Defined function to extract from contour_r
    contour_r = extract_contour(contour_r)
    right_centre = None

    # Looping if at least one contour or centre is found in left side of frame
    if len(contour_l) > 0:
        # for creating a circular contour with centroid
        c = max(contour_l, key=cv2.contourArea)
        ((x, y), r) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        # below is formula for calculating centroid of circle
        left_centre = (int(M["m10"] / (M["m00"] + 0.000001)), int(M["m01"] / (M["m00"] + 0.000001)))

        # If the radius meets a minimum size to avoid small distraction of same color then mark it in frame
        if r > radius_of_circle:
            # Draw the circle and centroid on the frame,
            cv2.circle(control_frame, (int(x), int(y)), int(r),
                       (0, 255, 0), 2)
            cv2.circle(control_frame, left_centre, 5, (0, 255, 0), -1)

            # Defining positions where left and right key will be detected
            if left_centre[1] < (height / 2 - window_size // 2):
                cv2.putText(control_frame, 'LEFT', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                # pyautogui is for clicking left key through gesture
                pyautogui.press('left')
                current_key.add(left)
                keyPressed = True
                keyPressed_lr = True
            elif left_centre[1] > (height / 2 + window_size // 2):
                cv2.putText(control_frame, 'RIGHT', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                pyautogui.press('right')  # pyautogui is for clicking right key through gesture
                current_key.add(right)
                keyPressed = True
                keyPressed_lr = True

    # Loop again if one contour or centre is found in right side of frame
    if len(contour_r) > 0:
        c2 = max(contour_r, key=cv2.contourArea)
        ((x2, y2), r2) = cv2.minEnclosingCircle(c2)
        M2 = cv2.moments(c2)
        right_centre = (int(M2["m10"] / (M2["m00"] + 0.000001)), int(M2["m01"] / (M2["m00"] + 0.000001)))
        right_centre = (right_centre[0] + width // 2, right_centre[1])

        if r2 > radius_of_circle:
            # Draw the circle and centroid on the frame if detect something
            cv2.circle(control_frame, (int(x2) + width // 2, int(y2)), int(r2),
                       (0, 255, 0), 2)
            cv2.circle(control_frame, right_centre, 5, (0, 255, 0), -1)
            if right_centre[1] < (height // 2 - window_size // 2):
                cv2.putText(control_frame, 'UP', (200, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                pyautogui.press('up')
                keyPressed = True
                current_key.add(up)
            elif right_centre[1] > (height // 2 + window_size // 2):
                cv2.putText(control_frame, 'DOWN', (200, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                pyautogui.press('down')
                keyPressed = True
                current_key.add(down)

    # Open Cv game detection window
    control_frame = control_frame.copy()
    # Developing a blue rectangular box for the detections to be done, defining height and width
    control_frame = cv2.rectangle(control_frame, (0, height // 2 - window_size // 2),
                                       (width, height // 2 + window_size // 2), (255, 0, 0), 2)
    cv2.imshow("Snake Controls", control_frame)


# Stop game
video.stop()
# Close all windows
cv2.destroyAllWindows()