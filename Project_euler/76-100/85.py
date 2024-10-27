def counting(m,n):
    if n==1 :
        return m*(m+1)//2
    elif m==1:
        return n*(n+1)//2
    elif n>m:
        return counting(m,n-1) + (n)*counting(m,1)
    elif m>n:
        return counting(m-1,n) + (m)*counting(1,n)
    elif m==n:
        return counting(m-1,m-1) + (m**3)

minimo=0
gera = [0,0]
for i in range(2,200):
    for j in range(2,200):
        if minimo==0:
            minimo = abs(2000000-counting(i,j))
            gera=[i,j]
        else:
            if minimo > abs(2000000-counting(i,j)):
                minimo = abs(2000000-counting(i,j))
                gera=[i,j]
print(minimo, gera, gera[0]*gera[1], counting(gera[0],gera[1]))
print(counting(3,2))