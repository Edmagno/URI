valor = input()
n100=0;n50=0;n20=0;n10=0;n5=0;n2=0
m1=0;m50=0;m25=0;m10=0;m05=0;m01=0

c = int(valor);
r = int(round((valor - c)*100));

n100 = c / 100;
c = c - n100 * 100;
n50 = c / 50;
c = c - n50 * 50;
n20 = c / 20;
c = c - n20 * 20;
n10 = c / 10;
c = c - n10 * 10;
n5 = c / 5;
c = c - n5 * 5;
n2 = c / 2;
c = c - n2 * 2;	

m1 = c;
m50 = r / 50;
r = r - m50 * 50;
m25 = r / 25;
r = r - m25 * 25;
m10 = r / 10;
r = r - m10 * 10;
m05 = r / 5;
r = r - m05 * 5;
m01 = r;
		
print 'NOTAS:'
print n100,'nota(s) de R$ 100.00'
print n50, 'nota(s) de R$ 50.00'
print n20, 'nota(s) de R$ 20.00'
print n10, 'nota(s) de R$ 10.00'
print n5, 'nota(s) de R$ 5.00'
print n2, 'nota(s) de R$ 2.00'
print 'MOEDAS:'
print m1, 'moeda(s) de R$ 1.00'
print m50, 'moeda(s) de R$ 0.50'
print m25, 'moeda(s) de R$ 0.25'
print m10, 'moeda(s) de R$ 0.10'
print m05, 'moeda(s) de R$ 0.05'
print m01, 'moeda(s) de R$ 0.01'