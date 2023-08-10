import numpy as np
# import matplotlib.pyplot as plt
# 1 dim
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# for i in a:``
#     print(i)

# for i in a:
#     if (i % 2 == 0):
#         print(f"This is an even number ", i)

# print(type(a))
# print(a.dtype)
# print(a.size)
# print(a.ndim)
# print(a.shape)
# print(a.mean())
# print(a.std())
# print(a.max())
# print(a.min())
# b = np.linspace(2,10,num=20)
# print(b)

# 2d

# b= [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
# A = np.array(b)
# # print(A)

# print(A[0][0:2])
# print(A[0:2, 2])
c = np.array([[1,0],[0,1]])
d = np.array([[2,1],[1,2]])
print(np.dot(c,d))