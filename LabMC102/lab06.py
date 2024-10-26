###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 06 - Lista de Compras
# Nome: Pedro Souza Santos
# RA: 288644
###################################################

# Leitura de dados
D = float(input())
N = int(input())
n=N
pymarket = [float(item) for item in input().split()]
cpy = ''
bytebazar = [float(item) for item in input().split()]
cby = ''
devshop = [float(item) for item in input().split()]
cdev = ''
menor = 0
c=0
possível=True
# Processamento dos dados
for a in range(0, N):
  menor = min(pymarket[a], bytebazar[a], devshop[a])

  if D - menor >= 0:
    D-=menor
    if menor == pymarket[a]:
      cpy = cpy + f' {a+1}'
    elif menor == bytebazar[a]:
      cby = cby + f' {a+1}'
    elif menor== devshop[a]:
      cdev = cdev + f' {a+1}'
  else:
    possível = False


# Saída de dados

if cpy != '':
  print('Itens comprados no PyMarket:')
  print(cpy.strip())
else:
  print('Nenhum item foi comprado no PyMarket')

if cby != '':
  print('Itens comprados no ByteBazar:')
  print(cby.strip())
else:
  print('Nenhum item foi comprado no ByteBazar')

if cdev != '':
  print('Itens comprados no DevShop:')
  print(cdev.strip())
else:
  print('Nenhum item foi comprado no DevShop')

if possível:
  print('Foi possível terminar a receita')
else:
  print('Não foi possível terminar a receita')