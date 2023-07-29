"""
Tipo Booleano
Algebra Booleana, criada por George Boole

2 constantes - Verdadeiro ou Falso

errado:
true, false

Certo:
True, False
"""
ativo = True

print(ativo)
print()

"""
Operações básicas
"""

# Negação (not):
"""
Inverte o valor de True para False ou vice-versa
"""
print(not ativo)
print()

# Ou (or):
"""
É uma operação binária(depende de dois valores). Pelo menos um dos dois deve ser verdadeiro para validar a sentença.
"""

valor1 = 10
valor2 = 20

if valor1 == 10 or valor2 == 10:
    print(True)
else:
    print(False)

# E (and)
"""
Também é uma operação binária. Os dois valores devem ser verdadeiros para validar a sentença.
"""
print()
if valor1 == 10 and valor2 == 10:
    print(True)
else:
    print(False)
