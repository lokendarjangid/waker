#!/home/lokendar/Desktop/python/waker/.venv/bin/python3

import cv2
import time
import atexit
import os
from face import Face

cap = cv2.VideoCapture(0)
face_detector = Face()

screen_off = False
os.system("gsettings set org.gnome.desktop.session idle-delay 0")



while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Check if there's any face in the frameos.system("xset s off")
    if face_detector.isface(frame=frame):
        last_face_time = time.time()
        face_detected = True

        if screen_off == True and face_detected == True:
            print("Face detected. Waking up computer...")
            os.system("gsettings set org.gnome.desktop.session idle-delay 0")
            # time.sleep(4)
            screen_off = False

    else:
        face_detected = False

    if not face_detected and time.time() - last_face_time > 7 and screen_off == False:
        print("No face detected for 60 seconds. Minimizing windows and putting computer to sleep...")
        time.sleep(4)
        screen_off = True
        os.system("gsettings set org.gnome.desktop.session idle-delay 300")
        os.system("systemctl suspend -i")

    atexit.register(os.system,"gsettings set org.gnome.desktop.session idle-delay 300")
    #cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


os.system("gsettings set org.gnome.desktop.session idle-delay 300")
cap.release()
cv2.destroyAllWindows()
