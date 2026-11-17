def multiplicacao(numero1, numero2):
    return numero1 * numero2


def soma_lista(lista):
    soma = 0
    for pos in range(len(lista)):
        soma += lista[pos]
    return soma 

num1 = 10
num2 = 20
n1 = 30
resultado = multiplicacao(num1,num2)
print(f"{num1}*{num2} = {multiplicacao(num1, num2)}")



def divisao(numero1, numero2):
    return numero1/ numero2

num1 = 24
num2 = 2
resultado = divisao (num1, num2)
print(f"{num1}/{num2} = {divisao(num1, num2)}")
