clientes = []
usuario = []
while True:
    mensagens = ("o nome", "o email", "o telefone", "a idade")
    for mensagem in mensagens:
        usuario.append(input(f'Digite {mensagem}: '))
    clientes.append(usuario[:])
    usuario.clear()
    if input('Deseja continuar? [S/N]: ').upper() == 'N':
        break


def achar():
    email = input('Digite o email do usuário para verificar o perfil: ')
    if email in [cliente[1] for cliente in clientes]:
        print(f"Informações do cliente encontrado: "
              f"{[cliente[0] for cliente in clientes if cliente[1] == email]}")
    else:
        print('O email não foi encontrado na lista.')
        achar()


achar()
