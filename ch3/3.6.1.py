import numpy as np
list1, list2 = [1,2,3], [4,5.0,6]
a,b = np.array(list1), np.array(list2)
print(a,b)
c = a + b
d = a - b
e = a*b
f = a / b
g = a * 2
h = b + 2
print( 'c = a + b ' , c)
print( "d= a - b:", d)
print("e=a*b:",e)
print("f=a/b:",f)
print("g = a*2:",g)
print("h=b+2:",h)
