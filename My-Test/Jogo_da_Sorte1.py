import random

ranking_nome = []
ranking_score = []
again = True

while again:
    aleatorio = random.randint(0, 100)
    nome = input("Digite o nome do player: ")

    num = int(input("Digite um número: "))
    cont = 1

    if aleatorio == num:
        print("Acertoooo mizeravi!!")
        print("Você acertou de primeira. Tá pica irmão!!")

    while aleatorio != num:
        cont += 1
        if aleatorio > num:
            print("Maior, porra!")
        elif aleatorio < num:
            print("Menor, caraio!")
        num = int(input("Digite novamente: "))

    if (len(ranking_nome) == 0):
        ranking_nome.append(nome)
        ranking_score.append(cont)
    else:
        for i in range(len(ranking_nome)):
            if cont <= ranking_score[i]:
                ranking_nome.insert(i, nome)
                ranking_score.insert(i, cont)
                break
            elif cont >= ranking_score[i] and cont == ranking_score[i+1]:
                ranking_nome.insert(i+1, nome)
                ranking_score.insert(i+1, cont)

    op = input("Deseja jogar novamente? (S/N)")
    while (op != 'S' and op != 's' and op != 'N' and op != 'n'):
        op = input("Deseja jogar novamente? (S/N)")
    if op == 'n' or op == 'N':
        again = False
    print(ranking_nome)
    print(ranking_score)
print(ranking_nome)
print(ranking_score)