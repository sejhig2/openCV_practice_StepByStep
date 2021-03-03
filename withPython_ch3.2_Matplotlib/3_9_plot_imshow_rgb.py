import cv2
import matplotlib.pyplot as plt
# 색상 순서 뒤집기
# BGR -> RGB  [:,:,::-1]

img = cv2.imread("../python_openCV/img/girl.jpg")

plt.imshow(img[:,:,::-1])
plt.xticks([])
plt.yticks([])
plt.show()