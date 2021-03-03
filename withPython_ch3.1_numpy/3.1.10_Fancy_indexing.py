import numpy as np

a = np.arange(10)
print(a)

# 배열a에서 5이상인 값을 가져온다.
b = a > 5
print(a[b])

#조건에 맞는 값 초기화 하기
a[a>5]=1
print(a)

b= np.arange(12).reshape(3,4)
print(b)
print(b[[0,2]])
# 특정 위치의 값 가져오기
# 0,2의 값과 2,3의 값 가져오기
print( b[[0,2],[2,3]])