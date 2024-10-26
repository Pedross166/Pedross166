def eratostenes(x):
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
  éprimo= True
  for i in range(2, len(lista)-1):
    if lista[i] and x%i==0:
      éprimo = False
    if éprimo == True:
      return {f'{x}': 1}
    else:
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

T=28
c=7

def conta_divisores(x):
  dic = decompoe_em_primo(x)
  s=1
  for i in dic.values():
    s*=i+1
  return s

while conta_divisores(T) <= 500:
  T += c+1
  c += 1

print(T)