import cv2
import numpy as np

img = np.full((500,500,3), 0, dtype = np.uint8) # 500,500,3 에서 3은 뭐지? 모르면 찾아봐!
cv2.imwrite("../python_openCV/img/test_blank_500_hjh.jpg", img)