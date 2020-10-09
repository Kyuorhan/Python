import random
    #   Import a biblioteca
ranking_nome = []
ranking_score = []
    #   2 Variavel do nome e os pontos do jogador
again = True

while again:
    aleatorio = random.randint(0, 100)
    nome = input("Digite o nome do player: ")
        #   Enquanto[While]-again for verdadeiro sorteia numero de 0 a 100
    num = int(input("Digite um número: "))
        #   Digite um valor inteiro
    cont = 1

    if aleatorio == num:
            #   Se[if]-aleatorio for igual num/Numero sorteado
        print("Acertoooo mizeravi!!")
            #   Então printe esta mensagem
        print("Você acertou de primeira. Tá pica irmão!!")
            #   Então printe esta mensagem
    while aleatorio != num:
        #   Enquanto[While]-aleatorio foi diferente ou igual num/Numero sorteado
        cont += 1
        if aleatorio > num:
            #   Se[if]-aleatorio for maior num/Numero sorteado
            print("Maior, porra!")
                #   Printe esta mensagem
        elif aleatorio < num:
            #   Se[elif] for menor num/Numero sorteado
            print("Menor, caraio!")
                #   Printe esta mensagem
        num = int(input("Digite novamente: "))
    if (len(ranking_nome) == 0):
        #   Se[if] Leia ranking_nome igual a 0
        ranking_nome.append(nome)
        ranking_score.append(cont)
            #   É um método adiciona um único item ao final da lista
    else:
        for i in range(len(ranking_score)):
            if cont <= ranking_score[i]:
                ranking_nome.insert(i, nome)
                ranking_score.insert(i, cont)
                break
            elif cont >= ranking_score[-1]:
                ranking_nome.append(nome)
                ranking_score.append(cont)
                break

    op = input("Deseja jogar novamente? (S/N)")
    while (op != 'S' and op != 's' and op != 'N' and op != 'n'):
        op = input("Deseja jogar novamente? (S/N)")
    if op == 'n' or op == 'N':
        again = False
print()
print('--------RANKING--------')
for j in range(len(ranking_nome)):
    print(f'{ranking_nome[j]}: {ranking_score[j]} tentativas')