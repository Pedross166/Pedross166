x=10**8 + 1
while True:
  x+=1
  l = str(x**2)
  if l[0]!='1':
    continue
  if l[2]!='2':
    continue
  if l[4]!='3':
    continue
  if l[6]!='4':
    continue
  if l[8]!='5':
    continue
  if l[10]!='6':
    continue
  if l[12]!='7':
    continue
  if l[14]!='8':
    continue
  if len(l)==17 and l[16]=='9':
    print(x, x**2)
    break

