n=str(input('Coloca os 100 numeros aqui: ')).split()
s=0
for i in n:
  s+=int(i)
print(str(s)[0:10])