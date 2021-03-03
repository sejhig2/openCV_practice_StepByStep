# 2.4.3 트랙바
# 알아야 할 것 1. 트랙바를 만드는 방법
# 알아야 할 것 2. 색을 변경하는 방법
# 알아야 할 것 3. 1+2, 트랙바의 위치에 따라 색을 변경하는 방법
import cv2
import numpy as np

win_name = "Trackbar"

img = cv2.imread("../python_openCV/img/blank_500.jpg")
cv2.imshow(win_name, img)

def onChange(x):
    print(x)

    r = cv2.getTrackbarPos("R", win_name)
    g = cv2.getTrackbarPos("G", win_name)
    b = cv2.getTrackbarPos("B", win_name)
    print(r,g,b)
    img[:] = [b,g,r]
    cv2.imshow(win_name, img)

cv2.createTrackbar("R", win_name, 255,255, onChange)
cv2.createTrackbar("G", win_name, 255,255, onChange)
cv2.createTrackbar("B", win_name, 255,255, onChange)

while True :
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()