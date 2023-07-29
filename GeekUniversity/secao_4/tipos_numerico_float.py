"""
Tipo numéricos - inteiros

OBS: É sempre interessante olhar o dir do tipo de dados que stá se usando
"""

num = 1_000_000
print(num)

num = 43
num = num // 2

print(num)

print(type(num))
print()

"""
Tipo Float

Tipo real, decimal

Casa decimais

OBS: O separador de casas de decimais é o ponto (".") e não a vírgula (",")
"""

# "Errado" -> (gera uma array)
valor = 1, 44
print(valor)

# "Certo" -> (gera uma float)
valor = 1.44
print(valor)
print(type(valor))
print()

# É possível dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(valor2)
print()

# É possível converter um float em int ou vice-versa
res = int(valor)
print(res)
print(type(res))
res = float(res)
print(res)
print(type(res))
print()

# Podemos trabalhar com números complexos
complexo = 5j
print(complexo)
print(type(complexo))


