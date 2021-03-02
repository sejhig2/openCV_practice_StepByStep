import cv2

video_file = "../python_openCV/img/big_buck.avi"

cap = cv2.VideoCapture(video_file) # 동영상 갭쳐 객체 생성
if cap.isOpened():
    # 프레임 수 구하기
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps) # 구한 프레임으로 지연시간 설정해주기. 30페이지 참고
    
    print("fps: %f, Delay:%dms"%(fps,delay))

    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(delay)
        else:
            break
else :
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()