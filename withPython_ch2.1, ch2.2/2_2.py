import cv2

img_file = "../python_openCV/img/girl.jpg"
img = cv2.imread(img_file,  cv2.IMREAD_GRAYSCALE)

if img is not None :
    cv2.imshow("IMAGE", img)
    cv2.waitKey()
    cv2.destroyWindow()
else:
    print("NO!")