import cv2
import numpy as np

# bgr 컬러 스페이스로 원색 픽셀 생성
red_bgr = np.array([[[0,0,255]]], dtype = np.uint8 ) # 빨강 값만 갖는 픽셀
green_bgr = np.array([[[0,255,0]]], dtype = np.uint8 ) # 초록
blue_bgr = np.array([[[255,0,0]]], dtype = np.uint8 ) # 파랑
yellow_bgr = np.array([[[0,255,255]]], dtype = np.uint8 ) # 노랑 값만 같는 픽셀

print("red:", red_bgr)
print("green:", green_bgr)
print("blue:", blue_bgr)
print("yellow:", yellow_bgr)

# BGR 컬러 스페이스를 HSV 컬러 스페이스로 변환
print("BGR -> color space 로 바꿨을 때: \n배열의 값이 어떻게 바뀌는지 눈으로 확인")
red_hsv = cv2.cvtColor(red_bgr, cv2.COLOR_BGR2HSV)
green_hsv = cv2.cvtColor(green_bgr, cv2.COLOR_BGR2HSV)
blue_hsv = cv2.cvtColor(blue_bgr, cv2.COLOR_BGR2HSV)
yellow_hsv = cv2.cvtColor(yellow_bgr, cv2.COLOR_BGR2HSV)

# HSV로 변환한 픽셀 출력
print( "red:", red_hsv)
print( "green:", green_hsv)
print( "blue:", blue_hsv)
print( "yellow:", yellow_hsv)