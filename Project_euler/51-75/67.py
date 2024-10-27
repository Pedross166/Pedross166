with open('Project_euler/funções e arquivos/0067_triangle.txt', 'r') as f:
  tri = f.read()
l = tri.split('''
''')
print(l)
for i in range(len(l)):
  l[i] = l[i].split()
  for j in range(len(l[i])):
    l[i][j] = int(l[i][j])
print(l)

for i in range(len(l)-2, 0, -1):
  for j in range(len(l[i-1])):
    l[i-1][j] = l[i-1][j] + max(l[i][j], l[i][j+1])

print(l[0])
