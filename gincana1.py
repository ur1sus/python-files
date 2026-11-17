'''
1 - Crie um programa que receba 10 números aleatórios
inteiros no intervalo entre 1 e 100 e armazene-os em uma 
lista. Ao final, exiba:
A lista com os numeros
O maior número
O menor número
Exemplo:
Saída:
lista = 5 8 1 9 4 7 2 6 3 10
Maior = 10
Menor = 1
'''

import random 

lista = [random.randint(1, 10) for _ in range (10)]
maior = lista[0]
menor = lista[0]
for numero in lista:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("lista =", lista)
print("maior =", maior)
print("menor =", menor)
