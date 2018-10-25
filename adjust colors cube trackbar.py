import cv2
import numpy as np

cap=cv2.VideoCapture(0)

def nothing(x):
    pass

##trackbars
#red-track
cv2.namedWindow("red-track")
cv2.createTrackbar("L-H","red-track",0,179,nothing)
cv2.createTrackbar("L-S","red-track",150,255,nothing)
cv2.createTrackbar("L-V","red-track",0,255,nothing)
cv2.createTrackbar("U-H","red-track",8,179,nothing)
cv2.createTrackbar("U-S","red-track",255,255,nothing)
cv2.createTrackbar("U-V","red-track",255,255,nothing)

#orange-track
cv2.namedWindow("orange-track")
cv2.createTrackbar("L-H","orange-track",12,179,nothing)
cv2.createTrackbar("L-S","orange-track",104,255,nothing)
cv2.createTrackbar("L-V","orange-track",171,255,nothing)
cv2.createTrackbar("U-H","orange-track",26,179,nothing)
cv2.createTrackbar("U-S","orange-track",255,255,nothing)
cv2.createTrackbar("U-V","orange-track",255,255,nothing)

#blue-track
cv2.namedWindow("blue-track")
cv2.createTrackbar("L-H","blue-track",90,179,nothing)
cv2.createTrackbar("L-S","blue-track",122,255,nothing)
cv2.createTrackbar("L-V","blue-track",211,255,nothing)
cv2.createTrackbar("U-H","blue-track",128,179,nothing)
cv2.createTrackbar("U-S","blue-track",255,255,nothing)
cv2.createTrackbar("U-V","blue-track",255,255,nothing)

#green-track
cv2.namedWindow("green-track")
cv2.createTrackbar("L-H","green-track",45,179,nothing)
cv2.createTrackbar("L-S","green-track",100,255,nothing)
cv2.createTrackbar("L-V","green-track",151,255,nothing)
cv2.createTrackbar("U-H","green-track",62,179,nothing)
cv2.createTrackbar("U-S","green-track",255,255,nothing)
cv2.createTrackbar("U-V","green-track",255,255,nothing)

#yellow-track
cv2.namedWindow("yellow-track")
cv2.createTrackbar("L-H","yellow-track",25,179,nothing)
cv2.createTrackbar("L-S","yellow-track",62,255,nothing)
cv2.createTrackbar("L-V","yellow-track",186,255,nothing)
cv2.createTrackbar("U-H","yellow-track",44,179,nothing)
cv2.createTrackbar("U-S","yellow-track",255,255,nothing)
cv2.createTrackbar("U-V","yellow-track",255,255,nothing)

