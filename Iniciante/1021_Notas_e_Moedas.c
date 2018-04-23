#include <stdio.h>

int main() {

    double dinheiro1,dinheiro;
          int numeros1000=0,numeros500=0,numeros20=0,numeros100=0,numeros5=0,numeros2=0,numeros1=0,numeros50=0, numeros25=0,numeros10=0, numeros05=0, numeros01=0;
          scanf("%lf", &dinheiro);
          dinheiro1=dinheiro;
           while(dinheiro>=100.00)  { dinheiro = dinheiro -100.00; numeros1000++;}
           while(dinheiro>=50.00)   { dinheiro = dinheiro - 50.00; numeros500++;}
           while(dinheiro>=20.00)   { dinheiro = dinheiro - 20.00; numeros20++;}
           while(dinheiro>=10.00)   { dinheiro = dinheiro - 10.00; numeros100++;}
           while(dinheiro>=5.00)    { dinheiro = dinheiro - 5.00; numeros5++;}
           while(dinheiro>=2.00)    { dinheiro = dinheiro - 2.00; numeros2++;}
           while(dinheiro>=1.00)    { dinheiro = dinheiro - 1.00; numeros1++;}
           while(dinheiro >=0.50) { dinheiro = dinheiro - 0.50; numeros50++;}
           while(dinheiro >=0.25) { dinheiro = dinheiro - 0.25; numeros25++;}
           while(dinheiro >=0.10) { dinheiro = dinheiro - 0.10; numeros10++;}
           while(dinheiro >=0.05) { dinheiro = dinheiro - 0.05; numeros05++;}
           while(dinheiro >=0.01) { dinheiro = dinheiro - 0.01; numeros01++;}
           printf("NOTAS:\n");
           printf("%d nota(s) de R$ 100.00\n",numeros1000);
           printf("%d nota(s) de R$ 50.00\n", numeros500);
           printf("%d nota(s) de R$ 20.00\n", numeros20);
           printf("%d nota(s) de R$ 10.00\n", numeros100);
           printf("%d nota(s) de R$ 5.00\n",  numeros5);
           printf("%d nota(s) de R$ 2.00\n",  numeros2);
           printf("MOEDAS:\n");
           printf("%d moeda(s) de R$ 1.00\n", numeros1);
           printf("%d moeda(s) de R$ 0.50\n", numeros50);
           printf("%d moeda(s) de R$ 0.25\n", numeros25);
           printf("%d moeda(s) de R$ 0.10\n", numeros10);
           printf("%d moeda(s) de R$ 0.05\n", numeros05);
           printf("%d moeda(s) de R$ 0.01\n", numeros01);

    return 0;
}
