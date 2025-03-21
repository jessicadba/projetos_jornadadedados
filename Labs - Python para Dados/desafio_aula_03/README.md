## Desafio Aula 03: Estruturas de Controle de Fluxo
Integrar na solução anterior um fluxo de While que repita o fluxo de execução até que o usuário insira as informações corretas.

### Entendento o desafio
As Estruturas de Controle de Fluxo em Python são responsáveis por controlar a sequência de execução de comandos no programa. Elas permitem que você tome decisões, repita ações ou manipule condições de forma dinâmica. 

### As Principais estruturas de controle Python são:
- **Condicional:** *if, elif, else* - 
Essas estruturas são usadas para tomar decisões com base em condições.
Exemplo:

```python
x = 10

if x > 0:
    print("Número positivo")
elif x == 0:
    print("Número é zero")
else:
    print("Número negativo")
```
*if* - Avalia a condição inicial.

*elif* - Avalia condições adicionais, caso o  seja falso.

*else* - Executa se nenhuma das condições anteriores for verdadeira.

- **Laço de Repetição:** *for* - é usado para iterar sobre sequências (como listas, strings, ranges)

```python
for i in range(5):
    print(i)  # Saída: 0, 1, 2, 3, 4

# Ele também funciona com outros iteráveis, como listas:
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta) # Saída: maçã, banana, laranja
```

- **Laço de Repetição:** *while* - executa um bloco de código enquanto uma condição for verdadeira.

```python
x = 0

while x < 5:
    print(x)
    x += 1  # Incremento para evitar loop infinito
```
É importante ter cuidado com loops infinitos, é necessário certificar que a condição do while eventualmente será falsa.

- **Controle de Fluxo Adicional:** 

*break* - Sai imediatamente do loop.

*continue* - Pula para a próxima iteração do loop, ignorando o restante do código.

```python
# exemplo break
for num in range(10):
    if num == 5:
        break
    print(num)  # Saída: 0, 1, 2, 3, 4

# exemplo continue
for num in range(5):
    if num == 3:
        continue
    print(num)  # Saída: 0, 1, 2, 4
```
 - **Controle com:** *pass* -  Ele não faz nada, mas evita erros de sintaxe.
Exemplo:

```python
for i in range(3):
    pass  # Código a ser implementado no futuro
```