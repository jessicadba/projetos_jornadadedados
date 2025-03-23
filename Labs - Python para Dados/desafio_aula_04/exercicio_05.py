# Dados fornecidos
lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# Calculando o preço total
preco_total = sum(precos[item] for item in lista_compras)

print(f"O preço total da lista de compras é: R$ {preco_total:.2f}")