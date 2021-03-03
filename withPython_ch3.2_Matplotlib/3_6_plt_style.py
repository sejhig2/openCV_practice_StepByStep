# 그래프의 점을 원하는 모양으로 바꿀 수 있다.
# 그래프의 점을 원하는 색상으로 바꿀 수 있다.
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
f1 = x * 5
f2 = x**2
f3 = x**2+x*2

plt.plot(x,'r--')
plt.plot(f1,'g.')
plt.plot(f2,'bv')
plt.plot(f3,'ks')
plt.show()