import numpy as np

# 배열의 값을 모두 +1 하기
mylist = list(range(10))
print(mylist)

for i in range(len(mylist)):
    mylist[i] = mylist[i] + 1
print(mylist)

# 위의 과정을 numpy를 사용해서 쉽게 하는 방법
a = np.arange(10)
print(a)
print(a+1)

b = np.arange(5)
print(b + 2)
print(b -1)
print(b *3)
print(b/2)
print(b**2)

b = np.arange(6).reshape(2,-1)
print(b)
print(b*2)

# 배열 끼리의 연산 ( 크기가 같아야 한다)
a = np.arange(10,60,10)
print(a)
b = np.arange(1,6,1)
print(b)
print("a+b:" , a+b)

# 크기가 달라도 행의 개수가 같다면 연산 가능
a = np.ones((2,3))
print(a)
d = np.arange(2).reshape(2,1)
print(d)
print(a+d)
# 크기가 달라도 열의 개수가 같다면 연산 가능

