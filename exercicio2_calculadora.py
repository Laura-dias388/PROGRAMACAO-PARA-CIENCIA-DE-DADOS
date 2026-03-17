# 1: Calculadora básica
print("=#=" * 30)
calculator = int(input("Qual operação básica você deseja realizar: "
                        "Adição digite 1 //Subtração digite 2 //Divisão digite 3 //Multiplicação digite 4: "))

number_one = int(input("Digite o primeiro número: "))
number_two = int(input("Digite o segundo número: "))

print("=#=" * 30)
if (calculator == 1):
  print(f"Calculando adição: ")
  resultAd = number_one + number_two
  print(f"Resultado: ", resultAd)

elif (calculator == 2):
  print(f"Calculando subtração: ")
  resultSub = number_one - number_two  
  print(f"Resultado: ", resultSub)

elif (calculator == 3):
  print(f"Calculando divisão: ")
  resultDiv = number_one / number_two 
  print(f"Resultado: ", resultDiv)

elif (calculator == 4):
  print(f"Calculando multiplicação: ")
  resultMult = number_one * number_two     
  print(f"Resultado: ", resultMult)
