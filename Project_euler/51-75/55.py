import funções as fp
def reverse(x):
    y = str(x)
    r = y[::-1]
    return int(r)

c=0
a=0

def isLycherel(x):
    t=x
    for i in range(50):
        if fp.ispal(t+reverse(t)):
            return False
        else:
            t= t+reverse(t)
        if i==49:
            return True
            
for i in range(1,10000):
    if isLycherel(i):
        c+=1

print(c)