import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX

    #blue
    low_blue=np.array([90,122,211])
    high_blue=np.array([128,255,255])
    mask1=cv2.inRange(hsv,low_blue,high_blue)
    blur1=cv2.GaussianBlur(mask1,(15,15),0)
    contours1,_=cv2.findContours(blur1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour1 in contours1:
        area1=cv2.contourArea(contour1)
        
        if area1>7000:
            print(area1)
            cv2.drawContours(frame,contour1,-1,(255,0,0),3)
            print("BLUE")
            cv2.putText(frame,'BLUE',(240,320), font, 2,(255,0,0),2,cv2.LINE_AA)       
    
    #Red
    
    low_red=np.array([123,88,209])
    high_red=np.array([179,255,255])
    mask2=cv2.inRange(hsv,low_red,high_red)
    blur2=cv2.GaussianBlur(mask2,(15,15),0)
    contours2,_=cv2.findContours(blur2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour2 in contours2:
        area2=cv2.contourArea(contour2)

        if area2>7000:
            cv2.drawContours(frame,contour2,-1,(0,0,255),3)
            print("RED")
            cv2.putText(frame,'RED',(240,320), font, 2,(0,0,255),2,cv2.LINE_AA)       
   
    #Green
        
    low_green=np.array([45,100,151])
    high_green=np.array([62,255,255])
    mask3=cv2.inRange(hsv,low_green,high_green)
    blur3=cv2.GaussianBlur(mask3,(15,15),0)
    contours3,_=cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour3 in contours3:
        area3=cv2.contourArea(contour3)

        if area3>7000:
            cv2.drawContours(frame,contour3,-1,(0,255,0),3)
            print("GREEN")
            cv2.putText(frame,'GREEN',(240,320), font, 2,(0,255,0),2,cv2.LINE_AA)       
   
    #orange
    
    low_or=np.array([12,104,171])
    high_or=np.array([26,255,255])
    mask4=cv2.inRange(hsv,low_or,high_or)
    blur4=cv2.GaussianBlur(mask4,(15,15),0)
    contours4,_=cv2.findContours(blur4,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour4 in contours4:
        area4=cv2.contourArea(contour4)

        if area4>7000:
            cv2.drawContours(frame,contour4,-1,(0,140,255),3)
            print("orange")
            cv2.putText(frame,'ORANGE',(240,320), font, 2,(0,140,255),2,cv2.LINE_AA)       
   
    #yellow
    
    low_ye=np.array([25,62,186])
    high_ye=np.array([44,255,255])
    mask5=cv2.inRange(hsv,low_ye,high_ye)
    blur5=cv2.GaussianBlur(mask5,(15,15),0)
    contours5,_=cv2.findContours(blur5,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour5 in contours5:
        area5=cv2.contourArea(contour5)

        if area5>7000:
            cv2.drawContours(frame,contour5,-1,(0,215,255),3)
            print("yellow")
            cv2.putText(frame,'YELLOW',(240,320), font, 2,(0,255,255),2,cv2.LINE_AA)       


    cv2.imshow("frame",frame)

    if cv2.waitKey(1)==27:#press esc to exit
        break;

cap.release()
cv2.destroyAllWindows()
