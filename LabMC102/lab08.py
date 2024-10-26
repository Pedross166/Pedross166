###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 08 - Processamento de Dados
# Nome: Pedro Souza Santos
# RA: 288644
###################################################
N = int(input())

def padrão_data(x):
  if len(x) == 8:
    x = x[:2]+ '-' + x[2:4] + '-' + x[4:]
  else:
    x = x[:2]+ '-' + x[3:5] + '-' + x[6:]
  return x

def padrão_telefone(x):
  if len(x) == 11:
    x = '('+ x[:2] + ')' + x[2:7] + '-' + x[7:]
  elif len(x) == 12:
    x =  '('+ x[:2] + ')' + x[2:]
  elif len(x) == 13:
    x = x[:9] + '-' + x[9:]
  return x

def padrão_nome(x) :
  nomes = str(x).split()
  proibidos = ['da', 'do', 'das', 'dos', 'de', 'e']
  nomes_ = []
  for i in nomes:
    if i.lower() not in proibidos:
     nomes_.append(i[0].upper() + i[1:].lower())
    else:
      nomes_.append(i.lower())
  return ' '.join(nomes_)

def padrão_endereço(x):
  if ',' in x:
    nome, número = x.split(', ')
  else:
    nome, número = x.split(' - ')
  nome = padrão_nome(nome)
  return nome + ', ' + número

# Saída de dados
for i in range(N):
  print(padrão_nome(str(input())))
  print(padrão_data(str(input())))
  print(padrão_endereço(str(input())))
  print(padrão_telefone(str(input())))