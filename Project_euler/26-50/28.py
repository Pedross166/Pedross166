c=1
n=1
for i in range(1,501):
    for j in range(4):
        s=2*i
        n+=s
        c+=n

print(c, n, s, 1001**2)