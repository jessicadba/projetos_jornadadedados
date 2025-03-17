# Inserção de dados
nome = input("Informe o seu nome e sobrenome: ")
salario = int(input("Informe o valor do seu salário bruto: "))
bonus = float(input("Informe a porcentagem do bônus recebida: "))

# Calculando o valor do bônus
valor_bonus = salario * (bonus / 100)

# Exibindo o resultado
print(f"O valor do seu bônus é: {valor_bonus:.2f}")