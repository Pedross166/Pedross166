n = int(input('Digite um numero para saber o seus fatores primos: '))

def isprime(x):
    if x ==1:
        return False
    for i in range(2, int((x+1)**0.5 + 1)):
        if x%i == 0:
            return False
    return True


for i in range(1,n+1):
    if isprime(i) and n%i==0:
        print(i)