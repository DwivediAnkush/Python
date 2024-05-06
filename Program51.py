#statistical functions
import numpy as np
import statistics as stats 
baked_food=[200,300,400,234,322]
a=np.array(baked_food)
print(np.mean(baked_food)) # sum of all the values/ numbers of values
print(np.median(baked_food)) #central value after sorting
print(stats.mode(baked_food))
print(np.std(baked_food))
print(np.var(baked_food))