#Atividade "Notas da Turma", aula 4.
notas = [7.5, 8.0, 6.5, 9.3]
media = sum(notas) / len(notas)
print("Média: ", media)

quantidade = int(input("Quantas notas você vai digitar? "))

notas = []
for i in range(quantidade):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("Notas:", notas)
print("Média:", media)

notas = []
while True:
    entrada = input("Digite uma nota (ou 'fim' para parar): ").strip().lower()
    if entrada == "fim":
        break
    notas.append(float(entrada))

if len(notas) == 0:
    print("Nenhuma nota foi digitada.")
else: 
    media = sum(notas) / len(notas)
    print("Notas:", notas)
    print("Média:", media)
