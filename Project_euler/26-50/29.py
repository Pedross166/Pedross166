x=0
seq = []
for a in range(2, 101):
  for b in range(2, 101):
    x = a**b
    if x not in seq:
      seq.append(x)

print(len(seq))