###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Kungsleden
# Nome: Pedro Souza Santos
# RA: 288644
###################################################

import numpy as np

entrada = input().split()
linha, coluna = int(entrada[0]), int(entrada[1])
cabana = [0,0]
floresta = [0,0]
finais = ['encontrou o fim da floresta.', 'de volta a cabana.', 'andou em circulos.', 'caminho sem saida.']

# Leitura de dados

mapa = np.array([ input().split() for i in range(linha) ])

# Processamento de dados

for i in range(linha):
  for j in range(coluna):
    if mapa[i, j] == 'C':
      cabana = [i, j]

for i in range(linha):
  for j in range(coluna):
    if mapa[i, j] == 'F':
      floresta = [i, j]


def busca(mapa, chave, pos_c):
  observados = []
  saída = 0
  if chave == 'N':
    p = [pos_c[0]-1, pos_c[1]]
  elif chave == 'S':
    p = [pos_c[0]+1, pos_c[1]]
  elif chave == 'L':
    p = [pos_c[0], pos_c[1]+1]
  elif chave == 'O':
    p =[pos_c[0], pos_c[1] - 1]
  a=p[0]
  b=p[1]
  while True:
    estou = mapa[a, b]
    #cabana
    if estou == 'C':
      saída = 1
      break
    #circulos
    elif [a, b] in observados:
      saída = 2
      break
    #floresta
    elif estou == 'F':
      saída = 0
      break
    observados.append([a, b])
    if estou == 'N':
      if a == 0:
        saída = 3
        break
      else:
        a-=1
    elif estou == 'S':
      if a == linha-1:
        saída = 3
        break
      else:
        a += 1
    elif estou == 'L':
      if b == coluna-1:
        saída = 3
        break
      else:
        b += 1
    elif estou == 'O':
      if b == 0:
        saída = 3
        break
      else:
        b -= 1

  return saída

# Saída de dados

print(f'N: {finais[busca(mapa, "N", cabana)]}')
print(f'S: {finais[busca(mapa, "S", cabana)]}')
print(f'L: {finais[busca(mapa, "L", cabana)]}')
print(f'O: {finais[busca(mapa, "O", cabana)]}')
