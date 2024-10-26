l = range(1,10**6 +1)
s = ''
p = 1
for i in l:
  s+=str(i)

for n in range(7):
  p*= int(s[10**n - 1])

print(p)