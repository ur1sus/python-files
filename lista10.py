#Faça um algoritmo para criar um lista com 10 números inteiros aleatórios no intervalo de 1 a 100 e mostre para o usuário. Utilize o módulo random.

import random

numeros = [random.randint(1, 100) for i in range(10)]
print("Lista de números aleatórios ", numeros )
