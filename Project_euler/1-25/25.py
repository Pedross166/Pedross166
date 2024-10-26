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

#25
def fib(x):
  f1 = 1
  f2 = 1
  f3 = 0
  if x==1:
    return 1
  elif x==2:
    return 1
  else:
    for i in range(3, x+1):
      f3 = f1 + f2
      f1 = f2
      f2 = f3
    return f3
x=1
while len(str(fib(x))) != 1000:
  x +=1

print(x)