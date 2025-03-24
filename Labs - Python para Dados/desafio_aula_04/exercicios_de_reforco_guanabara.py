# Variáveis compostas: tuple(), list[] e dict{}
# Dentro de coleções e de tuplas, pode-se utilizar o método len() é uma referência a length, que é comprimento.

# tuple -  uma variável que guarda vários valores. As tuplas são IMUTÁVEIS!!! Ou seja, você NÃO consegue alterar as variáveis de uma tupla em tempo de execução.

# Forma simples, sem precisar mostrar a posição dos elementos de detro da tupla
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'eu vou comer{comida} ')

print('Comi pra caramba!')

# Outra forma utilizando range, função muito útil para gerar uma sequência se precisar da posição do elemento dentro da tupla.
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim', 'batata frita')
for cont in range(0, len(lanche)): #o método len() é uma referência a length, que é comprimento.
    print(f'eu vou comer {lanche[cont]} na posição {cont}')

print('Comi pra caramba!')

# Outra forma utilizando o enumerate para mostrar a posição do elemento
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}') 

print('Comi pra caramba!')

# Organizar em ordem alfabética utilizando o método sorted
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
print(sorted(lanche))

# fateamento:
#print(lanche[2]) - pizza
#print(lanche[0:2]) - hamburguer e suco (desconsidera o último elemento)
#print(lanche[1:]) - suco, pizza e pudim
#print(lanche[1:3]) - suco e pizza (desconsidera o último elemento)
#print(lanche[-1]) - pudim (vai do ultimo ao primeiro elemento, ex: -2 pizza, -3 suco, -4 hamburguer)
#print(len(lanche)) - 4


# list - Tanto as tuplas quanto as listas guardam vários valores, mas diferentemente das tuplas, as listas são mutávies em tempo de execução.
# Toda lista é entre [] colchetes
lanche = ['hamburguer', 'suco', 'pizza', 'pudim', 'batata frita', 'cachorro-quente']

lanche.append('refrigerante') #adiciona o elemento no final da lista.
print(lanche)

lanche.insert(0, 'misto quente') # adiciona o elemento em uma determinada posição
print(lanche)

lanche[4] = 'picolé'
print(lanche)

del lanche[4] # exclui elementos da lista.
print(lanche)

lanche.pop(0) # normalmente utilizado para eliminar o último elemento, mas pode-se passa o parâmetro do elemento a ser excluído.
print(lanche)

lanche.remove('suco') # você não indica o índíce, mas sim, o conteúdo a ser excluído da lista.
print(lanche)


#valores = [3,7,9,5,4,8]
#valores.sort()
#valores.sort(reverse=True)
#print(valores)
#print(f'Essa lista tem {len(valores)} elementos. ')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

# dict
# Todo dicionário é entre {} chaves


