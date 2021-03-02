import cv2
img_file = "../python_openCV/img/girl.jpg"
img = cv2.imread(img_file)

if img is not None :
    cv2.imshow("사진 출력 예제",img)
    cv2.waitKey()
    cv2.destroyALLWindows()
else:
    print("no image file.")
