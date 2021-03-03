import numpy as np

# 데이터 타입 바꾸기 (형 변환하기)
# int 32 -> float 32형으로 형 변환하기
a = np.arange(5)
print(a)
print(a.dtype)

b = a.astype('float32')
print(b)
print(b.dtype)

# int32 -> float64로 형변환
c = a.astype(np.float64)
print(c)

# 부호가 없는 정수형으로 형변환
d = np.uint8(a)
print(d)