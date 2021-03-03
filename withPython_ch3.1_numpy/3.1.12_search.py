# 조건에 맞는 값 찾기
import numpy as np

a= np.arange(10,20)
print(a)

# 조건 (15이상)에 부합하는 것 찾기
# 결과는 인덱스로 나온다.
print(np.where(a>15))
# 조건에 부합하는 것을 맞으면 1, 틀리면 0으로 반환 (원래는 인덱스로 반환)
print( np.where(a>15,1,0))

# 조건에 부합하면 99를, 아니면 a배열 그대로
print( np.where(a>15, 99 ,a ))

# 2차원 배열에서 조건에 부합하는 위치를 반환.
# !! 결과값은 배열의 값이 아니라 배열의 위치다!!
b = np.arange(12).reshape(3,4)
print( "배열 b:",b)
coords = np.where(b>6)
print(coords)

# 위에서 나온 위치를 n,m 형태로 배열로 만들자
print(np.stack((coords[0], coords[1]), -1) )

a = np.arange(10,20)
print(np.nonzero(a>15))
print(np.where(a>15))

t = np.array( [True, True, True])
print(t)
# 모든 요소가 참인지 판별
print( np.all(t) )
    #하나라도 False가 있으면 False
t[1] = False
print(np.all(t))

tt = np.array( [[True, True],[False, True],[True, True]])
print(tt)
print(np.all(t))

# True,False 를 축 방향으로 판별
print(tt)
print(np.all(tt,0))
print(np.all(tt,1))

# 두 배열의 각 요소가 같은지 판별
a = np.arange(10)
b = np.arange(10)
print( a==b )

# 두 배열이 전체가 완전히 같은지 z.B) 이미지가 같은 이미지인지 판별
print( np.all(a==b) )

# 어느 부분이 같은지 혹은 틀린지 판별. 위치값으로 반환한다.
print( np.where( a==b ) )
a[2]=1
print( np.where( a!=b ) )

# 이전 프레임과 현재 프레임에 변화가 있는지, 
# 변화가 있는 픽셀의 위치가 어디인지
# 움직임을 감지하거나 객체를 추적하는 등 곳곳에 활용할 수 있다.