n=str(input('Coloca o número aí: ')).replace(' ', '')
maior=0
p=1
for i in range(0,1000-12):
  for a in range(i, i+13):
      p *= int(n[a])
      if p > maior:
        maior=p
  p = 1

print(maior)