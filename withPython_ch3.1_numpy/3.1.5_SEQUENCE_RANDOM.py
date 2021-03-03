import numpy as np

# 순차적으로 정수로 채우기
a = np.arange(5)
print(a)
print(a.dtype)
print(a.shape)

# 순차적으로 실수로 채우기
b = np.arange(5.0)
print(b)
print(b.dtype)
print(b.shape)

# 시작, 종료, 증가값을 지정해서 배열 만들기
c = np.arange(3,9,2)
print(c)
print(c.dtype)

# 난수 하나 만들기
print(np.random.rand())

# 난수를 배열로 만들기 크기는 2x3
a = np.random.rand(2,3)
print(a)