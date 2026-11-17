A = int(input("Digite um número A: "))
B = int(input("Digite um número B: "))
C = int(input("Digite um número C: "))
if (A > B) and (A > C):
    print(f"O {A} é o maior!")
elif (B > A) and (B > C):
    print(f"O {B} é o maior!")
elif (C > A) and (C > B): 
    print(f"O {C} é o maior!")
elif (A == B) and (A == C) and (B == C): 
    print(f"Os numeros {A}, {B}, {C} são iguais")
else:
    print(f"Algo deu errado!")
    
