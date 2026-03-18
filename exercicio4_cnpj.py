# 4: Cálculo do dígito verificador do CNPJ

print("=#=" * 30)
resp = "SIM"

while resp == "SIM":
  cnpj = input("\033[34mDigite seu CNPJ:\033[0m ")

  print("=#=" * 30)
  if len(cnpj) != 14 or not cnpj.isdigit():
      print("O cnpj precisa ter 14 dígitos e aceita apenas números!!")

  elif len(cnpj) == 14:

      print("CNPJ correto!")
      for i in cnpj:
        print(i, end="")
    
      

  resp = input("Se deseja cintinuar digite SIM! ou aperte 'F' para parar!")

  while resp != "SIM" and resp != "F":
    resp = input("Digite apenas SIM ou F: ")