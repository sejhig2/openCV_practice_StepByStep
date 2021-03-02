import numpy as np
import cv2

image = np.zeros((200,300), np.uint8)
image.fill(255) # 모든 원소를 255 흰색으로 지정

title1, title2 = "AUTOSIZE","NORMAL"
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) # 윈도우 생성 후 크기 변경 불가
cv2.namedWindow(title2, cv2.WINDOW_NORMAL) # 변경 가능

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400,300) # 윈도우 크기 강제 변경
cv2.resizeWindow(title2, 400,300)
cv2.waitKey(0)
cv2.destroyAllwindow()