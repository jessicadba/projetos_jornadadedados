# Solicita uma string ao usuário
texto = input("Digite uma string: ")

# Inicializa o dicionário para armazenar as contagens
contagem_caracteres = {}

# Loop para contar as ocorrências de cada caractere
for caractere in texto:
    if caractere in contagem_caracteres:
        contagem_caracteres[caractere] += 1
    else:
        contagem_caracteres[caractere] = 1

# Exibe o resultado
print("Número de ocorrências de cada caractere:")
for caractere, ocorrencias in contagem_caracteres.items():
    print(f"{caractere}: {ocorrencias}")