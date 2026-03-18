# 3: Cálculo do dígito verificador do CPF

print("=#=" * 30)
resp = "SIM"

while resp == "SIM":
  cpf = input("\033[34mDigite seu CPF:\033[0m ")

  print("=#=" * 30)
  if len(cpf) != 11 or not cpf.isdigit():
      print("O cpf precisa ter 11 dígitos e aceita apenas números!!")

  elif len(cpf) == 11:

      print("CPF correto!")
      for i in cpf:
        print(i, end="")
    
 
  resp = input("Se deseja cintinuar digite SIM! ou aperte 'F' para parar!")

  while resp != "SIM" and resp != "F":
    resp = input("Digite apenas SIM ou F: ")