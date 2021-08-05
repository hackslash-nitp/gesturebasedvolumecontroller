import cv2
import mediapipe as mp
import time


class handTracking:
    def __init__(self,mode=False,max_num_hands=2,detect_conf=0.5,track_conf=0.5):
        self.mode = mode
        self.max_hands = max_num_hands
        self.detec_conf = detect_conf
        self.track_conf = track_conf


        self.MPHands = mp.solutions.hands
        self.hands = self.MPHands.Hands(static_image_mode=self.mode,max_num_hands=2,min_detection_confidence=self.detec_conf,min_tracking_confidence=self.track_conf)
        self.drawMP = mp.solutions.drawing_utils



    def detectHands(self,img,Draw=True):
        imageRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)
        #print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for hnd in self.results.multi_hand_landmarks:
                if Draw:
                    #self.drawMP.draw_landmarks(img, hnd) --> This will draw only points i.e 21 in total over the hands.
                    self.drawMP.draw_landmarks(img, hnd, self.MPHands.HAND_CONNECTIONS) #This will draw the points and will draw connections also.


        return img

    def FindPosition(self,img,handNo=0,draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[handNo]


            for id, lm in enumerate(myhand.landmark):
                #print(id,lm)
                height,width,channels = img.shape
                centerX, centerY = int(lm.x*width), int(lm.y*height)
                lmList.append([id,centerX,centerY])
                #print(id,centerX,centerY)

                if draw:
                    cv2.circle(img,(centerX,centerY),10,(255,0,255),cv2.FILLED)

        return lmList




def main():
    pTime = 0
    cTime = 0
    frame = cv2.VideoCapture(0)
    detector = handTracking()

    while True:
        success, img = frame.read()
        img = detector.detectHands(img,Draw=True)
        lmlist = detector.FindPosition(img,draw=False)
        if len(lmlist)!=0:
            print(lmlist[4])


        cTime = time.time()
        FPS = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(FPS)), (10, 80), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
        cv2.imshow("Hand Tracking", img)
        cv2.waitKey(1)






if __name__ == '__main__':
    main()
