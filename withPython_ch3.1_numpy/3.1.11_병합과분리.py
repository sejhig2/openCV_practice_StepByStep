# 병합하는 방법과 분리하는 방법을 배운다.
import numpy as np
# 병합
a= np.arange(4).reshape(2,2)
print(a)

b= np.arange(10,14).reshape(2,2)
print(b)

# 수직으로 병합
print("vstack a+b:\n",np.vstack((a,b)))

# 수평으로 병합
print("hstack a+b:\n",np.hstack((a,b)))

# 지정한 축 기준으로 병합 concatenate()
print(np.concatenate((a,b),1)) # 수평으로
print(np.concatenate((a,b),0)) # 수직으로

a= np.arange(12).reshape(4,3)
b = np.arange(10,130,10).reshape(4,3)
print(a)
print(b)
#stack 으로 쌓는 방법 2가지 - 2가지 축방향으로 쌓기
c = np.stack((a,b),0)
print(c)
print(c.shape)

d = np.stack((a,b),1)
print("a:",a)
print("b:",b)
print(d)
print(d.shape)


# 같은 위치의 값을 모았다.(1,1)에 위치한 값들 끼리, 1,2에 위치한 값들 끼리.
# 2d->3d
e = np.stack((a,b),2)
print(e)
print(e.shape)

# 위의 결과 값과 같은 효과 -1
e = np.stack((a,b),-1)
print(e)
print(e.shape)

# 분리
# 배열을 3등분 하기
a = np.arange(12)
print(a)
print(np.split(a,3))

# 1차원 배열을 2번째,7번째에서 나누고 나머지는 다 몰아서 하나로.
print(np.split(a,[2,7]))
a,b,c = np.split(a,[2,7])
print(a,b,c)

# 3등분
a = np.arange(12)
print( np.split(a,3,0) )

# 2등분
print("수평 방향으로 2등분")
b = np.arange(12).reshape(4,3)
print(b)
print( np.split(b,2,0))

# 특정 열만 따로 slicing
print( np.split(b, [1],1))