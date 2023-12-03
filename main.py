import cv2
import mediapipe as mp
import time
#this is for the camera to work
cap = cv2.VideoCapture(1)

#these for traking the hand but still just variables
mpHands = mp.solutions.hands
hands = mpHands.Hands()

#variable to trak the hand by using points (from the built in function)
mpDraw = mp.solutions.drawing_utils

#variables for the FPS
previousTime = 0
currentTime = 0

#this whole loop is for the camera to work
while True:
    success, img = cap.read()
    #traking colour to trak the hand movements
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #hand dedction
    results = hands.process(imgRGB)

    #if the hand dedected then..
    if results.multi_hand_landmarks:
        #for handLms means for a single hand then do..
        for handLms in results.multi_hand_landmarks:
            #lm for the land makr and id will show the number of each point of the hand so we can interpert it later
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)

                #three variables to get postion to track the land marks
                height, width, channel = img.shape


                #x and y coordinates to track the land marks
                cx, cy= int(lm.x * width), int(lm.y * height)


                #now we can choose which land mark we will manipulate and I will chose land mark 12

                #highlight landmark number 12

                #if id == 12:
                #    cv2.circle(img, (cx, cy), 20, (100, 69, 69), cv2.FILLED)

                    #cv2.putText(img, "2ere fek Hemo", (30, 150), cv2.FONT_ITALIC, 1, (0, 0, 0), 3)

                    #print("2ere fek nezar")






            #this will make the points follow the hand
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)



    #print(results.multi_hand_landmarks)

    #this is to show fps
    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime
    #and this is for how do I you want to display the FPS
    cv2.putText(img, str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255) , 3)





    cv2.imshow("image", img)
    cv2.waitKey(1)





