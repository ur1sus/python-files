#Faça um algoritmo para organizar um fim de semana de uma pessoa. Ela deve escolher o dia passando um número inteiro por teclado e mostrar para o usuário o que ela escolheu. Se ela escolher um número fora do intervalo mostrar "Escolha inválida".
#Dia 1: Sexta-feira ir jogar bola
#Dia 2: Sábado ir ao cinema
#Dia 3: Domingo ir ao zoológico
#Dia 99: Escolha inválida
#Saída: 1
#Sexta-feira ir jogar bola

opcao = int(input("Digite o número do dia (1, 2, 3): "))
if opcao == 1:
    print("Jogar bola na sexta-feira.")
elif opcao == 2:  
    print("Ir ao cinema no sábado.")
elif opcao == 3:
    print("Ir ao Zoológico no domingo.")
else: 
    print("Escolha inválida.")
