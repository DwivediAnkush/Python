#sort
import numpy as np
ar=np.array(([7,8,3,4,67,44],[3,5,4,7,66,78]))
print(np.sort(ar))
print(np.where(ar%2==0))

#search
s=np.array([5,76,56,45])
a=np.searchsorted(s,45)
print(a)

p=np.array([20,30,40,50])
fa=[True,False,True,False]
new=p[fa]
print(new)