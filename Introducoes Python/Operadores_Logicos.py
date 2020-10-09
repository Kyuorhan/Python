""" Operadores Lógicos """

"""
    AND     # Somente se as duas condições da variavel for True(Verdadeiro), sera True... Se não False(Falso)
    OR      # Somente uma das condições da variável for True, sera True... Se não False
    NOT     # Inverte umas da condições do valor... Ex:True --> False or(ou) False --> True

"""
x = 7
y = 7
z = 8
print("AND:",x == y and x == z)                 # Somente se as duas condições for True
print("OR:",x == y or x == z)                  # Somente umas das condições for True
print("AND/OR:",x == y and x == z or z == y)
