import admin


while True:
    print("\n=== ADMIN ===")
    print("1 - Ver produtos")
    print("2 - Verificar stock")
    print("3 - Alterar preço")
    print("4 - Remover produto")
    print("0 - Sair")

    opcao = input("Escolhe: ")

    if opcao == "1":
        print(admin.mostrar_produtos())

    elif opcao == "2":
        try:
            id_prod = int(input("ID do produto: "))
            print(admin.verificar_stock(id_prod))
        except ValueError:
            print("ID inválido.")

    elif opcao == "3":
        try:
            id_prod = int(input("ID do produto: "))
            preco = float(input("Novo preço: "))
            print(admin.alterar_precos(id_prod, preco))
        except ValueError:
            print("Valor inválido.")

    elif opcao == "4":
        try:
            id_prod = int(input("ID do produto: "))
            print(admin.remover_produto(id_prod))
        except ValueError:
            print("ID inválido.")

    elif opcao == "0":
        print("A sair do sistema...")
        break

    else:
        print("Opção inválida. Tenta novamente.")