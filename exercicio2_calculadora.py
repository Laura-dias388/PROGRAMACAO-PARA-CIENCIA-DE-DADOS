# 1: Calculadora básica

calculator = int(input(f"Qual operação básica você deseja realizar:",
                        "Para Adição digite 1 //Para Subtração digite 2 //Para Divisão digite 3 //Para Multiplicação digite 4"))

if (calculator == 1):
  print(f"Calculando adição:")
  number_one = int(input("Digite o primeiro número:"))
