#include <stdio.h>
#include <stdlib.h>

int main()
{
int numero, horas;
double valor, salario;
scanf("%d",&numero);
scanf("%d",&horas);
scanf("%lf",&valor);
salario = horas*valor;
printf("NUMBER = %d\n",numero);
printf("SALARY = U$ %.2lf\n",salario);
return 0;
}
