# 다각형을 그릴때는 2차원 배열을 사용한다! 주의해야해

import cv2
import numpy as np

img = cv2.imread("../python_openCV/img/blank_500.jpg")

# 선으로 번개모양 그려보자
# 별을 그리기 위해선 꼭지점의 좌표를 찍어줘야지
pts1 = np.array([[50,50],[150,150],[100,140],[200,240]], dtype = np.int32)
# 별을 그려내자
cv2.polylines(img, [pts1], False, (255,0,0))

# 삼각형을 그려보자 -
#삼각형 좌표
pts2 = np.array([[350,50],[250,200],[450,200]], dtype = np.int32)
#그려내기
#cv2.polylines(img, [pts2], False, (150,0,0))
cv2.polylines(img, [pts2], True, (50,50,120), 20)
# False : 닫히지 않은 삼각형

# 5각형 그려보기
pts4 = np.array([[350,250],[450,350],[400,450],[300,450],[250,350]], dtype = np.int32)
#그려내기
cv2.polylines(img, [pts4], True, (50,50,50), 10)
# True : 닫힌 다각형 ( False : 닫히지 않은 다각형)


cv2.imshow("polyline draw", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

