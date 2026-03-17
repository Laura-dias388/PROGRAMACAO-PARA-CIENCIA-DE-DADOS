# 1: Cálculo do dígito verificador do CPF

print("=#=" * 30)

cpf = input("\033[34mDigite seu CPF:\033[0m ")

print("=#=" * 30)
if len(cpf) != 11 or not cpf.isdigit():
    print("O cpf precisa ter onze caracteres e ser números!!")

elif len(cpf) == 11:

    print("CPF correto!")
    for i in cpf:
      print(i, end="")
  
print("=#=" * 30)