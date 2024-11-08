import threading

import cv2 
from deepface import Deepface

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cve.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cve.CAP_PROP_FRAME_WIDTH, 480)

counter = 0
face_match = False
refernece_img = cv2.imread("reference.jpg")

def check_face(frame):
    global face_match
    try:
        if Deepface.verify(frame, refernece_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False

while True:
    if ret:
        if counter % 30 == 0:
            try: 
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass 
        counter+= 1

        if face_match:
            cv2.putText(frame, "MATCH", (20, 450), CV2.font_HERSHEY_SIMPLEX,2,(0,255,0),3)
        else:
             cv2.putText(frame, "MATCH", (20, 450), CV2.font_HERSHEY_SIMPLEX,2,(0,0,255),3)


    key = cv2.waitKey(1)
    if key == ord("q"):
          break
    
cv2.destroyALLWindows()
    
