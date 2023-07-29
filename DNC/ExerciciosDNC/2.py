"""
Questão 2.
Esse bimestre na faculdade você precisa tirar nota 8 de média para
passar na matéria, desenvolva um script que leia a nota de suas
últimas 3 provas, tire a média delas e verifique se você passou"""

# Recebendo do usuário a primeira nota e armazenando na variável "nota1"
nota1: float = float(input("Qual foi a nota da sua primeira prova? "))

# Recebendo do usuário a segunda nota e armazenando na variável "nota2"
nota2: float = float(input("Qual foi a nota da sua segunda prova? "))

# Recebendo do usuário a terceira nota e armazenando na variável "nota3"
nota3: float = float(input("Qual foi a nota da sua terceira prova? "))

# Checando segundo as notas do usuário se ele atingiu a média
if (nota1+nota2+nota3)/3 >= 8:
    # Informando ao usuário no console que ele atingiu a média
    print("Você atingiu a nota média necessária!")
else:
    # Informando ao usuário no console que ele NÃO atingiu a média
    print("Você NÃO atingiu a nota média necessária!")
