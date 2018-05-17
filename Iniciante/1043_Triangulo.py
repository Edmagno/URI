linha = raw_input().split()

a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

if abs(b-c) < a < (b+c) or abs(a-c) < b < (a+c) or abs(a-b) < c < (a+b):
    print 'Perimetro = {:.1f}'.format(a+b+c)
else:
    print 'Area = {:.1f}'.format(((a+b)*c)/2)
