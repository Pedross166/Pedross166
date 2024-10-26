def lista(x):
  r = str(x)
  saída = []
  for i in r:
    saída.append(i)
  return saída

n=10**6
procurados = []
t=1
while True:
  t+=1
  l = lista(t)
  s=0
  for i in l:
    s += int(i)**5
  if s==t:
    procurados.append(t)
  if t>=n:
    break


resultado = 0
for j in procurados:
  resultado += j

print(resultado, procurados)