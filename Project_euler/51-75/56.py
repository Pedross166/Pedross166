n=0
s = 0
maior=0
for a in range(2,100):
  for b in range(1,100):
    n=str(a**b)
    for i in n:
      s += int(i)
    if s>maior:
      maior=s
    s=0

print(maior)