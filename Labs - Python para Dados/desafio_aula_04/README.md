## Desafio Aula 04: Type hint, Tipos complexos (Dicionários vs DataFrames Vs Tabelas Vs Excel) e Funções
**Exercícios de Listas e Dicionários**

- Criar uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
- Dada a lista ["Python", "Java", "C++", "JavaScript"], remover o item "C++" e adicionar "Ruby".
- Criar um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
- Escrever um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
- Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcular o preço total da lista de compras.


## Entendento o desafio
*Python* utiliza tipagem dinâmica e por inferência. Isso significa que não precisa declarar explicitamente o tipo de uma variável ao defini-la, pois o *Python* identifica o tipo automaticamente em tempo de execução com base no valor atribuído. Por exemplo:

```python
x = 10       # Python sabe que 'x' é um inteiro
y = 3.14     # Python infere que 'y' é um float
z = "Spock"  # Python identifica que 'z' é uma string
```
Esse comportamento torna o Python mais simples e flexível de usar, mas também exige cuidado ao manipular os tipos das variáveis, especialmente em projetos grandes, para evitar erros.

### Type Hint
O conceito de Type Hint em Python é super útil para tornar o código mais legível e confiável, foi introduzido no Python a partir da versão 3.5 e as 
anotações de tipo têm sido aprimoradas nas versões subsequentes, tornando-se cada vez mais robustas e flexíveis. Por exemplo, a versão 3.9 introduziu tipos genéricos mais simples, como *list* e *dict* , sem a necessidade de importar do módulo *typing*.

Type Hint (ou "anotação de tipo") é uma maneira de indicar quais tipos de dados uma variável, função ou retorno devem ter. Ele não muda a funcionalidade do código em si (pois Python continua sendo dinâmico), mas serve como documentação e permite o uso de ferramentas estáticas, como linters ou IDEs, para ajudar a detectar possíveis erros antes de executar o código. Por exemplo:

```python
nome: str = "Jessica"
idade: int = 35
altura: float = 1.63
is_dba: boll = True
```

### Conceitos de Tipagem Forte e Tipagem Fraca
**Tipagem Forte** - 
Python é uma linguagem de tipagem forte, o que significa que ele não converte automaticamente tipos de dados em contextos onde eles não são compatíveis. Se você tentar somar um número com uma string, por exemplo, Python irá lançar um erro:
```python
x = 10
y = "20"
print(x + y)  # Vai gerar um TypeError

# Aqui, é preciso fazer a conversão explicitamente, como:
print(x + int(y))  # Resultado: 30
```
Python é forte porque respeita os tipos sem fazer conversões automáticas, mas é dinâmico porque permite flexibilidade na atribuição e alteração dos tipos das variáveis.

**Tipagem Fraca** - 
Linguagens de tipagem fraca *(como JavaScript)* permitem essas conversões automaticamente. No exemplo anterior, em JavaScript:

```javascript
let x = 10;
let y = "20";
console.log(x + y); // Resultado: "1020" (concatenação)
```

### Estrutura de listas em Python
As listas em Python são uma das estruturas de dados mais usadas por serem extremamente flexíveis e fáceis de trabalhar.
Uma lista é uma coleção ordenada e mutável de elementos, onde pode-se armazenar diferentes tipos de dados dentro de uma única lista, como inteiros, strings, floats, ou até outras listas. Elas são definidas usando colchetes [] e os elementos são separados por vírgulas.

```python
minha_lista = [1, 2, 3, "Spock", 4.5]
print(minha_lista)  # Saída: [1, 2, 3, 'Spock', 4.5]
```
**Pricipais características**
- *Indexação e ordenação -* Os elementos em uma lista são acessados através de índices, começando por 0 para o primeiro item. Exemplo:

```python
print(minha_lista[0])  # Saída: 1
print(minha_lista[3])  # Saída: 'Spock'
```
Pode-se acessar elementos a partir do final da lista, usando índices negativos.

```python
print(minha_lista[-1])  # Saída: 4.5 (último item)
```

- Mutabilidade - É possível alterar os elementos da lista após a sua criação.

```python
minha_lista[0] = 100
print(minha_lista)  # Saída: [100, 2, 3, 'Spock', 4.5]
```
Pode-se adicionar ou remover elementos livremente, sem precisar definir o tamanho da lista inicialmente.

