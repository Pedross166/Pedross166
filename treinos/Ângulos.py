from math import radians, sin, cos, tan
# theta=float(input('insira um ângulo em graus: '))
alpha=float(input('insira um ângulo em radiano: '))
# alpha=radians(theta)
s=sin(alpha)
c=cos(alpha)
t=tan(alpha)
# print('O seno de {0}° vale {1}, o cosseno de {0}° vale {2} e a tangente de {0}° vale {3}'.format(theta, s, c, t ))3
print('O seno de {0} vale {1}, o cosseno de {0} vale {2} e a tangente de {0} vale {3}'.format(alpha, s, c, t ))
