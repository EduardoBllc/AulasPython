"""
Questão 5.
Desenvolva um sistema que leia 3 números e diga qual é o maior (se
houver empate, exiba os empatados).
"""

# Criando um vetor para armazenar os números fornecidos,
# uma variável numérica para o maior e duas de String para
# caso ocorra empate
n = [0, 0, 0]
maior = 0
empate = any
posicao_maior = any

# Recebendo os números do usuário
n[0] = int(input("Digite o n1 "))
n[1] = int(input("Digite o n2 "))
n[2] = int(input("Digite o n3 "))

# Aqui fui um pouco além do proposto no módulo, já que não entramos
# em laços de repetição até o fornecimento destas atividades, mas como
# achei mais prático do que encher de if's e elses, fiz dessa maneira:

# Criei um laço de repetição para iterar o vetor, retornando cada valor
# numérico dentro do mesmo e testar se o número que ele possui é maior
# do que o armazenado na variável "maior"
for num in range(3):
    if n[num] > maior:
        # Caso ele for maior, substituo o valor de maior pelo valor do
        # número do vetor para o qual a iteração está apontando, e armazeno
        # de qual posição do vetor é o maior atualmente.
        maior = n[num]
        posicao_maior = f"n{num+1}"
    elif n[num] == maior:
        # Caso houver um empate entre 2 posições do vetor, primeiramente crio
        # uma variável temporária para iterar novamente entre todo o vetor e
        # retornar o maior número dele, para então descobrir se esse empate
        # é entre os maiores números ou não
        maiortemp = 0
        for i in range(3):
            if n[i] > maiortemp:
                maiortemp = n[i]
        # Caso o número retornado da segunda iteração seja igual ao que gerou
        # o empate, significa que o empate realmente é entre os maiores então
        # armazeno a posição do vetor do que gerou o empate na variável "empate"
        if maiortemp == n[num]:
            empate = f"n{num+1}"

# Se a variável "empate" não for mais any, significa que um empate aconteceu,
# então imprimo para o usuário quais posições empataram e quais foram seu valor
if empate != any:
    print(f"Os números {posicao_maior} e {empate} empataram sendo {maior}")
# Se minha variável "empate" continuar sem alteração, significa que
# não houve empate, então simplesmente imprimo o maior número e sua posição
else:
    print(f"O maior número foi o {posicao_maior} sendo {maior}")