### Principais métodos de listas em Python são: 
- append(): Adiciona um elemento ao final da lista.
```python
minha_lista.append(6)
print(minha_lista)  # Saída: [100, 2, 3, 'Spock', 4.5, 6]
```
- extend(): Adiciona elementos de outra lista ao final.
```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Usando extend()
lista1.extend(lista2)

print(lista1)  # Saída: [1, 2, 3, 4, 5, 6]
```
- insert(): Insere um elemento em uma posição específica.
```python
minha_lista.insert(1, "novo")
print(minha_lista)  # Saída: [100, 'novo', 2, 3, 'Spock', 4.5, 6]
```
- remove(): Remove o primeiro elemento igual ao valor especificado.
```python
minha_lista.remove(3)
print(minha_lista)  # Saída: [100, 'novo', 2, 'Spock', 4.5, 6]
```
- pop(): Remove e retorna o elemento de um índice específico (ou o último elemento, se o índice não for fornecido).
```python
ultimo = minha_lista.pop()
print(ultimo)       # Saída: 6
print(minha_lista)  # Saída: [100, 'novo', 2, 'Spock', 4.5]
```
- clear(): Remove todos os elementos da lista
```python
minha_lista = [1, 2, 3, 4, 5]
minha_lista.clear()
print(minha_lista)  # Saída: []
```
- index(): Retorna o índice do primeiro elemento igual ao valor especificado
```python
frutas = ["maçã", "banana", "laranja", "banana"]
indice = frutas.index("banana")
print(indice)  # Saída: 1 (posição da primeira ocorrência de "banana")
```
- count(): Conta quantas vezes um elemento aparece na lista
```python
numeros = [1, 2, 3, 2, 4, 2, 5]
quantidade = numeros.count(2)
print(quantidade)  # Saída: 3 (o número 2 aparece 3 vezes)
```
- sort(): Ordena os elementos da lista (apenas para elementos comparáveis, como números ou strings).
```python
numeros = [3, 1, 4, 2]
numeros.sort()
print(numeros)  # Saída: [1, 2, 3, 4]
```
- reverse(): Inverte a ordem dos elementos na lista
```python
numeros.reverse()
print(numeros)  # Saída: [4, 3, 2, 1]
```

### Estrutura de dicionários em Python
Dicionários armazenam pares chave-valor e são úteis para dados organizados em formato de "mapa" ou "tabela de busca", permitindo associar uma chave única a um valor correspondente.
Pode-se usar dicionários para representar dados estruturados, como um cadastro de clientes, um inventário de produtos ou mesmo configurações de sistemas.

**Principais características**:

- **Chaves únicas:** Cada chave em um dicionário deve ser única e imutável (pode ser uma string, número, tupla, etc.).
- **Valores variados:** Os valores podem ser de qualquer tipo, como números, strings, listas, outros dicionários, entre outros.
- **Desordenado:** Os itens não têm uma ordem fixa (a partir do Python 3.7, a ordem de inserção é mantida, mas não é garantida como regra fundamental).

```python
# Exemplo 1
aluno = {'nome': 'Carlos', 'idade': 22, 'curso': 'Engenharia'}
print(aluno['nome'])  # Saída = Carlos

# Exemplo 2
contato = {
    "nome": "Ana",
    "telefone": "1234-5678",
    "email": "ana@email.com"
}

# Acessando valores
print(contato["nome"])  # Ana
```

### Principais métodos de listas em Python são: 
- *get(chave)* - Retorna o valor associado à chave, ou *None* se não existir.
- *keys()* - Retorna as chaves.
- *values()* - Retorna os valores.
- *items()* - Retorna pares chave-valor como tuplas.
- *update(dicionario)* - Adiciona ou atualiza múltiplos pares chave-valor.

```python
produto.update({'marca': 'Samsung', 'cor': 'preto'})
print(produto)
```

### Principais diferenças entre Lista e Dicionário em Python
Tanto listas quanto dicionários são estruturas de dados fundamentais no Python, mas possuem diferenças importantes em sua organização e nos casos de uso. Busquei pesquisar mais afundo e encontrei essa tabela, que resume mais claramente estas diferenças:

| Aspecto            | Lista                           | Dicionário     |
|----------------    |----------------|----------------|
| **Estrutura**         | Coleção ordenada de elementos.   | Coleção desordenada de pares chave-valor.   |
| **Índice**            | Elementos acessados por índices numéricos (0, 1, 2, ...).                | Valores acessados por chaves únicas.          |
| **Mutabilidade**   | Mutável (pode adicionar/remover elementos).      | Mutável (pode adicionar/remover pares chave-valor).             |
| **Tipos de Dados** | Pode conter qualquer tipo de dado, inclusive misturados.  | As chaves devem ser imutáveis (ex.: strings, números); os valores podem variar.          |
| **Uso Comum**      | Para armazenar dados em sequência ou em lista.  | Para mapear ou relacionar dados, como um catálogo ou tabela.       |
| **Exemplo**        | ['maçã', 'banana', 'laranja']  | {''nome': 'Jessica', 'idade': 35, 'cidade': Rio de Janeiro}          |

- Listas são ideais para sequências ordenadas, como listas de itens ou filas.

```python
frutas = ['maçã', 'banana', 'laranja']
print(frutas[1])  # banana
```

- Dicionários são melhores para dados relacionais, como informações organizadas em formato de mapa ou tabela.

```python
aluno = {'nome': 'Jessica', 'idade': 35, 'cidade: Rio de Janeiro'}
print(aluno['cidade'])  # Rio de Janeiro
```