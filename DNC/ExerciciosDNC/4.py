""""
Questão 4.
Faça um script que você coloque a quantidade de dias e descubra em
qual trimestre esse dia está no ano.
"""
# Recebendo do usuário o número de dias e armazenando em "dia"
dia = int(input("Digite um número de dias do ano "))

# Fiz uma gambiarra aqui(kk)
# Para saber em qual trismestre o dia se encontra, simplesmente
# somei os dias dos meses de cada trismestre. Exemplo: jan tem 31,
# fev 28, mar 31 = 90 dias no primeiro trimestre, e assim por diante.

# Criando uma variável para armazenar o trimestre
trim = any

# Descobrindo em qual trimestre se encontra o ano através de uma
# série de condicionais
if dia <= 90:
    trim = "primeiro"
elif dia <= 181:
    trim = "segundo"
elif dia <= 273:
    trim = "terceiro"
else:
    trim = "quarto"

# Retornando ao usuário em qual trimestre se encontra o dia
print(f"O dia está no {trim} trimestre.")

# Primeira forma de resolução(menos sintática):
"""# Testando se o dia se encontra no primeiro trimestre
if dia <= 90:
    print("O dia está no primeiro trimestre")

# Testando se o dia se encontra no segundo trimestre
elif dia <= 181:
    # Informando o trismestre para o usuário
    print("O dia está no segundo trimestre")

# Testando se o dia se encontra no terceiro trimestre
elif dia <= 273:
    # Informando o trismestre para o usuário
    print("O dia está no terceiro trimestre")

# Testando se o dia se encontra no quarto trimestre
else:
    # Informando o trismestre para o usuário
    print("O dia está no quarto trimestre")"""
