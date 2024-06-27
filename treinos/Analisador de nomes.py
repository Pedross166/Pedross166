nome=str(input("Digite seu nome:"))
M=nome.upper()
m=nome.lower()
s=nome.split()
NoS=nome.replace(" ",  '')
N=len(NoS)
n=len(s[0])
print("""Nome em maiusculas: {}
Nome em minusculas: {}
Número de letras no nome:{}
O primeiro nome é {} e tem {} letras. """.format(M, m, N, s[0], n))