import cv2
import numpy as np

img = cv2.imread("../python_openCV/img/sunset.jpg")

x = 320; y = 150; w=50; h =50 # roi영역으로 잡을 좌표
roi = img[y:y+h, x:x+w] # roi 좌표를 지정하기 위해 범위로 배열 만들기
print(roi.shape)

# 사각형 그려내기
cv2.rectangle(roi,(0,0),(h-1, w-1),(0,255,0))
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()