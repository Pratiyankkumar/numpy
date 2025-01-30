import numpy as np

# All 0's Matrix
print(np.zeros(5))
print("*************************")
print(np.zeros((2,3)))
print("*************************")
print(np.zeros((2,3,2))) # And so on

print("--------------------All 1 Matrix--------------")

print(np.ones((4,2,2), dtype="int32"))

print("--------------------Any other number--------------")

print(np.full((2,2), 99))

array1 = np.full((2,2), 99)
print(np.full_like(array1, 4))

print("------------------Random decimal numbers------------")
print(np.random.rand(4,2))
print(np.random.random_sample(array1.shape))

print("------------------Random Integer numbers------------")
print(np.random.randint(1,9, size=(3,3)))

print("------------------Identity matrxi------------")
print(np.identity(4))

print("-------------------------Repeat Array----------------------")
arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis=1) # x axis
r2 = np.repeat(arr, 3, axis=0) #y axis
print(r1)
print(r2)

print("-----------------------Exercise-------------------------")
ex_arr = np.ones((5,5))
zero_matrix = np.zeros((3,3))
zero_matrix[1, 1] = 9
ex_arr[1:4, 1:4] = zero_matrix
print(ex_arr)
