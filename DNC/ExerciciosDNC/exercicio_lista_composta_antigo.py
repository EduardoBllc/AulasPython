clientes = []
usuario = []
while True:
    usuario.append(input('Digite o nome: '))
    usuario.append(input('Digite o email: '))
    usuario.append(input('Digite o telefone: '))
    usuario.append(input('Digite a idade: '))
    clientes.append(usuario[:])
    usuario.clear()
    resp = input('Deseja continuar? [S/N]: ')
    if resp.upper() == 'N':
        break
print(clientes)


def achar():
    email = input('Digite o email do usuário para verificar o perfil: ')
    cliente_encontrado = None
    for cliente in clientes:
        if email == cliente[1]:  # Verifica o email na posição 1 da sublista
            cliente_encontrado = cliente
            break
    if cliente_encontrado is not None:
        print('Informações do cliente encontrado:', cliente_encontrado)
    else:
        print('O email não foi encontrado na lista.')
        achar()


achar()
