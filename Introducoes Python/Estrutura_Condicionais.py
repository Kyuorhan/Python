""" Estrutura Condicionais [if/else] """

x = int(input("Digite um valor de x: "))
y = int(input("Digite um valor de y: "))
if x == y:
    print("São valores Iguais")
elif x > y:
    print("x é Maior que y")
else:
    print("x não é Maior que y")


""" Estrutura Condicionais [elif] """

x = int(input("Digite um valor de x: "))
y = int(input("Digite um valor de y: "))

if  x == y:
    print("São valores Iguais")
elif x < y:
    print("x não é Menor y:")
elif y > x:
    print("y não é Maior que x;")
else:
    print("São valores Diferente")

""" Exemplo """

x = int(input("Digite um valor de x:"))
y = int(input("Digite um valor de y:"))

if x == y:
    print("São numeros Iguais")
else:
    print("Não são numeros Iguais")

x = int(input("Digite um valor x:"))
y = int(input("Digite um valor y:"))

if x > y:
    if y > 0:
        print("y é maior que x\nb é positivo")
    else:
        print("y não é maior que x nem positivo")
else:
    print("y é menor que x")


    