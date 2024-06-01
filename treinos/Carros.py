D=int(input('Por quantos dias você alugou o carro? '))
K=float(input('Quantos kilometros você rodou com o carro? '))
P=60*D+0.15*K
print('O valor a pagar pelo aluguel do carro é {:.2f}.'.format(P))
