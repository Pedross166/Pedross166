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

c=1
sum = 0
while fib(c) <= 4000000:
  if fib(c)%2 == 0:
    sum += fib(c)
  c += 1

print(sum)