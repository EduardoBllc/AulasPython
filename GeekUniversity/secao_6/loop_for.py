"""
Estruturas de repetição
For

C ou Java:
for(i = 0; i < limitador; i++){
    //Execução do loop
}

Python:
for i in interável:
    //Execução do loop

Utiliza-se loops para iterar sobre sequências de valores ou sobre valores iteráveis

Exemplos de iteráveis:
- String
nome = "Eduardo Salvagni Ballico"

- Lista
lista = [1, 3, 5, 7, 9]

- Range
numeros = range(1,10)
"""

nome = "Eduardo Salvagni Ballico"

lista = [1, 3, 5, 7, 9]

numeros = range(1, 10)

# Range
"""
range(valor_inicial, valor_final, passo)
OBS: O valor final não é incluído
"""

# Exemplos simples
"""
for letra in nome:
    print(letra)

for item in lista:
    print(item)

for numero in numeros:
    print(numero)
"""

# Enumerate
"""
Método que itera algo e retorna o valor e o indíce do valor em uma tupla

lista = [1, 3, 5, 7, 9]

valor = [valor for valor in enumerate(lista)]
print(valor) -> [(0, 1), (1, 3), (2, 5), (3, 7), (4, 9)]

ou então separando e retornando em duas variáveis diferentes

valor = [f"índíce: {i} -> valor: {v}" for i, v in enumerate(lista)]
print(valor) -> ['índíce: 0 -> valor: 1', 'índíce: 1 -> valor: 3',
                 'índíce: 2 -> valor: 5', 'índíce: 3 -> valor: 7', 'índíce: 4 -> valor: 9']
"""
