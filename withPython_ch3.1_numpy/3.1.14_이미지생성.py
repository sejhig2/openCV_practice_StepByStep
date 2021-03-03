# 간단한 이미지를 생성해보자
import cv2
import numpy as np

img = np.zeros((120,120), dtype = np.uint8) # 크기는 120x120
img[25:35,:] = 45 # 이미지에 선 긋기 ( 가로 줄 )
img[55:65, : ] = 255
img[85:95,:] = 130

img[:,35:45] = 200 # 이미지에 선 긋기 ( 세로 줄 )
img[:,95:105] = 80
#윈도우 창에 표시하기
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows() # 모든 창 닫기
