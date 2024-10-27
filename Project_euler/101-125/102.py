import numpy as np
with open('Project_euler/funções e arquivos/0102_triangles.txt', 'r') as f:
  tri = f.read()

nn = tri.split("""
""")
c=0

for a in nn[0:len(nn)-1]:
  a=a.split(',')
  for b in range(len(a)):
    a[b]=int(a[b])
  x=a[0:2]
  y=a[2:4]
  z=a[4:6]

  if min(x[0],y[0],z[0])*max(x[0],y[0],z[0])>0 or min(x[1],y[1],z[1])*max(x[1],y[1],z[1])>0:
    continue
  else:
    Area = abs(np.linalg.det([[x[0], x[1]], [y[0], y[1]]])) + abs(np.linalg.det([[x[0], x[1]], [z[0], z[1]]])) + abs(np.linalg.det([[z[0], z[1]], [y[0], y[1]]]))
    area_  =  abs(np.linalg.det([[z[0]-x[0], z[1]-x[1]],[y[0]-x[0], y[1]-x[1]]]))
    if Area - 0.00000001 < area_ < Area + 0.00000001:
      c+=1

print(c)