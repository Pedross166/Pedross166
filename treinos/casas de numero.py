N=str(input("Digite um número com até quatro algrismos:"))
n=N.rjust(4,"0")
print("""Número:{}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(N, n[3], n[2], n[1], n[0]))
