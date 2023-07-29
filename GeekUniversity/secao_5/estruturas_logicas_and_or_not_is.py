"""
Estruturas Lógicas
and(e),or(ou),not(não),is(é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is
"""

logado = True
ativo = True

# or - Pelo menos uma das condições precisa coincidir
if logado or ativo:
    print("Parabéns, você possui uma conta!")
else:
    print("Talvez você não tenha uma conta...")

# and - As duas condições precisam coincidir
if logado and ativo:
    print("Bem vindo!")
else:
    print("Cheque sua caixa de email para ativar a conta!")

# not - Inverte o booleano

if not logado:
    print("Logue em sua conta!")

# is - Compara igualdades
if ativo is logado:
    print("Tá igual")
