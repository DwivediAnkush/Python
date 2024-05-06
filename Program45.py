#numpy in python
# numpy stands for numerical python. It uses in scientific calculations using arrays. It also has functions for working in domain of linear algebra, fourier transformation and matrices.

#creation
import numpy as np 
arr=np.array([10,20,30,40])
print(arr)
print(type(arr))

#slicing
print(arr[0:3])
print(arr[:])
a=np.array(([10,20,30,40],[20,30,40,50]))
print(a)
print(a[0:2,0:3])

#other functions
print(np.shape(a))
print(np.size(a))
print(np.ndim(a))
print(a.dtype)
'''
a.shape= array dimensions
len(a)= length of an array
b.ndim= number of array dimensions
e.size= number of array elements
b.dtype= data type of an array elements
b.astype(int)= convert on array to a different type
'''