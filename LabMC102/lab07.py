###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Dependências de Tarefas I
# Nome: Pedro Souza Santos
# RA: 288644
###################################################

# Leitura de dados
lista_in = str(input()).split()
lista=[]
for i in lista_in:
  lista.append(int(i)-1)

nao_fechado = True
sem_problemas=[]
analisados = []
# Verificação das dependências entre as tarefas
for a in lista:
  if a == lista[a]:
    sem_problemas.append(a)

for a in range(0, len(lista)):
  j=lista[a]
  i=a
  while i != j:
    if j in sem_problemas:
      analisados = []
      break
    elif j in analisados:
      nao_fechado = False
      analisados = []
      break
    else:
      analisados.append(j)
      i, j = j, lista[j]


# Impressão da saída
if nao_fechado:
    print("Todas as tarefas podem ser realizadas")
else:
    print("Alguma das tarefas não pode ser realizada")