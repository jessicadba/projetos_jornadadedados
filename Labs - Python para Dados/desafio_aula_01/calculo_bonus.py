nome = input("Informe o seu nome: ")
salario = float(input("Informe o valor do seu salário bruto: "))
bonus = float(input("Informe o valor do bônus recebido: "))
#CONSTANTE_BONUS = salario * 4.5

valor_bonus = salario * (bonus / 100)
#valor_bonus = CONSTANTE_BONUS

print(f"{nome}, o valor do seu bônus será de: {valor_bonus:.2f}")
