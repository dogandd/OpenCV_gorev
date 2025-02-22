import cv2
import numpy as np

img = cv2.imread("D:\\Resimler\\coins1.jpeg")

img = cv2.resize(img,(600,600))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_blur = cv2.medianBlur(gray,15)

circles = cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/5.5,param1 = 200,param2 = 10,minRadius=40,maxRadius=110)
if circles is not None:
    circles = np.uint16(np.around(circles))
    circle_num = 0
    for i in circles[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        circle_num += 1

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img,f"cember sayisi:{circle_num}",(300,40),font,1,(0,0,0),cv2.LINE_4)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()