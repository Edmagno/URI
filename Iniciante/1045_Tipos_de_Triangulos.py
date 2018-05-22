linha = raw_input().split()

a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

def maior(a,b):
    if a > b:
        return a
    else:
        return b
def menor(a,b):
    if a < b:
        return a
    else:
        return b
primeiro = maior(maior(a,b),c)
ultimo = menor(menor(a,b),c)


if a >= ultimo and a <= primeiro:
    if b<=a and c>=a or b>=a and c<=a:
        segundo = a
if b >= ultimo and b<=primeiro:
    if c<=b and a>=b or c>=b and a<=b:
        segundo = b
if c >= ultimo and c <=primeiro:
    if a<=c and b>=c or a>=c and b<=c:
        segundo = c

if primeiro >= (segundo+ultimo):
    print 'NAO FORMA TRIANGULO'
else:
    if (primeiro**2) == (segundo**2)+(ultimo**2):
        print 'TRIANGULO RETANGULO'
    if (primeiro**2) > (segundo**2)+(ultimo**2):
        print 'TRIANGULO OBTUSANGULO'
    if (primeiro**2) < (segundo**2)+(ultimo**2):
        print 'TRIANGULO ACUTANGULO'
    if a == b and a == c:
        print 'TRIANGULO EQUILATERO'
    if primeiro == segundo and primeiro!= ultimo or primeiro == ultimo and primeiro!=segundo or segundo == ultimo and segundo !=primeiro:
        print 'TRIANGULO ISOSCELES'
