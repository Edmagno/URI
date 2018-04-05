#include <stdio.h>
#include <stdlib.h>

int main()
{
int valor,hora=0,minuto=0,segundo=0;
scanf("%d",&valor);
while(valor>0){
    if(valor>=3600)
    {
        hora=hora+1;
        valor=valor-3600;
    }
    else if(valor>=60)
    {
        minuto=minuto+1;
        valor=valor-60;
    }
    else if(valor<60)
    {
        segundo = valor;
        valor =0;
    }
}
printf("%d:%d:%d\n",hora,minuto,segundo);
return 0;
}
