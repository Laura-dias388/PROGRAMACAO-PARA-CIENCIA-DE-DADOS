# 2: Calculadora básica
print("=#=" * 30)

resp = "SIM"

while resp == "SIM":
  calculator = int(input("Qual operação básica você deseja realizar: "
                        "Adição digite 1 //Subtração digite 2 //Divisão digite 3 //Multiplicação digite 4: "))

  number_one = int(input("Digite o primeiro número: "))
  number_two = int(input("Digite o segundo número: "))

  print("=#=" * 30)
  if (calculator == 1):
    print(f"Calculando adição: ")
    resultAd = number_one + number_two
    print(f"Resultado: ", resultAd)
    print("=#=" * 30)

  elif (calculator == 2):
    print(f"Calculando subtração: ")
    resultSub = number_one - number_two  
    print(f"Resultado: ", resultSub)
    print("=#=" * 30)

  elif (calculator == 3):
    print(f"Calculando divisão: ")
    resultDiv = number_one / number_two 
    print(f"Resultado: ", resultDiv)
    print("=#=" * 30)

  elif (calculator == 4):
    print(f"Calculando multiplicação: ")
    resultMult = number_one * number_two     
    print(f"Resultado: ", resultMult)
    print("=#=" * 30)
    
  resp = input("Se deseja cintinuar digite SIM! ou aperte 'F' para parar!")

  while resp != "SIM" and resp != "F":
    resp = input("Digite apenas SIM ou F: ")