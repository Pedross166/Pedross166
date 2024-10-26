###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Escolhendo seu Cartão de Crédito
# Nome: Pedro Souza Santos
# RA: 288644
###################################################

# Leitura da entrada
anuidade = float(input())
beneficios = float(input())
cashback = float(input())/100
gasto = float(input())
# Cálculos e impressão da saída
dif = anuidade - (beneficios + gasto*cashback)*12
if dif>0:
  print(True)
else:
  print(False)