###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Tit for Tat
# Nome: Pedro Souza Santos
# RA: 288644
###################################################
eu=c0=adv=0

# Leitura da entrada

k=int(input())

# Processamento dos dados

for i in range(0, k):
  if i==0:
    print(0)
    c=int(input())
    c0=c
    if c==1:
      adv+=5
    elif c==0:
      adv+=3
      eu+=3
  else:
    print(c0)
    c=int(input())
    if c0==c==1:
      eu+=1
      adv+=1
    elif c0==c==0:
      eu+=3
      adv+=3
    elif c0==1 and c==0:
      eu+=5
    elif c0==0 and c==1:
      adv+=5
    c0=c

# Saída de dados
print(eu)
print(adv)