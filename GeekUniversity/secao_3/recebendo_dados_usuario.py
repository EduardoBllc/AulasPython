from datetime import date
"""
Recebendo dados do usuário

Input() -> Todo dado recebido do tipo input é do tipo String
"""

# Entrada de dados
# print("Qual seu nome?")
# Armazenando dados na variável "nome"
# nome = input()
nome = input('Qual se nome? ')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)
# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))
# Exemplo de print 'mais atual'  3.7
print(f'Seja bem-vindo(a) {nome}')

# Armazenando dados na variável "idade"
# print("Qual sua idade? ")
# idade = input()
idade = int(input('Qual sua idade? '))

# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2.x
# print('%s tem %s anos' % (nome, idade))
# Exemplo de print 'moderno' 3.x
# print('{0} tem {1} anos'.format(nome, idade))
# Exemplo de print 'mais atual'  3.7
print(f'{nome} tem {idade} anos')

data_atual = date.today().year
print(f'{nome} nasceu em {data_atual - idade} ou {data_atual - idade - 1}')


