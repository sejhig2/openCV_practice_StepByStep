import cv2
import numpy as np

img = cv2.imread("../python_openCV/img/sunset.jpg")

x = 320; y = 150; w=50; h =50 # roi영역으로 잡을 좌표
roi = img[y:y+h, x:x+w] # roi 좌표를 지정하기 위해 범위로 배열 만들기
print(roi.shape)
img2 = roi.copy() # roi 배열 복제
roi = img[y:y+h, x:x+w , x:x+w+w] # 새로운 좌표에 roi추가, 태양 2개 만들기
cv2.rectangle(img, (x,y),(x+w+w, y+h),(0,255,0)) # 2개의 태양 영역에 사각형 표시
cv2.imshow('img',img)
cv2.imshow('roi',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()