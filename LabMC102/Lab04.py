###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Chefe de Cozinha
# Nome: Pedro Souza Santos
# RA: 288644
###################################################
tempo=tempo_final=c=0
# Leitura da entrada
while tempo_final<= 23*60:
  horas, minutos, tempo_pedido = [int(x) for x in input().replace(":", " ").split()]

  tempo= horas*60 + minutos

  if tempo_final >= tempo:
    tempo = tempo_final + tempo_pedido
  else:
    tempo += tempo_pedido

  if tempo < 23*60:
    c+=1
  else:
    break

  tempo_final=tempo

# Saída de dados
print(c)