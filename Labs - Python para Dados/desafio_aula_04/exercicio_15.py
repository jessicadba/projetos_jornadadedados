# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
# String inicial
texto = "jornada de dados"

# Criando o dicionário de frequência
frequencia = {}
for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

# Exibindo o dicionário de frequência
print("Frequência dos caracteres:")
for caractere, quantidade in frequencia.items():
    print(f"{caractere}: {quantidade}")
