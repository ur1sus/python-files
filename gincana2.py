'''
2 - Crie um programa que receba 15 números aleatórios no 
intervalo entre 1 e 100 e armazene-os em uma lista.
Mostre:
A quantidade de pares
Mostre os pares em uma lista chamada lista_pares
Exemplo:
Saída:
Lista = [38, 24, 85, 44, 89, 98, 94, 16, 88, 35, 71, 63, 16, 29, 85]
Quantidade de pares = 8
Lista de pares = [38, 24, 44, 98, 94, 16, 88, 16]
'''
import random
lista = [random.randint(1, 100) for _ in range(15)]
lista_pares = [num for num in lista if num % 2 == 0]
quantidade_pares = len(lista_pares)
print(f"Lista normal = {lista}")
print(f"Quantidade de pares = {quantidade_pares}")
print(f"Lista de pares = {lista_pares}")

'''
import random
lista = [random.randint(1, 100) for tamanho in range (15)]
 
contador = 0
par = []

for numero in range(15):
    if lista[numero] % 2 == 0 


'''
