import numpy as np

# a = np.array([1,2,3], dtype="int16")
# b = np.array([[1,2, 3], [2, 5, 7]])

# print(a.ndim, b.ndim)
# print(a.shape, b.shape)
# print(a.dtype)
# print(a.itemsize)
# print(a.nbytes)

a = np.array([
  [1,2,3,4,5,6,7],
  [8,9,10,11,12,13,14]
])

print(a)
print(a.shape)
print(a[1, 5]) #[r, c] output : 13
print(a[0, :]) # Gets the first row
print(a[:, 0]) # Gets the first columns

# Getting little more fancy [startindex:endindex:stepsize]
print(a[0, 1: 6:2])
a[1, 5] = 20 #changes the 2nd row 6th element
print(a)
a[:, 2] = 5 # Changes the 3 rd element of both the rows
print(a)



