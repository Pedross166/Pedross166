l89 = [85, 89, 145, 42, 20, 4, 16, 37, 58, 2, 3, 9, 81, 65, 61]
l1 = [1, 10, 13, 32, 44]
observados = []
l0 = []
for i in range(1,10000000):
  l0.append(i)

for i in l89+l1:
  l0.remove(i)

r = '0'
n = 0
while True:
  if len(l0) == 0:
    break

  r = str(l0[0])
  observados.append(l0[0])
  while True:
    for j in r:
      n += int(j)**2
    if n in l89:
      for a in observados:
        l89.append(a)
        l0.remove(a)
      observados = []
      break
    elif n in l1:
      for a in observados:
        l1.append(a)
        l0.remove(a)
      observados = []
      break
    else:
      if n not in observados:
        observados.append(n)
      n, r = 0, str(n)


print(len(l89))
print(10000000-len(l1))