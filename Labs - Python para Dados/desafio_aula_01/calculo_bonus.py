# Definindo as variáveis para a inserção de dados
nome = input("Informe o seu nome: ")
salario = float(input("Informe o valor do seu salário bruto: "))
bonus = float(input("Informe o valor do bônus recebido: "))
#CONSTANTE_BONUS = salario * 4.5
# Uma constante é uma variável cujo valor não deve ser alterado após ser definido. As constantes em python, são definidas com LETRAS MAIÚSCULAS.
# Se o bônus for um valor fixo, ou seja, que não irá mudar, pode-se definir a CONSTANTE_BONUS acima.
 

# Calculando o valor do bônus
# Aqui pode-se alterar a regra de cálculo do bônus, de acordo com as regras de negócio da empresa.
valor_bonus = salario * (bonus / 100) # ajustado para calcular em porcentagem.
#valor_bonus = CONSTANTE_BONUS


# Exibindo o resultado. 
# O "f" f-strings permite colocar texto e as variáveis juntas, {}
# (:.2f) para formatar o resultado com duas casas decimais, tornando o valor mais legível.
print(f"{nome}, o valor do seu bônus será de: {valor_bonus:.2f}")


