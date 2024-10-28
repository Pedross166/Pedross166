###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Jogos Olímpicos
# Nome: Pedro Souza Santos
# RA: 288644
###################################################

# Leitura da quantidade de provas e pesos
N, O, P, B = [int(i) for i in input().split()]

paises={}
ordenada = []
fem=''
modalidades={}
listaM=[]
# Leitura das provas
for i in range(N):
    prova = input().split('-')
    for j in range(len(prova)):
        prova[j]=prova[j].strip()
    for b in prova[2:5]:
        if b not in paises.keys():
            paises[b]={'ouro': 0, 'prata': 0, 'bronze': 0, 'recorde': 0, 'pontos': 0, 'dobradinha': 0 }
    paises[prova[2]]['ouro'] += 1
    paises[prova[2]]['pontos'] += O
    if len(prova) == 6:
        paises[prova[2]]['recorde'] += 1
    paises[prova[3]]['prata'] += 1
    paises[prova[3]]['pontos'] += P
    paises[prova[4]]['bronze'] += 1
    paises[prova[4]]['pontos'] += B
    if prova[0] not in listaM:
        listaM.append(prova[0])
    modalidades[prova[0]+prova[1]] = prova[2]

for i in listaM:
    try: 
        if modalidades[i+'F']==modalidades[i+'M']:
            paises[modalidades[i+'F']]['dobradinha']+=1
    except:
        pass

        
# Ordenação pelo Critério Oficial
print('Critério Oficial:')
ouros, pratas, bronzes = [], [], []
for i in paises.keys():
    if paises[i]['ouro'] not in ouros:
        ouros.append(paises[i]['ouro'])
    if paises[i]['prata'] not in pratas:
        pratas.append(paises[i]['prata'])
    if paises[i]['bronze'] not in bronzes:
        bronzes.append(paises[i]['bronze'])
ouros.sort()
pratas.sort()
bronzes.sort()
ord=[]
oord=[]
pord=[]
bord=[]
for i in ouros:
    for j in paises.keys():
        if paises[j]['ouro']==i:
            oord.append(j)
    for k in pratas:
        for h in oord:
            if paises[h]['prata']==k:
                pord.append(h)
        for l in bronzes:
            for m in pord:
                if paises[m]['bronze']==l:
                    bord.append(m)
            bord.sort(reverse=True)
            ord+=bord
            bord=[]
        pord=[]
    oord=[]

ord=ord[::-1]
s=' - '.join(ord)
print(s)

# Ordenação Ponderado
print('Ponderado:')
pond=[]
for i in paises.keys():
    if paises[i]['pontos'] not in pond:
        pond.append(paises[i]['pontos'])
pond.sort()
ord = []
semiord = []
for i in pond:
    for j in paises.keys():
        if paises[j]['pontos']==i:
            semiord.append(j)
    semiord.sort()
    semiord=semiord[::-1]
    ord+=semiord
    semiord=[]
ord=ord[::-1]
pond=' - '.join(ord)
print(pond)

# Ordenação por Recordes Olímpicos
print('Recorde Olímpico:')
ro=[]
ord=[]
for i in paises.keys():
    if paises[i]['recorde'] not in ro:
        ro.append(paises[i]['recorde'])
ro.sort()
recordistas=[]
for t in ro:
    for q in paises.keys():
        if paises[q]['recorde']==t:
            recordistas.append(q)
    for i in ouros:
        for j in recordistas:
            if paises[j]['ouro']==i:
                oord.append(j)
        for k in pratas:
            for h in oord:
                if paises[h]['prata']==k:
                    pord.append(h)
            for l in bronzes:
                for m in pord:
                    if paises[m]['bronze']==l:
                        bord.append(m)
                bord.sort(reverse=True)
                ord+=bord
                bord=[]
            pord=[]
        oord=[]
    recordistas=[]
ord=ord[::-1]
s=' - '.join(ord)
print(s)


# Ordenação por Dobradinha
print('Dobradinha:')
dobra=[]
ord=[]
for i in paises.keys():
    if paises[i]['dobradinha'] not in dobra:
        dobra.append(paises[i]['dobradinha'])
dobra.sort()
dobradas=[]
for t in dobra:
    for q in paises.keys():
        if paises[q]['dobradinha']==t:
            dobradas.append(q)
    for i in ouros:
        for j in dobradas:
            if paises[j]['ouro']==i:
                oord.append(j)
        for k in pratas:
            for h in oord:
                if paises[h]['prata']==k:
                    pord.append(h)
            for l in bronzes:
                for m in pord:
                    if paises[m]['bronze']==l:
                        bord.append(m)
                bord.sort(reverse=True)
                ord+=bord
                bord=[]
            pord=[]
        oord=[]
    dobradas=[]
ord=ord[::-1]
s=' - '.join(ord)
print(s)