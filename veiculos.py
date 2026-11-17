#Faça um algoritmo para criar um lista de nomes de carros até que o usuário queira encerrar o mesmo e mostre a lista para o usuário em tempo real. Utilize vetor e uma estrutura de repetição.

carros = []
while True:
    nome = input("Digite o nome de um carro (ou 'sair'para encerrar): ")
    carros.append(nome)
    print(f"Lista atual de carros: {carros}\n")
    if nome.lower() == 'sair':
        break
    
print(f"Lista de carros: {carros}")   
