# 평균, 최대 값, 최소 값 같은 통계값들을 알아보자.

import numpy as np
a = np.arange(12).reshape(3,4)
print(a)
# 전체 합
print(np.sum(a))
# 행 방향 합
print(np.sum(a,1))
# 열 방향 합
print(np.sum(a,0))

# 평균 구하기
# 전체 평균
print(np.mean(a))
# 행방향 평균
print(np.mean(a,1))
# 열 방향 평균
print(np.mean(a,0))

# 최소값 구하기
print(np.min(a))
print(np.amin(a))
print(np.min is np.amin)
print(np.min(a,1))
print(np.min(a,0))
