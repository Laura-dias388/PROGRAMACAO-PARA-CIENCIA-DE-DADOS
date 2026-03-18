# 5: Sistema de menu de usuários

usuarios = []

while True:
    print("MENU:")
    print("1 - Incluir usuário")
    print("2 - Excluir usuário")
    print("3 - Consultar usuário")
    print("4 - Alterar usuário")
    print("5 - Listar todos os usuários")
    print("9 - Sair")
    
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        usuarios.append(nome)
        print(f"Usuário '{nome}' incluído com sucesso.")
        print("=#=" * 30)

    elif opcao == "2":
        nome = input("Digite o nome do usuário a ser excluído: ")
        if nome in usuarios:
            usuarios.remove(nome)
            print(f"Usuário '{nome}' excluído com sucesso.")
        else:
            print(f"Usuário '{nome}' não encontrado.")
        print("=#=" * 30)

    elif opcao == "3":
        nome = input("Digite o nome do usuário a ser consultado: ")
        if nome in usuarios:
            print(f"Usuário '{nome}' encontrado.")
        else:
            print(f"Usuário '{nome}' não encontrado.")
        print("=#=" * 30)

    elif opcao == "4":
        nome_antigo = input("Digite o nome do usuário a ser alterado: ")
        if nome_antigo in usuarios:
            indice = usuarios.index(nome_antigo)
            novo_nome = input("Digite o novo nome: ")
            usuarios[indice] = novo_nome
            print(f"Usuário '{nome_antigo}' alterado para '{novo_nome}'.")
        else:
            print(f"Usuário '{nome_antigo}' não encontrado.")
        print("=#=" * 30)

    elif opcao == "5":
        if len(usuarios) == 0:
            print("Não há usuários cadastrados.")
        else:
            print("Usuários cadastrados:")
            for nome in usuarios:
                print(f"- {nome}")
                print("=#=" * 30)
                
    elif opcao == "9":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")