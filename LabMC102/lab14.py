###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Dependências de Tarefas II
# Nome: Pedro Souza Santos
# RA: 288644
###################################################

"""
Função para detectar ciclos nas dependências das tarefas,
que deve ser implementada de forma recursiva.

Argumentos:
    - dependências: matriz com as dependências de cada tarefa
    - tarefa: tarefa sendo analisada
    - visitadas: lista de tarefas que já foram analisadas
Retorno:
    Essa função deve retornar True se não houver ciclos nas
    dependências da tarefa e False caso contrário.

IMPORTANTE: A submissão de um programa sem uma FUNÇÃO RECURSIVA válida
            implementada será considerada TENTATIVA DE FRAUDE.
"""
def verifica_tarefas(dependencias, tarefa, visitadas):
    for i in dependencias[tarefa-1]:
        if i==0:
            return True
        elif i in visitadas:
            return False
        elif verifica_tarefas(dependencias, i, visitadas + [tarefa])==False:
            return False
    return True

# Leitura de dados

tarefas_possiveis=True
dependencias=[]

N=int(input())
for i in range(N):
    dependencias.append([int(j) for j in input().split()])

# Verificação das dependências entre as tarefas
for i in range(N):
    if verifica_tarefas(dependencias, i+1, []) == False:
        tarefas_possiveis=False
# Impressão da saída
if tarefas_possiveis:
    print("Todas as tarefas podem ser realizadas")
else:
    print("Alguma tarefa não pode ser realizada")