def fat(x):
  x=int(x)
  s=1
  for i in range(1,x):
    s*=i+1
  return s

def arranjo(x,y):
  c=int(x)
  s=1
  while True:
    s*=c
    c-=1
    if c == x-y:
      break
  return(s)

def Cab(x,y):
  x=int(x)
  y=int(y)
  if x==y or y==0:
    return 1
  elif y==1 or y==x-1:
    return x
  else:
    return (x/y)*Cab(x-1, y-1)

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

def listaprim(x):
  erat =eratostenes(x)
  l=[]
  for i in range(2,len(erat)):
    if erat[i]:
      l.append(i)
  return l

def isprime(x):
  l = eratostenes(int(x)**0.5 + 1)
  for i in range(2, len(l)):
    if l[i] and x%i == 0:
      return False
  return True


def decompoe_em_primo(x):
  t=x
  lista = eratostenes(int((x**0.5)+10))
  dic_primos={}
  primo = 2
  count = 2
  while t != 1:
    if t%primo==0:
      if f'{primo}' in dic_primos.keys():
        dic_primos[f'{primo}']+=1
        t = t//primo
      else:
        dic_primos[f'{primo}']=1
        t = t//primo
    else:
      while True:
        count += 1
        if count == len(lista):
          break
        if lista[count]:
          primo = count
          break
      if primo > t**0.5:
        if f'{t}' in dic_primos.keys():
          dic_primos[f'{t}']+=1
          break
        else:
          dic_primos[f'{t}']=1
          break
      if count == len(lista):
        break
  return dic_primos

def phi(x):
  phi = x
  dic = decompoe_em_primo(x)
  for i in dic.keys():
    x *= 1-1/int(i)
  return(x)


def conta_divisores(x):
  dic = decompoe_em_primo(x)
  s=1
  for i in dic.values():
    s*=i+1
  return s

def mdc(x, y):
  z=min(x,y)
  w=max(x,y)
  if w%z == 0:
    return z
  else:
    return mdc(z, w%z)


def mmc(x, y):
  return x*y/mdc(x,y)