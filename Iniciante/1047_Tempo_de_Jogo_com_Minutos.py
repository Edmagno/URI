linha = raw_input().split()
hi = int(linha[0])
mi = int(linha[1])
hf = int(linha[2])
mf = int(linha[3])

if hf == hi:
    if mf > mi:
        hora = hf - hi
        minuto = mf -mi
    if mi > mf:
        hora = (24 -(hf - hi))-1
        minuto = 60 -(mi-mf)
    if mi == mf:
        hora = 24
        minuto = 0


if hf > hi:
    if mf>mi:
        hora = hf - hi
        minuto = mf - mi
    if mi>mf:
        hora = (hf - hi)-1
        minuto = 60 -(mi-mf)
    if mi==mf:
        hora = hf - hi
        minuto = mf - mi
if hi > hf:
        if mf>mi:
            hora = 24 -(hi-hf)
            minuto = mf - mi
        if mi>mf:
            hora = (24 -(hi-hf)) -1
            minuto = 60 -(mi-mf)
        if mi == mf:
            hora = 24 -(hi-hf)
            minuto = mf - mi




print 'O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora,minuto)
