import numpy as np

before = np.array([
  [1,2,3,4], 
  [5,6,7,8]
])

print(before)

after = before.reshape((2,2,2)) ## resize is possible if the args multiply ups to the total no of elements in the matrices 
print(after)
