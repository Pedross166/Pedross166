def eratostenes(x):
  x=int(x)
  if x == 1:
    return [False]
  crivo =[False, False]
  for i in range(2, x+1):
    crivo.append(True)
  for i in range(2, x):
    if crivo[i]:
      for j in range(2, x//(i)+1):
        crivo[i*j] = False
  return crivo

erat = eratostenes(10000000)

def lista_primo(x):
  l=eratostenes(x)
  l1=[]
  for i in range(len(l)):
    if l[i]:
      l1.append(i)
  return l1

def isprime(x):
  a = int((int(x)**0.5 + 1))
  for i in range(2, a):
    if erat[i] and x%i == 0:
      return False
  return True

def concatenate(x, y):
  st1 = str(x)+str(y)
  n1= int(st1)
  st2 = str(y)+str(x)
  n2= int(st2)
  return isprime(n1) and isprime(n2)

l = lista_primo(10000)
l2=[]
l3=[]
l4=[]
l5=[]

for i in l:
  for j in l:
    c=j
    if concatenate(i, j) and j<i:
      a=[i,j]
      a.sort()
      if a not in l2:
        l2.append(a)
  if c<i:
    continue
  for j in l2:
    if concatenate(i,j[0]) and concatenate(i, j[1]):
      a=j+[i]
      a.sort()
      if a not in l3:
        l3.append(a)
  for j in l3:
    if concatenate(i,j[0]) and concatenate(i,j[1]) and concatenate(i, j[2]):
      a=[i]+j
      a.sort()
      if a not in l4:
        l4.append(a)
  for j in l4:
    if concatenate(i,j[0]) and concatenate(i,j[1]) and concatenate(i, j[2]) and concatenate(i, j[3]):
      a=[i]+j
      a.sort()
      l5.append(a)
      print(l5)
      s=0
      for b in a:
        s+=b
      print(s)
      break
  if len(l5)>0:
    break

print(l5)



