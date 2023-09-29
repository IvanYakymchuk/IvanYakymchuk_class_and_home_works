import numpy as np
import matplotlib.pyplot as plt
import random

ar = np.arange(10, 50)
print (ar)

print (ar[::-1])

matrix = np.arange(9).reshape(3, 3)
print(matrix)

ar1 = np.array([1, 2, 0, 0, 4, 0])
ar1_non_zero = np.nonzero(ar1)
print(ar1_non_zero[0])

ar_ones = np.eye(3, dtype=int)
print(ar_ones)

matrix_3x3x3 = np.random.rand(3,3,3)
print(matrix_3x3x3)

matrix_10x10 = np.random.rand(10,10)
print (np.min(matrix_10x10))
print (np.max(matrix_10x10))

X = np.random.random_sample((1, 30))
print(np.mean(X))


ar3 = np.zeros((5, 5),dtype=int)
ar3[0, :] = 1
ar3[-1, :] = 1
ar3[:, 0] = 1
ar3[:, -1] = 1
print (ar3)

a = 3
b = 3
ar4 = np.random.rand(a,b)
ar4_new = np.pad(ar4, ((1, 1), (1, 1)), mode='constant', constant_values=0)
print(ar4_new)

index_6x7x8 = np.unravel_index(100, (6,7,8))
print(index_6x7x8)
