import numpy as np

v1 = np.array([1,2,3,4,])
v2 = np.array([5,6,7,8])

# Vertical Stacking
stacked_v_array = np.vstack([v1, v2, v1, v1]) # number of columns should be equal
print(stacked_v_array)

# Horizontally Stacking
stacked_h_array = np.hstack([v1, v2]) #number of rows should be equal
print(stacked_h_array)