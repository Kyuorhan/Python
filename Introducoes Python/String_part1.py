""" Strings Pate 1 """

"""  String é um tipo de dados  em que se armazena coleções  de caracteres  (texto)  """

"""
    As strings são delcaradas entre aspas
                            
                            var1 = 1
                            var2 = "1"
                            
    Nesse exemplo var1 é um numeral, enquanto var2 é uma string 
"""

""" Concatenação """

var1 = "Eu nao vivo sem"
var2 = "Music"

contecatenaçao = var1 + ", "+ var2 # para da um espaço so colocar entre aspas[var1 + " " + var2]
print(contecatenaçao)   # vai juntar(somar) as duas variaveis de string [var1 + " " + var2]
caracteres = len(contecatenaçao)
print(caracteres)

""" separar as palavras [Horizontal/Vertical] """

print(var1[0],var1[1],var1[2],var1[3],var1[4],var1[5],var1[6],var1[7],var1[8],var1[9],var1[10],var1[11],var1[12],var1[13],var1[14],)
#Horizontal
print(var2[0])
print(var2[1])
print(var2[2])
print(var2[3])
print(var2[4])
#Vertical

""" Concatenar posição """

print(contecatenaçao[0:],var2[0:5],var2[0])
# vai imprimir [0 até ou fim], ou [0 até posição 5], ou [somente posição 0]


