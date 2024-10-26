###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - No Man's Sky
# Nome: Pedro Souza Santos
# RA: 288644
###################################################

PROTOTIPOS = ('PD', 'PA', 'PTR', 'PTE', 'PC', 'PR', 'PO', 'PV')
PAISAGENS = ('SOA', 'SVM', 'SCO', 'SF1', 'SF2', 'SF3', 'SL', 'SPC')
CONDICOES_CLIMATICAS = ('CC0', 'CC1', 'CC2', 'CN1', 'CN2', 'CN3', 'CN4', 'CV', 'CTA1', 'CTA2', 'CTE1')

TERRENO_PROTO = {
  'PD':  ('TD', 'TA2'),
  'PA':  ('TA1 TA2', 'TD TP TM'),
  'PTR': ('TP TM', 'TAR TO1 TO2'),
  'PTE': ('TP TM', 'TAR TO1 TO2 TC'),
  'PC':  ('TC TM', 'TO1 TO2 TP'),
  'PR':  ('TC TM', 'TO1 TO2'),
  'PO':  ('TO1 TO2', 'TAR TM'),
  'PV':  ('TM', 'TP TC')
}

TERRENO_ADJACENCIA = {
  'TAR': 'TAR TO1 TP TC TM',
  'TO1': 'TAR TO1 TO2 TM',
  'TO2': 'TO1 TO2',
  'TA1': 'TA1 TA2 TP TC TM',
  'TA2': 'TA1 TA2 TD TC TM',
  'TD': 'TA2 TD',
  'TP': 'TAR TA1 TA2 TP TC TM',
  'TC': 'TAR TA1 TA2 TP TC TM',
  'TM': 'TAR TO1 TA1 TA2 TP TC TM'
}

ELEMENTOS = {
  # Scenarios
  'SOA' : ('PA',               'TA1 TA2'),
  'SVM' : ('PTR PTE PR PO',    'TO1 TO2'),
  'SCO' : ('PTR PTE PR PO',    'TO1'),
  'SF1' : ('PTR PTE',          'TP TM'),
  'SF2' : ('PTR PTE',          'TP TM'),
  'SF3' : ('PA PTR PTE',       'TP TM'),
  'SL'  : ('PTR PTE',          'TP TM TC'),
  'SPC' : (PROTOTIPOS,         'TC TM'),
  # Weather conditions
  'CC0' : ('PTR PTE PC PR PO', 'TAR TO1 TO2 TP TC TM'),
  'CC1' : ('PTR PTE PR PO',    'TAR TO1 TO2 TP TC TM'),
  'CC2' : ('PTR PTE PR PO',    'TAR TO1 TO2 TP TC TM'),
  'CN1' : ('PTE PR PO',        'TAR TP TC TM'),
  'CN2' : ('PTE PC PR PO',     'TAR TP TC TM'),
  'CN3' : ('PTE PC',           'TAR TP TC TM'),
  'CN4' : ('PC',               'TAR TP TC TM'),
  'CV'  : ('PV',               'TP TC TM'),
  'CTA1': ('PD PA',            'TD'),
  'CTA2': ('PD PA PV',         'TD TA2 CV'),
  'CTE1': ('PR',               'TM TO1 TO2'),
  # Animals
  'AMA' : (PROTOTIPOS,         'TD TA2'),
  'AAV' : (PROTOTIPOS,         'TAR TP TA1 TC TM'),
  'AMM' : (PROTOTIPOS,         'TO1 TO2 TAR'),
  'APE' : (PROTOTIPOS,         'TO1 TO2 SL TAR'),
  'AAL' : (PROTOTIPOS,         'TAR TP SL TO1'),
  'ACR' : (PROTOTIPOS,         'TAR TO1'),
  'AHQ' : (PROTOTIPOS,         'TAR TA1 TP TM'),
  'ARO' : (PROTOTIPOS,         'TAR TA1 TA2 TD TC TM'),
  'AFE' : (PROTOTIPOS,         'TAR TA1 TP TC TM SF1'),
  'ACA1': (PROTOTIPOS,         'TP TC TM SF1'),
  'ACA2': (PROTOTIPOS,         'TP TC TM SF1'),
  'AHOT': (PROTOTIPOS,         'TP TC TM SF1 SF2 SF3')
}

# Leitura de dados
proto = input()
I, J = input().split()
I, J = int(I), int(J)
mapa = []
for i in range(I):
  mapa.append(input().split())

regra1 = True
falha_r1={}
regra2 = True
falha_r2 = {}
regra3 = True
falha_r3 = {}
# Processamento de dados
for i in range(I):
  for j in range(J):
    coisas = mapa[i][j].split(',')
    paisagens=[]
    condicoes = []
    animais=[]
    cond=0
    c2 = 0
    for k in coisas[1:]:
      if k[0]=='A':
        animais.append(k)
      elif k[0]=='C':
        condicoes.append(k)
      elif k[0]=='S':
        paisagens.append(k)
    #regra 1
    if coisas[0] not in TERRENO_PROTO[proto][0] and coisas[0] not in TERRENO_PROTO[proto][1]:
      regra1=False
      falha_r1[f'{i},{j}']=coisas[0]
    #regra 2
    if mapa[(i-1)%I][j].split(',')[0] not in TERRENO_ADJACENCIA[coisas[0]]:
      regra2=False
      falha_r2[f'{i},{j}']=coisas[0]
    if mapa[(i+1)%I][j].split(',')[0] not in TERRENO_ADJACENCIA[coisas[0]]:
      regra2=False
      falha_r2[f'{i},{j}']=coisas[0]
    if mapa[i][(j-1)%J].split(',')[0] not in TERRENO_ADJACENCIA[coisas[0]]:
      regra2=False
      falha_r2[f'{i},{j}']=coisas[0]
    if mapa[i][(j+1)%J].split(',')[0] not in TERRENO_ADJACENCIA[coisas[0]]:
      regra2=False
      falha_r2[f'{i},{j}']=coisas[0]
    #regra 3
    for k in coisas[1:]:
      if proto not in ELEMENTOS[k][0]:
        regra3=False
        falha_r3[f'{i},{j}'] = coisas[0]
      if coisas[0] in ELEMENTOS[k][1]:
        continue
      else:
        if k == 'CTA2':
          for m in condicoes:
            if m in ELEMENTOS[k][1]:
              c2+=1
          if c2==0:
            regra3=False
            falha_r3[f'{i},{j}'] = coisas[0]
        elif k in 'APE AAL AFE ACA1 ACA2 AHOT':
          for m in paisagens:
            if m in ELEMENTOS[k][1]:
              cond+=1
          if cond==0:
            regra3=False
            falha_r3[f'{i},{j}'] = coisas[0]
        else:
          regra3=False
          falha_r3[f'{i},{j}'] = coisas[0]

# Saída de dados
print('regra 1')
if regra1:
  print('ok')
else:
  for i in falha_r1.keys():
    print(f'{i}:{falha_r1[i]}')
  print('falha')
print('regra 2')
if regra2:
  print('ok')
else:
  for i in falha_r2.keys():
    print(f'{i}:{falha_r2[i]}')
  print('falha')
print('regra 3')
if regra3:
  print('ok')
else:
  for i in falha_r3.keys():
    print(f'{i}:{falha_r3[i]}')
  print('falha')