# aggregation functions
import numpy as np
a=np.array([30,49,59,90]) 
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.size(a))
print(np.mean(a))
print(np.cumsum(a))
print(np.cumprod(a))

p=[100,30,490,456]
q=[40,23,45,56]
price=np.array(p)
quantity=np.array(q)

print(price,"\n",quantity)
print(np.sum(price))