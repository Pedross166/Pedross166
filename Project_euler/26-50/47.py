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

def decompoe_em_primo(x):
  t=x
  lista = eratostenes(int((x**0.5)+2))
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
      if count == len(lista):
        break
      if primo > t**0.5+1:
        if f'{t}' in dic_primos.keys():
          dic_primos[f'{t}']+=1
          break
        else:
          dic_primos[f'{t}']=1
          break
  return dic_primos

n=4
while True:
  l1 = decompoe_em_primo(n)
  if len(l1.keys())!=4:
    n+=1
    continue
  l2 = decompoe_em_primo(n+1)
  if len(l2.keys())!=4:
    n+=1
    continue
  l3 = decompoe_em_primo(n+2)
  if len(l3.keys())!=4:
    n+=1
    continue
  l4 = decompoe_em_primo(n+3)
  if len(l4.keys())!=4:
    n+=1
    continue
  break
print(n)