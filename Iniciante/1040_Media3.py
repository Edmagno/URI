linha = raw_input().split()
n1 = float(linha[0])
n2 = float(linha[1])
n3 = float(linha[2])
n4 = float(linha[3])

media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

print 'Media: {:.1f}'.format(media)
if media >= 7.0:
    print 'Aluno aprovado.'
elif media < 5.0:
    print 'Aluno reprovado.'
else:
    print 'Aluno em exame.'
    exame = float(input())
    final = (exame + media)/2
    if final>=5.0:
        print 'Nota do exame: {:.1f}'.format(exame)
        print 'Aluno aprovado.'
        print 'Media final: {:.1f}'.format(final)
    else:
        print 'Nota do exame: {:.1f}'.format(exame)
        print 'Aluno reprovado.'
        print 'Media final: {:.1f}'.format(final)
