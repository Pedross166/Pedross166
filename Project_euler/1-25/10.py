def isprime(x):
    if x ==1:
        return False
    for i in range(2, int((x+1)**0.5 + 1)):
        if x%i == 0:
            return False
    return True

s=0
for i in range(1,2000000):
  if isprime(i):
    s += i
print(s)