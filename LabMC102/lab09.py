###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 09 - Álbum de Fotos
# Nome: Pedro Souza Santos
# RA: 288644
###################################################

N = int(input())
fotos = {}
pessoas = {}
tudo = []
maior = 0
pessoa = ''

# Leitura de dados

for i in range(N):
  conjunto = str(input())
  corte = conjunto.find(':')
  ID, nomes = conjunto[0:corte].split()[1], conjunto[corte+2:].split(', ')
  fotos[f'{ID}'] = nomes
  tudo += nomes

# Processamento de dados

for i in tudo:
  if i != '':
    if i not in pessoas:
      pessoas[i] = 1
    else:
      pessoas[i] +=1

tudo = ''

for i in pessoas.keys():
  if pessoas[i] > maior:
    maior = pessoas[i]
    pessoa = i
  elif pessoas[i] == maior:
    if i < pessoa:
      pessoa = i

for i in fotos.keys():
  if pessoa in fotos[i]:
    tudo += i + ' '

# Saída de dados

print(f'''No total, {len(pessoas.keys())} pessoas apareceram nas fotos.
{pessoa} foi a pessoa mais frequente, aparecendo na(s) foto(s): {tudo[:len(tudo)-1]}''')