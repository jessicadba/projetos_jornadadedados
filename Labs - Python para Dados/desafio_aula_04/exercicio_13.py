# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
# Dicionário de estoque de produtos
estoque = {
    "Notebook": 10,
    "Celular": 0,
    "Monitor": 5,
    "Teclado": 0,
    "Mouse": 8
}

# Filtrando produtos com quantidade maior que 0
produtos_disponiveis = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

# Exibindo os produtos disponíveis
print("Produtos disponíveis:", produtos_disponiveis)