# Solicita e valida o nome do usuário
while True:
    nome = input("Informe o seu nome: ").strip()  # Remove espaços desnecessários
    if nome.isdigit() or not nome:  # Verifica se o nome contém apenas números ou está vazio
        print("Erro: Por favor, insira um nome válido (não numérico e não vazio).")
    else:
        break  # Nome válido, sai do loop

# Solicita e valida o valor do salário
while True:
    try:
        salario = float(input("Informe o valor do seu salário bruto: "))
        if salario < 0:
            print("Erro: O salário não pode ser negativo. Tente novamente.")
        else:
            break  # Salário válido, sai do loop
    except ValueError:
        print("Erro: Entrada inválida. Digite um número válido.")

# Solicita e valida o percentual de bônus
while True:
    try:
        bonus = float(input("Informe o valor do bônus recebido (em %): "))
        if bonus < 0:
            print("Erro: O bônus não pode ser negativo. Tente novamente.")
        else:
            break  # Percentual válido, sai do loop
    except ValueError:
        print("Erro: Entrada inválida. Digite um número válido.")

# Calcula o valor do bônus
valor_bonus = salario * (bonus / 100)

# Exibe o resultado final
print(f"{nome}, o valor do seu bônus será de: {valor_bonus:.2f}")
