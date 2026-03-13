# 1: Cálculo de desconto

value_account = int(input(f"Qual o valor da conta: "))
value_discount = int(input(f"Qual o valor do desconto a ser aplicado: "))

new_value = value_account * (value_discount / 100)
result_value = value_account - new_value

print(f"O valor digitado com desconto é:", result_value)