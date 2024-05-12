import numpy as np 
import time
import sys


l = range(1000)
print(sys.getsizeof(5)*len(l))


array = np.arange(1000)
print(array.size*array.itemsize)

#nump usese less space in the memory than lists
#and is also faster than lists 