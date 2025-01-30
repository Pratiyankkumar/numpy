import numpy as np

b = np.array([
  [
    [1,2],[3,4]
  ],
  [
    [5,6],[7,8]
  ]
])

print(b.ndim)
print(b[0,1,1]) #both line 13 and 14 are same and gives same output
print(b[0][1][1])

print(b[0]) ## 1st row
print(b[1]) ## 2nd row
print(b[:, 0]) ## 1st columns
print(b[:, 1]) ## 2nd column

print("****************************")
b[:, 1] = [[5,6], [9,10]]
print(b)