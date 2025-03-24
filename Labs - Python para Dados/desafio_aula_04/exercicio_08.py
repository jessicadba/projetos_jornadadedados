#Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# Lista de dicionários representando pessoas
pessoas = [
    {"nome": "Luciano", "idade": 28},
    {"nome": "Diego", "idade": 22},
    {"nome": "Jessica", "idade": 35}
]

# Ordenando a lista pelo campo 'nome'
pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa["nome"])

# Exibindo a lista ordenada
for pessoa in pessoas_ordenadas:
    print(pessoa)