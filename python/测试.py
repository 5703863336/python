import numpy as np

a = np.array([1,2,3,4,5])
b = np.arange(5)

c = np.power(a-b,2)
print(np.sum(c))