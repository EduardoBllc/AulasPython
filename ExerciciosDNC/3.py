"""
Questão 3.
A fisioterapeuta que você vai gosta muito de brincar com números, e
pediu para você criar um sistema que verifique se a altura inserida é
par ou impar"""

# Recebendo a altura do usuário e armazenando na variável "altura"
altura: int = int(input("Qual sua altura em cm? "))
# Checando se a divisão inteira por 2 da altura fornecida resulta em resto 0 ou 1
# sendo que se resultar 0 é par e se resultar 1 é ímpar
if altura % 2 == 0:
    # Informando ao usuário no console que a altura fornecida é par
    print("Sua altura é um número par!")
else:
    # Informando ao usuário no console que a altura fornecida é ímpar
    print("Sua altura é um número ímpar!")
