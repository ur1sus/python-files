#Aula 3 e desafios
temperaturas = [22, 25, 21, 24, 26, 23, 22]
print(f"A lista tem {len(temperaturas)} valores")
print(temperaturas[0])
print(temperaturas[6])

#desafio 2
i = 0
while i < len(temperaturas):
    print(temperaturas[i])
    i += 1

#Desafio 3
soma = 0 
i = 0
while i < len(temperaturas):
    soma = soma + temperaturas[i]
    i += 1
print(f"Soma = {soma}")

#Desafio 4 
media = soma / len(temperaturas)
print(f"Média = {media}")

#Desafio 5
procurada = 27
encontrou = False
i = 0
while i < len(temperaturas):
    if temperaturas[i] == procurada:
        encontrou = True
        break
    i +=1
if encontrou == True:
    print(f"Encontrou a temperatura {procurada} na lista")
else:
    print("Não encontrou a temperatura")
