# 창을 이동하는 것 같은 효과 ( 실제로는 창을 닫고 위치를 옮겨서 다시 띄우는 것)
import cv2

img_file = "../python_openCV/img/girl.jpg"
img = cv2.imread(img_file)
title = "IMG"
x,y = 100, 100

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x,y)
    key = cv2.waitKey(0) & 0xFF
    print(key, chr(key))
    if key == ord('h'):
        x = x -10
    elif key == ord('j'):
        y = y+10
    elif key == ord('k'):
        y = y-10
    elif key == ord('l'):
        x = x+10
    elif key == ord('q') or key == 27: # 27 :  esc 키
        break
        cv2.destroyAllWindows()
    cv2.moveWindow(title, x, y)
