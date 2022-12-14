import cv2 
import time 
import numpy as np 
#Starting up the webcam
cap = cv2.VideoCapture(0)
image = cv2.imread("famousplace.jpg")
#Reading the captured frame until the camera is open 
while True:
    ret,img=cap.read()
    print(img)
    img = cv2.resize(img,(640,480))
    image = cv2.resize(img,(640,480))
    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])
    mask_1 = cv2.inRange(img,l_black,u_black)
    #Keeping only the part of the image without the red color
    res_1 = cv2.bitwise_and(img,img,mask=mask_1)
    f = img-res_1
    f= np.where(f==0,image,f)
    #Display this output to the user
    cv2.imshow("magic",img)
    cv2.imshow("mask_1",f)
    if  cv2.waitKey(1) and 0xffFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
