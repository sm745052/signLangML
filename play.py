import cv2
import numpy as np
import os
import speech_recognition as sr  
import os
import keyboard

def show(x):
    cap = cv2.VideoCapture('.\sign_images\{}'.format(x))
    
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video  file")
    
    # Read until video is completed
    while(cap.isOpened()):
        
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
        
            # Display the resulting frame
            cv2.imshow('signs', frame)
        
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            # Press enter on keyboard to  exit
            if keyboard.is_pressed("tab"):
                break
    
        # Break the loop
        else: 
            break
    
    # When everything done, release 
    # the video capture object
    cap.release()
   
# Closes all the frames
# cv2.destroyAllWindows()

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

try:
    text = (r.recognize_google(audio))
    print(text)
    splitted_text = text.split(' ')
    for i in splitted_text:
        for j in os.listdir('./sign_images/'):
            if j[:-4] == i:
                show(j)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))


