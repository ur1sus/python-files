produtos = []
def mostrar_menu():
    print("\n1 - Cadastrar Produto")
    print("2 - Consultar Produto por ID")
    print("s - Sair do Programa")

def cadastrar_produto():
    id = int(input("\nDigite o ID o produto: "))
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: \n"))
    produto = {
        "id":id, 
        "nome":nome,
        "preco": preco
    }
    produtos.append(produto)

def busca_id(id):
    for prouto in produtos:
        if produto["id"] == id:
            print("\nProduto encontrado")
            print(produto)
        else:
            print("\nProduto não encontrado")
