import cv2
import time
import math
import numpy as np
import HandTracking as htrack

#initializing window width & height
camWidth = 840
camHeight = 640

#capturing the video stream from the camera
frame = cv2.VideoCapture(0)
frame.set(3,camWidth)
frame.set(4,camHeight)
ptime = 0 #presentTime


#create object for our HandTracking class
detector = htrack.handTracking(detect_conf=0.7)

#################################################
#pycaw for volume control. github- https://github.com/AndreMiras/pycaw

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
 #value of volumne as 0 ---> 100 (as system vol value)
# value (-10) as 51, so more the lesser values(in negative) greater is our system vol value.
volbar = 400
barPer = 0
vol = 0
minVol = volRange[0]
maxVol = volRange[1]
#vol range = -65 to 0


#################################################

while True:
    success,img = frame.read()
    handImage = detector.detectHands(img)
    lmList = detector.FindPosition(handImage,draw=False) #lmList has all the values for 21 different points in form of (x,y) coordinates
    #print("detection value points as x,y",lmList)
    #print("totol no of detections we are able to get as:",len(lmList))
    if len(lmList)!=0:
        print(lmList[4],lmList[8])

        x1,y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(handImage,(x1,y1),10,(255,0,255),cv2.FILLED)
        cv2.circle(handImage,(x2,y2),10,(255,0,255),cv2.FILLED)
        cv2.line(handImage,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(handImage,(cx,cy),10,(255,0,255),cv2.FILLED)


        length = math.hypot(x2-x1,y2-y1)
        print("Value of  length",length)
        #hand range is taken as 50-200. it can vary according the to focal length of camera.
        vol = np.interp(length,[25,200],[minVol,maxVol])
        #print("hi i am volume",vol)
        barPer = np.interp(length,[25,200],[0,100])
        volbar = np.interp(length, [25, 200], [400, 150])
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(handImage,(cx,cy),10,(0,0,255),cv2.FILLED)


    cv2.rectangle(handImage,(50,150),(85,400),(0,0,255),3)
    cv2.rectangle(handImage,(50,int(volbar)),(85,400),(102,102,255),cv2.FILLED)
    cv2.putText(handImage,f'{int(barPer)}%',(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
    #calculate Frame per second value
    ctime = time.time()
    FPS = 1/(ctime - ptime)
    ptime = ctime

    cv2.putText(img,f'FPS: {int(FPS)}',(40,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
    cv2.imshow("Volume control",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
