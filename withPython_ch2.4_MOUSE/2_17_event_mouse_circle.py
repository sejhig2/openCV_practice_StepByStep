# 1. esc 키를 눌렀을 때 종료 시키기
# 2. 마우스를 클릭했을 때 이벤트가 발생하도록 함수 짜기
# 3. 각종 도형을 그리는 방법.
# 4. 마우스의 위치에 도형이 그려지도록
# 5. 마우스 이벤트 함수를 호출해서 사용하는 방법법import cv2

title = "moust event" # 창 제목
img = cv2.imread("../python_openCV/img/blank_500.jpg") # 흰색 배경 불러온다. 여기다가 그럴 것이다.
cv2.imshow(title, img) # 흰색 이미지를 창으로 표현

def onMouse(event, x,y , flag, param): # 마우스가 클릭 됐을 때 구현될 콜백 함수
    print(event,x,y,) # 파라미터가 콘솔에 표현 되도록 하자  (위치(x,y 좌표)를 표시)
    if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼을 눌렸을 경우
        cv2.circle(img,(x,y), 30, (10,20,250), -1)  # 지금30짜리의 원을 그리기
        cv2.imshow(title, img) # 그린 것을 img에 표시
cv2.setMouseCallback(title, onMouse) # 마우스 콜백 함수를 GUI 윈도우에 등록

while True :
    if cv2.waitKey(0) & 0xFF == 27: #esc로 종료
        break
    cv2.destroyAllWindows() # 위에서 esc눌렀을 때 모두 닫기