""" Comando input """

"""
    No caso vou criar uma Variável para executa-la em pront de comando - cmd
    cd desktop          --  Pasta selecionada
    dir                 --  Local do arquivo
    cd ..               --  Retorna na Pasta anterior
    
"""
idade = int(input("Qual a sua Idade:"))
#   Cria uma variável(idade)
#   input: São comando inviado pelo usuario para o programa, permite interação pelo programa
print("Sua idade é:",idade)

nome = str(input("Qual seu nome completo: "))
nrua = str(input("Qual o seu endereço da sua Rua: "))
ncasa = int(input("Numero do endereço da sua casa: "))
nbairro = str(input("Qual o seu bairro: "))
cpf = int(input("Qual seu cpf: "))
nacio = str(input("Qual sua  Nacionalidade: "))
print("Bem vindo {}\nSeu enderço da sua rua é {} {} no bairro {}\nE seu CPF é {} Nacionalidade: {}"
      .format(nome, nrua, ncasa, nbairro, cpf, nacio))

peso = float(input("Qual o seu peso: "))
print("Seu peso é {}kg".format(peso))

