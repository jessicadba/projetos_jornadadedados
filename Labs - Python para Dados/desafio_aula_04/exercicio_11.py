# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# Lista de dicionários representando produtos
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500.0},
    {"id": 2, "nome": "Celular", "preco": 1500.0},
    {"id": 3, "nome": "Monitor", "preco": 800.0}
]

# Produto que queremos atualizar (por exemplo, o produto com id 2)
id_produto_para_atualizar = 2
novo_preco = 1600.0

# Atualizando o preço do produto
for produto in produtos:
    if produto["id"] == id_produto_para_atualizar:
        produto["preco"] = novo_preco
        break  # Finaliza o loop após encontrar e atualizar

# Exibindo a lista atualizada de produtos
for produto in produtos:
    print(produto)