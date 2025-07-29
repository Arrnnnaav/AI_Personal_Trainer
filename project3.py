#we will be finding the angle between two joints and
#according to that angle we can predict and tell whether the exercise done is in a right way or not
import cv2 as cv
import numpy as np
import PoseEstimationModule as pose

cap = cv.VideoCapture(0)
detector = pose.poseDetector()
count = 0
dir = 0
while True:
    success, img = cap.read()
    img = cv.flip(img, 1)
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, draw=False)
    #print(lmList)
    if len(lmList) != 0:
        # Right Arm
        angle = detector.findAngle(img, 15,13,11, draw=True)
        # # Left Arm
        # angle = detector.findAngle(img, 11, 13, 15,False)
        per = np.interp(angle, (150,30), (0, 100))
        bar = np.interp(angle, (150,30), (300, 100))
        # print(angle, per)
        # Check for the dumbbell curls
        color = (200, 0, 0)
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0

        #print(count)
        print(bar)
        # Draw Bar
        cv.rectangle(img, (50, 100), (70, 300), color, 3)
        cv.rectangle(img, (50, int(bar)), (70, 300), color, cv.FILLED)
        cv.putText(img, f'{int(per)} %', (50, 350), cv.FONT_HERSHEY_PLAIN, 3,
                    color, 3)
        # Draw Curl Count
        cv.putText(img, str(int(count)), (50,50), cv.FONT_HERSHEY_PLAIN, 2,
                    (0, 0, 0), 2)

    cv.namedWindow('image', cv.WINDOW_NORMAL)
    cv.imshow('image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()