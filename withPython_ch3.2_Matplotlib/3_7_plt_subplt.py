# 그래프를 나누서 여러개의 창에 그릴 수 있다.
import matplotlib.pyplot as plt
import numpy as np

x= np.arange(10)
plt.subplot(2,2,1)
plt.plot(x, x**2)

plt.subplot(2,2,2) # 그래프가 표현될 위치 2,2,2
plt.plot(x,x*5)

plt.subplot(223) # 위치를 이런 방법으로도 표현 가능
plt.plot(x,np.sin(x))

plt.subplot(224)
plt.plot(x, np.cos(x))

plt.show()