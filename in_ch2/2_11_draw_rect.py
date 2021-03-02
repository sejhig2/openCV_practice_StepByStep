import cv2

img = cv2.imread("../python_openCV/img/blank_500.jpg")

cv2.rectangle(img, (50,50), (150,150), (255,0,0), 15)
cv2.rectangle(img, (50,50), (150,150), (255,0,0), -1)
#1. 두께 :15 또는 채우기 : -1
#2. 시작 - 끝 위치 (50,50) , (150,150)
#3. 색상 rgb 250,0,0

cv2.imshow("rectangle_draw", img)
cv2.waitKey(0)
cv2.destroyAllWindows()