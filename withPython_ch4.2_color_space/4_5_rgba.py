import cv2
import numpy as np

img = cv2.imread("../python_openCV/img/opencv_logo.png") # 기본 값 옵션
bgr = cv2.imread("../python_openCV/img/opencv_logo.png",cv2.IMREAD_COLOR) # 컬러 옵션
bgra = cv2.imread("../python_openCV/img/opencv_logo.png", cv2.IMREAD_UNCHANGED)

print("default", img.shape, "color:",bgr.shape, "unchanged:",bgra.shape)


cv2.imshow("bgr",bgr)
cv2.imshow("bgra",bgra)
cv2.imshow("alpha",bgra[:,:,3]) # 알파(투명도) 채널만 표시
cv2.waitKey(0)
cv2.destroyAllWindows()