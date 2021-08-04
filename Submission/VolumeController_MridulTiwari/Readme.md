
## Overview
This is an Elementry Volume Control App using Hand Gestures. The App has been Designed using OpenCv, Mediapipe & Pycaw which takes input using Webcam/USB-Camera and returns detection of hand gestures with certain points which are basically used for Decreasing/Increasing the volumne of the System.


## Technical Aspect
This App is divided into two part:
1. __HandTracking.py__ : This File is responsible for detecting 21 different points on our hand as shown in below Video File. All points are connected to one another and they do have some coordinate value as (x,y). Video Frames are fetched using webcam or device camera can also be used.
2. __VolumeControl.py__: Building App which could control volume of the system.
    - Frames which are fetched through webcam are passed one after the other for detection.
    - Corner Coordinates (X,Y) for Thumb and index finger are taken into consideration.
    - Volume is controlled using the distance between those points. More the distance higher the Volume and vice-versa.

## Installation
The HandGestureController App is coded in python version 3.6, with other libraries as pycaw, mediapipe, opencv-python and numpy. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). Upgrade using pip package if you are using any lower version. The dependencies are mentioned in the requirements.txt file. Go with the below mentioned command for installing them in one go.
```bash
pip install -r requirements.txt
```
