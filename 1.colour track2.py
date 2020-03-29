import cv2
import numpy as np

device=cv2.VideoCapture(0)

def nothing(x):
    pass

#trackbar
cv2.namedWindow("trackbar")
cv2.createTrackbar("L-H","trackbar",0,179,nothing)
cv2.createTrackbar("L-S","trackbar",0,255,nothing)
cv2.createTrackbar("L-V","trackbar",0,255,nothing)
cv2.createTrackbar("U-H","trackbar",179,179,nothing)
cv2.createTrackbar("U-S","trackbar",255,255,nothing)
cv2.createTrackbar("U-V","trackbar",255,255,nothing)

while True:
    ret,frame =device.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)    
    #cv2.imshow("frame",frame)

    l_h=cv2.getTrackbarPos("L-H","trackbar")
    l_s=cv2.getTrackbarPos("L-S","trackbar")
    l_v=cv2.getTrackbarPos("L-V","trackbar")
    h_h=cv2.getTrackbarPos("U-H","trackbar")
    h_s=cv2.getTrackbarPos("U-S","trackbar")
    h_v=cv2.getTrackbarPos("U-V","trackbar")
    print(l_h,l_s,l_v,h_h,h_s,h_v)
    low=np.array([l_h,l_s,l_v])
    high=np.array([h_h,h_s,h_v])

    mask=cv2.inRange(hsv,low,high) 
    result=cv2.bitwise_and(frame,frame,mask=mask)    

    cv2.imshow("result",result)

    if cv2.waitKey(25)  & 0xFF==ord('q'):
           break

device.release()
cv2.destroyAllWindows()
