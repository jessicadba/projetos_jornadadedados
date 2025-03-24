# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
# Lista de valores inicial
valores = [10, 15, 20, 25, 30, 35, 40]

# Dividindo em duas listas: pares e ímpares
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

# Exibindo os resultados
print("Valores pares:", pares)
print("Valores ímpares:", impares)