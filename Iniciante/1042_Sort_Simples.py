linha = raw_input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

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

if a > ultimo and a < primeiro:
    segundo = a
elif b > ultimo and b < primeiro:
    segundo = b
else:
    segundo = c


print '{}'.format(ultimo)
print '{}'.format(segundo)
print '{}\n'.format(primeiro)

print '{}'.format(a)
print '{}'.format(b)
print '{}'.format(c)
