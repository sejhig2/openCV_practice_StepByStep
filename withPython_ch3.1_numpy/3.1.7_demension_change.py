#차원 변경
import numpy as np

# 1차원 -> 2차원
a = np.arange(6)
print(a)
# 방법1
b= a.reshape(2,3)
print(b)
# 방법2
c = np.reshape(a, (2,3))

# 1행짜리를 2행으로 변경
# -1의 의미 : 행 또는 열의 크기를 지정하고 나머지는 알아서 맞춰라
d = np.arange(100).reshape(2,-1)
print(d)
print(d.shape)
# 1행 짜리를 2열로 변경
d = np.arange(100).reshape(-1,2)
print(d)
print(d.shape)

# 크기가 안 맞다면? 101개를 2로 나눠서 만들어보자
# f = np.arange(101)
# f = f.reshape(-1,2)
# print(f) # 에러 발생

# 행과 열을 바꾸는 전치
g = np.arange(10).reshape(-1,2)
print(g)
print(g.T)