import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../python_openCV/img/girl.jpg")

plt.imshow(img)
plt.show()
#  BGR 순서라서 색상이 좀 이상한다

# BGR -> RGB  [:,:,::-1]
