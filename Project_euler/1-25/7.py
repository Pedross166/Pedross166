n = int(input('Qual primo você quer ver: '))

def isprime(x):
    if x ==1:
        return False
    for i in range(2, int((x+1)**0.5 + 1)):
        if x%i == 0:
            return False
    return True

contprim = 0
c=0
while contprim != n:
    c+=1
    if isprime(c):
        contprim += 1
        primo = c

print(c)