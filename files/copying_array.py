import numpy as np

a = np.array([1,2,3])
b = a # like this if we change a b will also change (Wrong way)
b = a.copy() # This is correct ways
b[0] =100 

print(a)