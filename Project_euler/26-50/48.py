n=0
for a in range(1,1001):
  n+=a**a

print(str(n)[::-1][9:0:-1])