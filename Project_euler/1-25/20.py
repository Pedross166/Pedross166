def fat(x):
  f=1
  for p  in range(1, x+1):
    f *= p
  return f

r=0
n = str(fat(100))
for a in n:
  r += int(a)

print(r)