#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
double fixo, salario, vendas;
string nome;
cin>>nome;
cin>>fixo>>vendas;
salario = fixo + (0.15*vendas);
cout<<fixed<<setprecision(2)<<"TOTAL = R$ "<<salario<<endl;

return 0;
}
