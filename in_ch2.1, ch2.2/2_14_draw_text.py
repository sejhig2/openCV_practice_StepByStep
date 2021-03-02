import cv2

img = cv2.imread("../python_openCV/img/blank_500.jpg")

cv2.putText(img, "Plain", (50,30), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0),2)
# 1. 색상 : (255,0,0)
# 2. 폰트 : FONT_HERSHEY_PLAIN
# 3. 위치 : (50,30)
# 4. 크기 : 3
# 5. 굵기 : 2
cv2.putText(img, "hello", (50,130), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0),3)
cv2.putText(img, "Hallo", (50,230), cv2.FONT_HERSHEY_DUPLEX, 5, (0,0,255),5)

cv2.imshow("draw_text",img)
cv2.waitKey(0)
cv2.destroyAllWindows()