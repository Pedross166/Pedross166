import numpy as np
y=np.array([1,10,100,15])
x=y.std(ddof=0)
print(x)