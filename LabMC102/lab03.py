###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Geladeiras Subzero
# Nome:Pedro Souza Santos
# RA:288644
###################################################

# leitura de dados
t = input()
p = int(input())
w = int(input())

# Verificação e impressão do nome do modelo a ser recomendado
if p>=4 and w<=100:
  print('IceCold')
if t=='D' and p==1:
  print('Gel-D')
if w>130 and t=='S':
  print('Frost++')
if t=='D':
  if p==3:
    if w<=100:
      print('Gel-DPlus')
    else:
      print('DupCold')
  elif p>=4 and w>100:
    print('Frost++')
  elif p==2:
    if w <=150:
      print('Gel-DPlus')
    else:
      print('DupCold')
if t=="S":
  if p<=2:
    if w<=70:
      print('Gel-S')
    elif 70<w<=130:
      print('Gel-SPlus')
  if p==3 and w<=130:
    print('DeluxFF')
  if p>3 and 100<w<=130:
    print('DeluxFF')