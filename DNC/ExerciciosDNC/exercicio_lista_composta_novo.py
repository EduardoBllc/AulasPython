# Criando as listas que irão armazenar os dados dos clientes
clientes = []
usuario = []
while True:
    mensagens = ("o nome", "o email", "o telefone", "a idade")
    # Para cada mensagem, pedirá para o usuário inserir uma informação
    for mensagem in mensagens:
        usuario.append(input(f'Digite {mensagem}: '))
    # Adiciona o registro de usuário completo à lista de clientes e depois limpa o registro
    # para começar um novo
    clientes.append(usuario[:])
    usuario.clear()
    # Checando se o usuário quer adicionar mais algum registro
    if input('Deseja continuar? [S/N]: ').upper() == 'N':
        break

# Criando a função que irá checar e imprimir os dados do email consultado
def achar():
    # Recebendo o email
    email = input('Digite o email do usuário para verificar o perfil: ')
    # Checando se o email existe em uma lista com todos os emails da lista clientes
    if email in [cliente[1] for cliente in clientes]:
        # Exibindo o resultado
        print(f"Informações do cliente encontrado: "
              f"{[cliente[0] for cliente in clientes if cliente[1] == email]}")
    else:
        # Informando que não existe o email consultado na lista e fazendo uma chamada recursiva
        print('O email não foi encontrado na lista.')
        achar()


achar()
