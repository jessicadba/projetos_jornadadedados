## Desafio Aula 01: Cálculo de Bônus com Entrada do Usuário
Escrever um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

### Entendento o desafio
**Definição das variáveis para a inserção de dados:**

```PYTHON
nome = input("Informe o seu nome: ")
salario = float(input("Informe o valor do seu salário bruto: "))
bonus = float(input("Informe o valor do bônus recebido: "))
#CONSTANTE_BONUS = salario * 4.5
```
Uma constante é uma variável cujo valor não deve ser alterado após ser definido. As constantes em python, são definidas com LETRAS MAIÚSCULAS.
Se o bônus for um valor fixo, ou seja, que não irá mudar, pode-se definir a CONSTANTE_BONUS acima.

**Calculando o valor do bônus:**

Aqui pode-se alterar a regra de cálculo do bônus, de acordo com as regras de negócio da empresa. O código abaixo realiza o cálculo em porcentagem.
Como dito anteriormente, é possível definir uma constante onde o valor do bônus será fixo.

```PYTHON
valor_bonus = salario * (bonus / 100)
#valor_bonus = CONSTANTE_BONUS
```

**Exibindo o resultado:**

O *"f" f-strings* são uma forma mais eficiente e elegante de combinar texto com variáveis e expressões. Foram introduzidas no Python 3.6 e tornam o código mais legível e direto.

*(:.2f)* Ele é usado para formatar números com duas casas decimais, geralmente para valores de ponto flutuante (float). Abaixo explico melhor a sintaxe do seu funcionamento: 

- : – Introduz a parte de formatação.

- .2 – Define o número de casas decimais (neste caso, 2).

- f – Indica que o valor será formatado como um número de ponto flutuante

```PYTHON
print(f"{nome}, o valor do seu bônus será de: {valor_bonus:.2f}")
```
Explicar o código aqui foi a maneira que encontrei para consolidar meu aprendizado, e espero que isso ajude outras pessoas que, assim como eu, estão entrando nesse universo fantástico da Engenharia de Dados. Fiquem à vontade para enviar sugestões e melhorias. 😊