c=1000000
e=c
termos=1
maximo=0
geramax=0
for c in range(1000000, 1, -1):
  e=c
  termos = 1
  while e != 1:
    if e%2==0:
      e=int(e/2)
      termos += 1
    else:
      e=3*e +1
      termos += 1
  if termos>maximo:
    maximo=termos
    geramax=c

print(geramax)