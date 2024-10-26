import math
def mdc(x, y):
  z=min(x,y)
  w=max(x,y)
  if w%z == 0:
    return z
  else:
    return mdc(z, w%z)

def mmc(x, y):
  return x*y/mdc(x,y)

t=1
for i in range(1,20):
  t=mmc(i, t)

print(t)