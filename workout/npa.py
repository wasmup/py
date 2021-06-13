import numpy as np
# Creating a 1D array from a list
a = np.array([1, 2, 3])
print(a)  # [1 2 3]

# Creating a 2D array from a list of lists
b = np.array([[1, 2], [3, 4]])
print(b)
# [[1 2]
#  [3 4]]

# Creating a 3D array from a list of lists of lists
c = np.array([[[1, 2],
               [3, 4]],
              [[5, 6],
               [7, 8]]])
print(c)
# [[[1 2]
#  [3 4]]
#  [[5 6]
#  [7 8]]]
print(c.ndim)  # 3
print(c.shape)  # (2, 2, 2)
print(c.dtype)  # int64

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(np.max(a))
print(np.min(a))
print(np.average(a))

b = np.array([[1, 1, 1],
              [1, 1, 2],
              [1, 1, 2]])

print(a + b)
print(a - b)
print(a * b)
print(a / b)


a = np.array([130, 137]) * np.array([1.1, 1.1])
print(a)
