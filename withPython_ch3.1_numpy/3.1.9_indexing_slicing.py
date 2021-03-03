import numpy as np
b= np.arange(12).reshape(3,4)
print(b)

# 2차원 배열에서 열만 뽑기
print(b[0])
print(b[1])

# 2차원 배열의 특정 위치의 값을 가져오기
print(b[0][2])
print(b[2][3])

# 특정 행 또는 열의 값 모두 바꾸기
b[0] = 111
print(b)

# 특정 위치의 값 초기화 하기. 2 가지 방법
b[2][1] = 888
b[1,2] = 999
print(b[2][1])
print(b)

# 특정 행,열 뽑기 (범위로)
b = np.arange(12).reshape(3,4)
print(b)
print(b[0:2])

print(b[0:2, 1 ])  # 범위는 n:m로 지정한다. 행과 열은 , 로 구분한다.

# 특정 행,열을 : 를 활용해서 범위 또는 전체로 가져오는 방법
print(b)
print("b[:,1]:", b[:,1])
print("b[:2,]:",b[:2,:])
