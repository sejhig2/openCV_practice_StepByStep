import numpy as np

np.random.seed(16394)

# 균일 분포 난수
a= np.random.rand(2,3)

# 평균0, 표준편차1의 정규 분포 난수
b = np.random.randn(2,3)

# 균일 분포 난수 1차원 행렬(1x6)
c = np.random.rand(6)

# 1~100사이의 정수 난수 1차원 행렬(1x6)
d = np.random.randint(1,100,(6))

# 배열의 크기 바꾸기 2x3크기로 바꾸기
c= np.reshape(c,(2,3))

# 배열의 크기 바꾸기 2행으로 바꾸고 남은 원소에 맞춰서 열에 넣기
d = d.reshape(2,-1)
print(d)
d = d.reshape(3, -1)
print(d)