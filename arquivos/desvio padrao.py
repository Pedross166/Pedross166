import numpy as np
import matplotlib.pyplot as plt

a=np.array([[1, 1.2, 3]])
b=np.array([2, 5, 6])

d=np.array([3, 4, 5])
c=np.array([7,7,7])

plt.scatter(a,b, marker="o")
plt.scatter(d,c, marker="xb-")
plt.show()