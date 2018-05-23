salario = float(input())

if salario >= 0.00 and salario <= 2000.00:
    print 'Isento'
elif salario >= 2000.01 and salario <= 3000.00:
    taxa = salario - 2000.00
    imposto = taxa*0.08
    print 'R$ {:.2f}'.format(imposto)
elif salario >= 3000.01 and salario <= 4500.00:
    taxa = salario -3000.00
    imposto = (1000*0.08)+(taxa*0.18)
    print 'R$ {:.2f}'.format(imposto)
else:
    taxa = salario -4500.00
    imposto = (1000.00*0.08) + (1500.00*0.18) + (taxa*0.28)
    print 'R$ {:.2f}'.format(imposto)
