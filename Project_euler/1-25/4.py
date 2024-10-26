def ispal(x):
  if x==x[::-1]:
    return True
  else:
    return False
maior = 0
for a in range(999, 99, -1):
  for b in range(999, 99, -1):
    if ispal(str(a*b)):
      if a*b > maior:
        maior = a*b
print(maior)