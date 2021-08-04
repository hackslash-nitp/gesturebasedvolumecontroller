# GestureBasedVolumeController <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px">
## Installing Dependencies 💻
---
pip install mediapipe 
---
pip install opencv-python
---

### This is an implementation of computer vision library "opencv" to make a gesture based volume controller which detects the hand landmarks using "mediapipe" library.

* The index and thumb are used to set the scale and by their movement we alter the volume level.
* The pinky is used to set the desired volume by being raised or bent.
* The application window terminates as soon as we remove our hand from staging area.
* The user may face some difficulties with the index numbers in setting up cv2.VideoCapture(0). In that case try 1 or 2 instead of 0.
* To install dependencies create a virtual env. in python version less than 3.9 and run <span style="background-color: #FFFF00">"$pip install -r requirements.txt"</span>.

Below is a working demo:-

![Image of Model](https://github.com/jhashivam-2001/gesturebasedvolumecontroller/blob/main/Submission/VolumeController_ShivamJha/volume_control.png)
