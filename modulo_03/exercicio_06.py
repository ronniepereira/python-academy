salario_atual = float(input("Digite seu salário atual: "))
porcentagem_aumento = float(input("Digite a porcentagem de aumento: "))

salario_novo = salario_atual + (salario_atual * porcentagem_aumento / 100)

print(f"Parabéns, seu novo salário é de: R${salario_novo}")
