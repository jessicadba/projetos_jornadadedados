#Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# Lista inicial de idades
idades = [12, 18, 24, 16, 30, 14, 22]

# Filtrando idades maiores ou iguais a 18
idades_filtradas = [idade for idade in idades if idade >= 18]

# Exibindo as idades filtradas
print("Idades maiores ou iguais a 18:", idades_filtradas)