linha = raw_input().split()
a = int(linha[0])
b = int(linha[1])

if a == b:
    print 'O JOGO DUROU 24 HORA(S)'
elif a > b:
    c = (24 -a) + b
    print 'O JOGO DUROU {} HORA(s)'.format(c)
else:
    c = b - a
    print 'O JODO DUROU {} HORA(S)'.format(c)
