# include<iostream>
# include<stdlib.h>
# define MAX 3
using
namespace
std;

void
atribuiValores(int * A, int * B, int * C, int * D)
{
for (int i = 0; i < MAX; i++)
{
for (int j = 0; j < MAX; j++)
{
if (A[i] == B[j])
C[i] = A[i];
}
}

for (int i = 0; i < MAX; i++)
{
for (int j = 0; j < MAX; j++)
{
if (A[i] != B[j])
D[i] = A[i];
else
{
D[i] = NULL;
break;
}
}
}
}

void
exibeTela(char
nome, int * vetor)
{
for (int i = 0; i < MAX; i++)
{
if (i == 0)
printf("%c = {", nome);

if (vetor[i] != NULL)
(i == (MAX - 1)) ? cout << vetor[i]: cout << vetor[i] << ", ";

if
(i == (MAX - 1))
cout << "}\t";
}
}

void inicializaNULL(int * vetor)
{
    for (int(i = 0); i < MAX; i++)
        vetor[i] = NULL;
}

int main()
{
    int A[MAX], B[MAX];

    for (int j = 0; j < 2; j++)
    {
        for (int i = 0; i < MAX; i++)
        {
            (j == 0) ? cout << "Valor de A[" << i+1 << "]: ": cout << "Valor de B[" << i + 1 << "]: ";
            (j == 0) ? cin >> A[i]: cin >> B[i];
}
}

system("cls");

exibeTela('A', A);
exibeTela('B', B);
cout << endl << endl;

int(C[MAX], D[MAX]);

inicializaNULL(C);
inicializaNULL(D);

atribuiValores(A, B, C, D);

exibeTela('C', C);
exibeTela('D', D);

return 0;
}