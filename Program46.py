#mathematical operations in numpy
import numpy as np
arr1=np.array([30,40,50,60])
arr2=np.array([40,50,60,70])
print(arr1+arr2) # addition
print(np.add(arr1,arr2)) #addition

print(arr2-arr1) #subtract
print(np.subtract(arr2,arr1)) #subtract

print(arr1*arr2)#multiply
print(np.multiply(arr1,arr2))#multiply

print(arr1/arr2)# divide
print(np.divide(arr1,arr2))#divide

arr1=np.array([3,4,2,1])
arr2=np.array([2])
print(np.power(arr1,arr2)) #power

arr1=np.array([9,16,4,1])
print(np.sqrt(arr1)) #square root