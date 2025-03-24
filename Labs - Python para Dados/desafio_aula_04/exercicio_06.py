# Objetivo: Dada uma lista de emails, remover todos os duplicados:
emails = [
    "exemplo1@email.com",
    "exemplo2@email.com",
    "exemplo1@email.com",
    "exemplo3@email.com"
]
# Removendo duplicados usando um conjunto (set)
emails_unicos = list(set(emails))

# Exibindo a lista sem duplicados
print("Emails únicos:", emails_unicos)

