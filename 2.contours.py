import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    low=np.array([90,122,211])
    high=np.array([179,255,255])
    mask=cv2.inRange(hsv,low,high)
    blur=cv2.GaussianBlur(mask,(15,15),0)
    contours,_=cv2.findContours(blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area=cv2.contourArea(contour)
##      print (area)
        if area>3000:
            cv2.drawContours(frame,contour,-1,(255,0,0),3)
   
##    print("number of contours=%d"%len(contours))
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    
    if cv2.waitKey(1)==27:#press esc to exit
        break;

cap.release()
cv2.destroyAllWindows()
