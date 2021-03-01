import numpy as np
#0으로 채워진 2행5열짜리 배열
a = np.zeros((2,5), np.uint8)

# 1로 채워진 3행1열짜리 배열 uint8 : 부호없는 8비트 정수형
b = np.ones((3,1),np.uint8)

# 값이 없는 1행 5열짜리 배열. 자료의 크기는 64비트
c = np.empty((1,5), np.float64)

#배열을 원하는 숫자로 모두 채우기
d = np.full((3,4),20, np.float32)
