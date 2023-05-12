"""
Questão 1.
Seu primeiro desafio é desenvolver um programa para um depósito de
bebidas que valide venda de bebidas para maiores de idade (maior ou
igual 18 anos) no mercado, o programa deve receber do usuário os
valores do nome e ano que ele nasceu e retornar se ele pode comprar
bebidas."""

print("Bem-vindo à loja de bebidas")

# Recebendo o nome fornecido pelo usuário e armazendo na variável "nome"
nome: str = input("Qual seu nome? ")

# Recebendo o ano de nascimento fornecido pelo usuário e armazendo na variável "nome"
ano: int = int(input('Que ano você nasceu? '))

# Testando se segundo o ano de nascimento que o usuário forneceu ele seria maior de idade
if (2023 - ano) >= 18:
    # Imprimindo no console a mensagem informando que o usuário é maior de idade e pode
    # comprar bebidas
    print("Bom dia {}, você pode comprar bebidas!".format(nome))
else:
    # Imprimindo no console a mensagem informando que o usuário NÂO é maior de idade e NÃO
    # pode comprar bebidas
    print(f'Bom dia {nome}, você NÃO pode comprar bebidas!')
