#include <stdio.h>
#include <stdlib.h>

int main()
{
int tempo,velocidade;
double litros;
scanf("%d",&tempo);
scanf("%d",&velocidade);
litros = (velocidade*tempo)/12.000;
printf("%.3lf\n",litros);
return 0;
}
