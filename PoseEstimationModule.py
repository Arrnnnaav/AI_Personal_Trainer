import cv2 as cv
import mediapipe as mp
import math
class poseDetector:
    def __init__(self,mode = False, complexit = 1, smoothlandmarks = True, segmentation = False, detection = 0.5, tracking = 0.5):
        self.mode = mode
        self.complexit = complexit
        self.smoothlandmarks = smoothlandmarks
        self.segmentation = segmentation
        self.detection = detection
        self.tracking = tracking
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.complexit,self.smoothlandmarks,self.segmentation,self.detection,self.tracking)
        self.mpDraw = mp.solutions.drawing_utils

    def findPose(self,img,draw):
        imgBGR = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.result = self.pose.process(imgBGR)
        # to get the information about landmarks
        # print(result.pose_landmarks)
        if self.result.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.result.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self,img,draw):
        self.lmList = []
        if self.result.pose_landmarks:
        #access landmark coordinates
            for id, lm in enumerate(self.result.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv.putText(img,str(id), (cx,cy), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
        return self.lmList

    def findAngle(self, img, p1, p2, p3, draw):
        #get landmarks
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]
        #calculate the angle
        angle = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2))
        if angle<0:
            angle += 360
        #print(angle)
        #drawing the points
        if draw:
            cv.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
            cv.line(img, (x3, y3), (x2, y2), (255, 255, 255), 2)
            cv.circle(img,(x1,y1), 10, (255,0,0), cv.FILLED)
            cv.circle(img, (x1, y1), 18, (255, 0, 0), 2)
            cv.circle(img, (x2, y2), 10, (255, 0, 0), cv.FILLED)
            cv.circle(img, (x2, y2), 18, (255, 0, 0), 2)
            cv.circle(img, (x3, y3), 10, (255, 0, 0), cv.FILLED)
            cv.circle(img, (x3, y3), 18, (255, 0, 0), 2)
            cv.putText(img,str(int(angle)),(x2,y2-15), cv.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)

        return int(angle)
def main():
    cap = cv.VideoCapture(0)
    detector = poseDetector()
    while True:
        start = cv.getTickCount()
        success, img = cap.read()
        img = cv.flip(img, 1)
        if not success:
            break

        img1 = detector.findPose(img, draw = True)
        lmList = detector.findPosition(img1, draw = True)
        img = detector.findAngle(img,7,0,8,True)
        print(lmList[2])
        end = cv.getTickCount()
        fps = cv.getTickFrequency() / (end - start)
        cv.putText(img, 'FPS: ' + str(int(fps)), org=(20, 30), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=2,
                   color=(0, 255, 0), thickness=2)
        cv.namedWindow('Video', cv.WINDOW_NORMAL)
        cv.imshow('Video', img)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv.destroyAllWindows()
if __name__ == '__main__':
    main()