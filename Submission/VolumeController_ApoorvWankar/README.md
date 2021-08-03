
# Volume control system using gestures

In this project we are using Gesture Control to change the volume of a computer. We first look into hand tracking and then we will use the hand landmarks to find gesture of our hand to change the volume. You can control the volume of your PC/MAC using this project.


## Run Locally

Clone the project

```bash
  git clone https://github.com/apoorvwankar/crispy-engine.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install opencv-python
  pip install mediapipe
  pip install autopy
```

Run the program.


  
## Note

If you face any type of issue with the webcam, try changing the following value in the python file.

```bash
  cv2.Videocapture(0)
```

  Try incrementing the value '0' until you see your webcam.
  
  
  Screenshot:
  ![Screenshot 2021-08-03 221738](https://user-images.githubusercontent.com/74948909/128076548-62bc20f4-0445-4ea0-9c98-2c4a31ed10eb.png)

