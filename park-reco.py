import sys
sys.path.append('/home/suganth/project-expo/sub-programs')

import numpy as np
import cv2
import Core

cap = cv2.VideoCapture(0)

i,j = 0,14
while(i<j):

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    Core.main(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i+=1

cap.release()
cv2.destroyAllWindows()
