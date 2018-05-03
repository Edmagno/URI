import math

linha = raw_input().split()
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

delta = (b**2)-4*a*c

if delta>=0 and a!=0:
    r1=(-b+ math.sqrt(delta))/(2*a)
    r2=(-b- math.sqrt(delta))/(2*a)
    print('R1 = {}'.format(round(r1,5)))
    print('R2 = {}'.format(round(r2,5)))
else:
    print('Impossivel calcular')
