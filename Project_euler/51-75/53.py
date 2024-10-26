def Cab(x,y):
  x=int(x)
  y=int(y)
  if x==y or y==0:
    return 1
  elif y==1 or y==x-1:
    return x
  else:
    return (x/y)*Cab(x-1, y-1)

c=0

for n in range(1, 101):
  for r in range(n+1):
    if Cab(n, r)>1000000:
      c+=1

print(c)