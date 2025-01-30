import numpy as np

a = np.ones((2,3))
# print(a)

b = np.full((3,2), 2)
# print(b)

print(np.matmul(a, b)) # To multiply two mtrices algebrically

# Finding determinants of a identiity matrix (You can find out of any square matrix z)
identity_matrix = np.identity(3)
determinant = np.linalg.det(identity_matrix)
print(determinant)