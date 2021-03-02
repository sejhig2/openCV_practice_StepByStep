import cv2
img = cv2.imread("../python_openCV/img/blank_500.jpg") # 이미지 불러오기 ( 이 위에다가 선 그릴거야 )
cv2.line(img, (50,50),(250,350),(50,0,100), 12, cv2.LINE_AA)
# 1. 시작 x,y(50,50) ~ 끝 x,y(250,350) 지점.
# 2. 두께 : 12
# 3. v2.LINE_AA : 안티엘리어싱 적용했다.
# 4. 0,0,100 : rgb


cv2.imshow("line draw window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()