import numpy as np

a = np.empty((2,3))
print(a)
print(a.dtype)

a.fill(255)
print(a)

b= np.zeros((2,3))
print(b)

# 자료형을 지정해서 만들기
# 0으로 채우기
c = np.zeros((2,3), dtype = np.int8)
print(c)

# 1로 채우기
d = np.ones((2,3), dtype = np.int8)
print(d)

# 3차원 배열 만들기
e = np.full((2,3,4), 255 , dtype = np.uint8)
print(e)
# 1. 깊이 : 2, 가로x세로 : 3x4
# 2. 자료형 : unsigned 8bit integer

# 있던 자료의 크기 활용하기
# 이미지랑 같은 크기지만 값은 다른 배열 만들기

import cv2

img = cv2.imread("../python_openCV/img/girl.jpg")
print(img.shape)

a = np.empty_like(img)
print(a)

b = np.zeros_like(img)
print(b)

c = np.ones_like(img)
print(c)

d = np.full_like(img, 255)
print(d)