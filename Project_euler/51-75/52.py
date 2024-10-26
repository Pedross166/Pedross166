t=1
def lista(x):
  r = str(x)
  saída = []
  for i in r:
    saída.append(i)
  return saída


while True:
  l1 = lista(t)
  l1.sort()
  l2 = lista(2*t)
  l2.sort()
  if l1!=l2:
    t+=1
    continue
  l3 = lista(3*t)
  l3.sort()
  if l1!=l3:
    t+=1
    continue
  l4 = lista(4*t)
  l4.sort()
  if l1!=l4:
    t+=1
    continue
  l5 = lista(5*t)
  l5.sort()
  if l1!=l5:
    t+=1
    continue
  l6 = lista(6*t)
  l6.sort()
  if l1==l6:
    break
  else:
    t+=1

resultado = []
for i in range(1,7):
  resultado.append(i*t)
print(resultado)