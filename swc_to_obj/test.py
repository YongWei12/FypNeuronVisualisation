import numpy as np

#code to create a numpy array with vector as individual component
vector1 = np.array([1,2,3])
vector2 = np.array([3,2,3])
a = np.zeros(shape=(5,2))
a = a.astype(np.object)
a[0][0] = vector1
a[2][1] = vector2
print(a)