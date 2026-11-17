def menu_escolha(escolha):
    match escolha:
        case "1":
            cadastrar_produto()
        case "2":
            id_produto = int(input("Digite o ID: "))
            busca_id(id_produto)
while True:
    mostrar_menu()
    escolha = input("\nDigite a escolha ou [s] para sair: ")
    menu_escolha(escolha)
    if escolha.lower() == "s":
        break
