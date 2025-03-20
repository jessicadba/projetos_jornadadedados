# Solicita ao usuário que digite seu nome
try:
    nome = input("Digite seu nome: ").strip()
    if len(nome) == 0:
        print("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in nome):
        print("O nome não deve conter números.")
    else:
        print("Nome válido:", nome)

        # Solicita ao usuário que digite o valor do seu salário
        salario_input = input("Digite o valor do seu salário: ")
        if salario_input.replace('.', '', 1).isdigit():  # Valida se é um número
            salario = float(salario_input)
            if salario < 0:
                print("Por favor, digite um valor positivo para o salário.")
            else:
                # Solicita ao usuário que digite o valor do bônus recebido
                bonus_input = input("Digite o valor do bônus recebido: ")
                if bonus_input.replace('.', '', 1).isdigit():  # Valida se é um número
                    bonus_recebido = float(bonus_input)
                    if bonus_recebido < 0:
                        print("Por favor, digite um valor positivo para o bônus.")
                    else:
                        # Calcula o bônus final e o KPI
                        bonus_final = bonus_recebido * 1.2  # Exemplo, ajuste conforme necessário
                        kpi = (salario + bonus_final) / 1000  # Exemplo simples de KPI

                        # Exibe os resultados ao usuário
                        print(f"Seu KPI é: {kpi:.2f}")
                        print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")
                else:
                    print("Entrada inválida para o bônus. Por favor, digite um número válido.")
        else:
            print("Entrada inválida para o salário. Por favor, digite um número válido.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
