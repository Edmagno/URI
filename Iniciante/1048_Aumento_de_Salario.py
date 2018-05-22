salario = float(input())

if salario >= 0.00 and salario <= 400.00:
    coef = 0.15
    percentual = 15
elif salario >=400.01 and salario <= 800.00:
    coef = 0.12
    percentual = 12
elif salario >=800.01 and salario <= 1200.00:
    coef = 0.10
    percentual = 10
elif salario >= 1200.01 and salario <= 2000.00:
    coef = 0.07
    percentual = 7
else:
    coef = 0.04
    percentual = 4

novo = salario +(salario*coef)
reajuste = novo - salario
print 'Novo salario: {:.2f}'.format(novo)
print 'Reajuste ganho: {:.2f}'.format(reajuste)
print 'Em percentual: {} %'.format(percentual)
