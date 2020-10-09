""" String parte 2 """
""" Métodos """

"""
    Em Python, strigns são objetos
    Pode-se aplicar métodos a strings
        
                string = srting.método()
                
"""
""" Métodos [Lower/Upper] """

x = "Não vivo sem MUSIC"
y = "Not dead life MUSIC"
'''
concatenar = x + ", " + y

print(concatenar)
print(concatenar.lower()) # Deixa tudo Menusculo
print(concatenar.upper()) # Deixa tudo Maisculo
# Podemos utilizar na Variavel tbem
concatenar = concatenar.lower()
print(concatenar)'''

""" Métodos [Strip] """

concat = x + ", " + y + "\n"
print(concat.strip())
# Strip ele remove caracteres especial, espaço ou quebra de linha etc

""" Métodos [Split] """

split = "O rato roeu a roupa do rei de Roma"
lista1 = split.split()
print(lista1) # Splite converteu a string por espaço etc[split()] fazendo uma lista
lista2 = split.split("r")
print(lista2) # Split tbem pode quebra uma letra tipo "r" [remove oq tiver "r"]
