import random

while True:
    dim_linha = int(input("Digite a dim da linha: "))
    dim_coluna = int(input("Digite a dim da coluna: "))
    matriz = [[random.randint(1, 10) for coluna in range (dim_coluna)] for linha in range(dim_linha)]
    for linha in range(dim_linha):
        for coluna in range(dim_coluna): 
            print(matriz[linha][coluna], end=" ")
        print()
    continua = input("Deseja continuar?[s, n]: ").lower()
    if continua == "n":

matriz = [[random.randint(1, 10) for coluna in range(3)] for linha in range(3)]
imprime_matriz(matriz)

opcao = int(input("\nDeseja 0, 1 ou 2 para somar uma linha especifica: "))
soma = 0
match opcao:
    case 0:
        linha = matriz [0]
        for elemento in linha:
            soma += elemento
        print(f"A Soma da linha 0 é:  {soma}")
    case 1:
        linha = matriz [1]
        for elemento in linha:
            soma += elemento
        print(f"A Soma da linha 1 é:  {soma}")
    case 2:
        linha = matriz [2]
        for elemento in linha:
            soma += elemento
        print(f"A Soma da linha 2 é:  {soma}")
    case _:
        print("Opção inválida. Digite 0, 1 ou 2.")
    
