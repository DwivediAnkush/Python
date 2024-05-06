#concatinate and aplitting arrays
import numpy as np
arr1=np.array([30,40,50])
arr2=np.array([5,5,4])
print(np.concatenate([arr1,arr2]))
print(np.concatenate([arr1,arr2],axis=0))
print(np.hstack([arr1,arr2]))# horizontal concatenation
print(np.vstack([arr1,arr2]))# vertical concatenate

#splitting
a=np.array([20,40,30,10,20])
b=np.array_split(a,4)
print(b)