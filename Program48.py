# addition and deletion of elemnets
import numpy as np
a=np.array([20,40,60,80])
print(np.append(a,[90,100]))

print(np.insert(a,1,50)) # array,index,value

print(np.delete(a,1))