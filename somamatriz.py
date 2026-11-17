

import random

def criar_matriz(linhas, colunas):  
     matriz = []
     for i in range (linhas):
         linha = []
         for i in range (colunas):
            linha.append(random.randint(1, 10))
     matriz.append(linha)
return matriz

def soma_matrizes (m1, m2, linhas, colunas):
    linhas = len(m1)
    colunas = len(m1[0])
    matriz_soma = []
    for i in range (linhas):
        linha = []
    for c in range(colunas):
            linha.append(m1[i][c] + m2[i][c])
    matriz_soma.append(linha)    
return matriz_soma

def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:<3}", end=" ")
        print()

linhas = 3
colunas = 3

matriz1 = criar_matriz(linhas, colunas)
matriz2 = criar_matriz(linhas, colunas)
matriz_resultado = somar_matrizes(matriz1, matriz2, linhas, colunas)

print("Matriz 1:")
imprimir_matriz(matriz1)

print("\nMatriz 2:")
exibir_matriz(matriz2)

print("\nMatriz resultados:")
exibir_matriz(matriz_resultado)

