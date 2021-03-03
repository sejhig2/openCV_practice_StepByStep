# 4_3에서 함수 만드는게 꽤나 힘들었다. 제공해주는 함수를 사용해서 조금 더 쉽고 간편하게 구현해보자.

import cv2
import numpy as np

img = cv2.imread("../python_openCV/img/sunset.jpg")
x,y,w,h = cv2.selectROI('IMG',img,False) # x,y 좌표와 높이, 너비
if w==True and h == True :
    roi = img[y:y+h, x:x+w]
    cv2.imshow("cropped",roi)
    cv2.moveWindow("cropped",0,0)
    cv2.imwrite("../python_openCV/img/cropped2,jpg")
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()