while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX


    l_h1=cv2.getTrackbarPos("L-H","red-track")
    l_s1=cv2.getTrackbarPos("L-S","red-track")
    l_v1=cv2.getTrackbarPos("L-V","red-track")
    h_h1=cv2.getTrackbarPos("U-H","red-track")
    h_s1=cv2.getTrackbarPos("U-S","red-track")
    h_v1=cv2.getTrackbarPos("U-V","red-track")


    l_h2=cv2.getTrackbarPos("L-H","orange-track")
    l_s2=cv2.getTrackbarPos("L-S","orange-track")
    l_v2=cv2.getTrackbarPos("L-V","orange-track")
    h_h2=cv2.getTrackbarPos("U-H","orange-track")
    h_s2=cv2.getTrackbarPos("U-S","orange-track")
    h_v2=cv2.getTrackbarPos("U-V","orange-track")
    


    l_h3=cv2.getTrackbarPos("L-H","blue-track")
    l_s3=cv2.getTrackbarPos("L-S","blue-track")
    l_v3=cv2.getTrackbarPos("L-V","blue-track")
    h_h3=cv2.getTrackbarPos("U-H","blue-track")
    h_s3=cv2.getTrackbarPos("U-S","blue-track")
    h_v3=cv2.getTrackbarPos("U-V","blue-track")


    l_h4=cv2.getTrackbarPos("L-H","green-track")
    l_s4=cv2.getTrackbarPos("L-S","green-track")
    l_v4=cv2.getTrackbarPos("L-V","green-track")
    h_h4=cv2.getTrackbarPos("U-H","green-track")
    h_s4=cv2.getTrackbarPos("U-S","green-track")
    h_v4=cv2.getTrackbarPos("U-V","green-track")

    
    l_h5=cv2.getTrackbarPos("L-H","yellow-track")
    l_s5=cv2.getTrackbarPos("L-S","yellow-track")
    l_v5=cv2.getTrackbarPos("L-V","yellow-track")
    h_h5=cv2.getTrackbarPos("U-H","yellow-track")
    h_s5=cv2.getTrackbarPos("U-S","yellow-track")
    h_v5=cv2.getTrackbarPos("U-V","yellow-track")

    
    #print(l_h,l_s,l_v,h_h,h_s,h_v)
    
    #blue

    low_blue=np.array([l_h3,l_s3,l_v3])
    high_blue=np.array([h_h3,h_s3,h_v3])
    mask1=cv2.inRange(hsv,low_blue,high_blue)
    blur1=cv2.GaussianBlur(mask1,(15,15),0)
    _,contours1,_=cv2.findContours(blur1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour1 in contours1:
        area1=cv2.contourArea(contour1)
        
        if area1>7000:
            print(area1)
            cv2.drawContours(frame,contour1,-1,(255,0,0),3)
            print("BLUE")
            cv2.putText(frame,'BLUE',(240,50), font, 2,(255,0,0),2,cv2.LINE_AA)       
            break    
    #Red
    low_red=np.array([l_h1,l_s1,l_v1])
    high_red=np.array([h_h1,h_s1,h_v1])

    mask2=cv2.inRange(hsv,low_red,high_red)
    blur2=cv2.GaussianBlur(mask2,(15,15),0)
    _,contours2,_=cv2.findContours(blur2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour2 in contours2:
        area2=cv2.contourArea(contour2)

        if area2>7000:
            cv2.drawContours(frame,contour2,-1,(0,0,255),3)
            print("RED")
            cv2.putText(frame,'RED',(240,200), font, 2,(0,0,255),2,cv2.LINE_AA)       
            break
    #Green
        

    low_green=np.array([l_h4,l_s4,l_v4])
    high_green=np.array([h_h4,h_s4,h_v4])
    mask3=cv2.inRange(hsv,low_green,high_green)
    blur3=cv2.GaussianBlur(mask3,(15,15),0)
    _,contours3,_=cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour3 in contours3:
        area3=cv2.contourArea(contour3)

        if area3>7000:
            cv2.drawContours(frame,contour3,-1,(0,255,0),3)
            print("GREEN")
            cv2.putText(frame,'GREEN',(240,300), font, 2,(0,255,0),2,cv2.LINE_AA)       
            break
    #orange
    
    low_or=np.array([l_h2,l_s2,l_v2])
    high_or=np.array([h_h2,h_s2,h_v2])

    mask4=cv2.inRange(hsv,low_or,high_or)
    blur4=cv2.GaussianBlur(mask4,(15,15),0)
    _,contours4,_=cv2.findContours(blur4,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour4 in contours4:
        area4=cv2.contourArea(contour4)

        if area4>7000:
            cv2.drawContours(frame,contour4,-1,(0,140,255),3)
            print("orange")
            cv2.putText(frame,'ORANGE',(240,400), font, 2,(0,140,255),2,cv2.LINE_AA)       
            break
    #yellow
    
    low_ye=np.array([l_h5,l_s5,l_v5])
    high_ye=np.array([h_h5,h_s5,h_v5])

    mask5=cv2.inRange(hsv,low_ye,high_ye)
    blur5=cv2.GaussianBlur(mask5,(15,15),0)
    _,contours5,_=cv2.findContours(blur5,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour5 in contours5:
        area5=cv2.contourArea(contour5)

        if area5>7000:
            cv2.drawContours(frame,contour5,-1,(0,215,255),3)
            print("yellow")
            cv2.putText(frame,'YELLOW',(240,500), font, 2,(0,255,255),2,cv2.LINE_AA)       
            break

    cv2.imshow("frame",frame)
##    cv2.imshow("mask",mask2)
    if cv2.waitKey(1)==27:#press esc to exit
        break;

cap.release()
cv2.destroyAllWindows()
