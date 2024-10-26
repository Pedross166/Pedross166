###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - O Caso do Medalhão Roubado
# Nome: Pedro Souza Santos
# RA: 288644
###################################################

# Leitura da entrada
N = int(input())

museu = []
for _ in range(N):
    museu.append(list(input()))

M = int(input())
suspeitos = {}
SUSPEITOS = {}
PISTAS = []
for _ in range(M):
    letra, pistas = input().split()
    PISTAS+=pistas
    suspeitos[letra] = pistas.split(",")
    SUSPEITOS[letra] = 0

# Verificação da posição do detetive e coleta de pistas

I = N
J = len(museu[0])
c = 0

def procurar(i,j):
  if i>0:
    if museu[i-1][j] == 'D':
      return True
  if j>0:
    if museu[i][j-1]=='D':
      return True
  if i<I-1:
    if museu[i+1][j]=='D':
      return True
  if j<J-1:
    if museu[i][j+1] == 'D':
      return True
  return False

while True:
  for i in range(I):
    for j in range(J):
      if museu[i][j]=='.':
        if procurar(i,j):
          c+=1
          museu[i][j]='D'
      if museu[i][j] in PISTAS:
        if procurar(i,j):
          for a in suspeitos.keys():
            if museu[i][j] in suspeitos[a]:
              SUSPEITOS[a] +=1
          museu[i][j]='D'
  if c==0:
    break
  else:
    c=0

# Verificação dos suspeitos e impressão da saída
maior = 0
for a in SUSPEITOS.values():
  if a>maior:
    maior=a

imprimir=''

for a in SUSPEITOS.keys():
  if SUSPEITOS[a] == maior:
    imprimir += a + ' '

print(imprimir[0:len(imprimir)-1])