import cv2

video_file = "../python_openCV/img/big_buck.avi"

cap = cv2. VideoCapture(video_file)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(1000)
        else:
            break
else :
    print("cant't open video.")
cap.release()
cv2.destroyAllWindows()