import numpy as np

# Boolean masking and Advanced Indexing

data = np.genfromtxt('1a.txt', delimiter=",", dtype="int32")
print(data > 50) # You can perform boolean
print(data[data > 50])
print(np.any(data > 50, axis=0))
print(np.all(data > 50, axis=0))
print(((data > 50) & (data < 100)))
print(~((data > 50) & (data < 100))) #not

