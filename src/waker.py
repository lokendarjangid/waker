#!/home/lokendar/Desktop/python/waker/.venv/bin/python3

import cv2
import time
import os
from face import Face

cap = cv2.VideoCapture(0)
face_detector = Face()

screen_off = False
os.system("xset s 60")
os.system("xset dpms force off")
os.system("xset s blank")


while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Check if there's any face in the frame
    if face_detector.isface(frame=frame):
        last_face_time = time.time()
        face_detected = True

        if screen_off == True and face_detected == True:
            print("Face detected. Waking up computer...")
            os.system("xset s 60")
            os.system("xset dpms force off")
            os.system("xset s blank")
            # time.sleep(4)
            screen_off = False

    else:
        face_detected = False

    if not face_detected and time.time() - last_face_time > 7 and screen_off == False:
        print("No face detected for 60 seconds. Minimizing windows and putting computer to sleep...")
        time.sleep(4)
        screen_off = True
        os.system("xset dpms force on")
        os.system("xset s reset")
        os.system("systemctl suspend -i")

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


os.system("xset dpms force on")
os.system("xset s reset")
cap.release()
cv2.destroyAllWindows()
