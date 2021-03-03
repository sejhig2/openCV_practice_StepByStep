import cv2

img = cv2.imread("../python_openCV/img/blank_500.jpg")

# 원 그리기. 원점(150,150), 반지름 100
cv2.circle(img, (150,150), 100, (100,100,100),10)
cv2.circle(img, (50,50), 50, (200,100,100), 5)

#반원 그리기
cv2.ellipse(img, (150,300), (90,40), 0,181, 300, (255,0,0))
#1. 181, 300 : 시작 각~ 끝 각
#2. (90,40) : 타원을 그릴 때 사용
#3. 0,181,300 에서 0 : 기울기를 줄 때 사용


cv2.imshow("circle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()