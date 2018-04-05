#include <stdio.h>

int main() {

    int idade,ano,c,mes,e,dia;

    scanf("%d",&idade);

    ano=idade/365;
    c=idade%365;

    mes=c/30;
    e=c%30;

    dia=e/1;
    printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n",ano,mes,dia);
    return 0;
}
