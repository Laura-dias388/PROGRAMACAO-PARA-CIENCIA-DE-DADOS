# 5: Sistema de menu de usuários

users = []

while True:
    print("MENU:")
    print("1 - Incluir usuário")
    print("2 - Excluir usuário")
    print("3 - Consultar usuário")
    print("4 - Alterar usuário")
    print("5 - Listar todos os usuários")
    print("9 - Sair")
    
    option = input("Digite a opção desejada: ")
    if option == "1":
        name = input("Digite o nome do usuário: ")
        users.append(name)
        print(f"Usuário '{name}' incluído com sucesso.")
        print("=#=" * 30)

    elif option == "2":
        name = input("Digite o nome do usuário a ser excluído: ")
        if name in users:
            users.remove(name)
            print(f"Usuário '{name}' excluído com sucesso.")
        else:
            print(f"Usuário '{name}' não encontrado.")
        print("=#=" * 30)

    elif option == "3":
        name = input("Digite o nome do usuário a ser consultado: ")
        if name in users:
            print(f"Usuário '{name}' encontrado.")
        else:
            print(f"Usuário '{name}' não encontrado.")
        print("=#=" * 30)

    elif option == "4":
        old_name = input("Digite o nome do usuário a ser alterado: ")
        if old_name in users:
            index = users.index(old_name)
            updated_name = input("Digite o novo nome: ")
            users[index] = updated_name
            print(f"Usuário '{old_name}' alterado para '{updated_name}'.")
        else:
            print(f"Usuário '{old_name}' não encontrado.")
        print("=#=" * 30)

    elif option == "5":
        if len(users) == 0:
            print("Não há usuários cadastrados.")
        else:
            print("Usuários cadastrados:")
            for name in users:
                print("=#=" * 30)
                print(f"- {name}")
                print("=#=" * 30)
                
    elif option == "9":
        print("Você clicou 9 para sair...")
        break
    else:
        print("Opção inválida. Tente novamente.")