# 키를 눌렀을 때 이벤트 : 창 크기 수정. (안 되는 경우도 있다)

import cv2
file_path = "../python_openCV/img/girl.jpg"
img = cv2.imread(file_path)
img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

# 창 2개 만들자
cv2.namedWindow('origin', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("gray", cv2.WINDOW_NORMAL)

# 창 2개를 표시하자
cv2.imshow("origin", img)
cv2.imshow("gray", img_gray)

cv2.moveWindow("origin", 0,0)
cv2.moveWindow("gray", 100,100)

cv2.waitKey(0) # 키를 누르면 사이즈 변경
cv2.resizeWindow("origin", 100, 200)
cv2.resizeWindow("gray",100,100)

cv2.waitKey(0) # 아무키나 누르면
cv2.destroyWindow("gray") #gray 창 닫힌다.

cv2.waitKey(0) # 아무기나 누르면
cv2.destroyAllWindow() # 모든 창 닫힌다.