# OpenCV
Human Interaction to change volume in Windows OS

# Prerequisites:
-You need a Camera and if you have multiple cameras you can switch to any camera installed on your PC by changing the line 26 "cap = cv2.VideoCapture(0)" to "cap = cv2.VideoCapture(1)" or any number as you wish. 
-You need to install CV2 and Numpy libraries.

#Usage
-Ensure your webcam is connected and accessible.
-A window will open showing the webcam feed with hand landmarks tracked.
-Landmarks will be displayed as filled circles (with color of your choice) on the hand and connected by lines to represent hand movement.
-the distance between the user's thumb and index finger will increase or decrease the volume on your PC.

#Note: 
You can uncomment specific sections of the code (e.g., marking a particular landmark) to experiment with different functionalities.
