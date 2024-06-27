from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

UprlD=float(0.1)
Urdg=float()

d1=np.array([])
x1=d1.mean()
u1=d1.std()/np.sqrt(6)

d2=np.array([])
x2=d1.mean()
u2=d1.std()/np.sqrt(6)

d3=np.array([])
x3=d1.mean()
u3=d1.std()/np.sqrt(6)

d4=np.array([])
x4=d1.mean()
u4=d1.std()/np.sqrt(6)

d5=np.array([])
x5=d1.mean()
u5=d1.std()/np.sqrt(6)

d6=np.array([])
x6=d1.mean()
u6=d1.std()/np.sqrt(6)

d7=np.array([])
x7=d1.mean()
u7=d1.std()/np.sqrt(6)

d8=np.array([])
x8=d1.mean()
u8=d1.std()/np.sqrt(6)

d9=np.array([])
x9=d1.mean()
u9=d1.std()/np.sqrt(6)

d10=np.array([])
x10=d1.mean()
u10=d1.std()/np.sqrt(6)

Ud1=np.sqrt(u1**2+Urdg**2+UprlD**2)
Ud2=np.sqrt(u2**2+Urdg**2+UprlD**2)
Ud3=np.sqrt(u3**2+Urdg**2+UprlD**2)
Ud4=np.sqrt(u4**2+Urdg**2+UprlD**2)
Ud5=np.sqrt(u5**2+Urdg**2+UprlD**2)
Ud6=np.sqrt(u6**2+Urdg**2+UprlD**2)
Ud7=np.sqrt(u7**2+Urdg**2+UprlD**2)
Ud8=np.sqrt(u8**2+Urdg**2+UprlD**2)
Ud9=np.sqrt(u9**2+Urdg**2+UprlD**2)
Ud10=np.sqrt(u10**2+Urdg**2+UprlD**2)

D=np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10])
h=np.array([])

m=float()
um=float()
g=float(9.8)

E=m*g*h