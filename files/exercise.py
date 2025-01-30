import numpy as np

#Matrix 1
arr1 = np.ones((5,5))
zero_three = np.zeros((3,3))
arr1[1:4, 1:4] = zero_three
# print(arr1)

## Matrix 2
arr2 = np.zeros((5,5))
np.fill_diagonal(arr2, 9)
# print(arr2)

#Matrix 3
arr3 = np.ones((5,5))
zero_mat = np.zeros((2,2))
arr3[0:2, 0:2] = zero_mat
arr3[0:2, 3:5] = zero_mat
arr3[3:5, 0:2] = zero_mat
arr3[3:5, 3:5] = zero_mat
# print(arr3)

# Matrix 4
arr4 = np.full((5,5), 2)
five_mat = np.full((3,3), 5)
arr4[1:4, 1:4] = five_mat
# print(arr4)

arr4 = np.zeros((6,5))
arr4[2:4, 0:2] = [[11,12], [16,17]]
arr4[[0,1,2,3], [1,2,3,4]] = [2,8,14,20]
arr4[[0,4,5], 3:] = [[4,5], [24,25], [29, 30]]
print(arr4)

