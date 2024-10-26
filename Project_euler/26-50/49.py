def eratostenes(x):
  x=int(x)
  if x == 1:
    return [False]
  crivo =[False, False]
  for i in range(2, x+1):
    crivo.append(True)

  for i in range(2, x):
    if crivo[i]:
      for j in range(2, x//(i)+1):
        crivo[i*j] = False

  return crivo

def listaprim(x):
  erat =eratostenes(x)
  l=[]
  for i in range(2,len(erat)):
    if erat[i]:
      l.append(i)
  return l

l = listaprim(10000)
l2 = listaprim(1000)
for i in l2:
  l.remove(i)

dic={}

for i in l:
  a = str(i)
  x=''
  l2=[]
  for b in a:
    l2.append(b)
    for k in sorted(l2):
      x+=k
  if x not in dic.keys():
    dic[f'{x}'] = [a]
  else:
    dic[f'{x}'] += [a]

r=[]
x=''

for i in dic.keys():
  if len(dic[i])==3:
    for j in dic[i]:
      x+=j
    r.append(x)
    x=''


print(dic)