""" Estrutura de Repetição (For e Range) """

""" Para/Alcançar - For/Range """
print('---Teste---')
for i in range(10):
    # Para i in Alcançar(Paramentros);
    # Ex se: paramentros for valor 10, (For i in Range)vai alcança até um determinado valor, 1 até o 10;
    # Lembre-se q a contagem em computação patrão sempre comece pelo valor 0;
    # Então se Valor do parametros for 10, no caso 10 não sera exibido: Porque sempre começa pelo 0 <--(0,1,2,3,4,5,6,7,8,9);
    print(i)
print('---Teste---')
for i in range(15,20):
    # Ex: eu posso utiliza 2 elementos para uma contagem a partir do 15 para 20;
    print(i)
print('---Teste---')
for i in range(1,20,2):
    """
    Tambem posso utiliza mais um elemento pra determinar uma contagem pra aquele valor
    Ex tenho 3 elementos:   primeiro determina paramentro;
                            segundo a contagem que determina daquele parametro;
                            terceiro que imprimi em quantos valor para aquela contagem;
    No caso (for i in range(10,20,2))--> ta pedindo que conte de 10 a 20, determinando a contagem 2 em 2
    """
    print(i)