from math import hypot
a=float(input('comprimento do cateto adjacente:'))
o=float(input('comprimento do cateto oposto:'))
h=hypot(a,o)
print('O comprimento da hipotenusa mede {}' .format(h))