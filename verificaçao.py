idade = int(input("Digite uma idade: "))
match idade: 
    case idade if idade > 0 and idade <= 4:
      print ("Essa pessoa é um bebê")
    case idade if idade > 5 and idade <= 9:
      print ("Essa pessoa é uma criança")
    case idade if idade > 10 and idade <= 17:
      print ("Essa pessoa é um adolescente")
    case idade if idade >= 18:
      print ("Essa pessoa é um adulto")
    case _: 
        print("Idade não pode ser negativo")
