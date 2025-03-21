## Desafio Aula 02: Refatorar o projeto da aula 01 evitando Bugs
Tratar os possíveis erros em Python (ou em qualquer linguagem de programação) é essencial para garantir que o programa funcione de forma robusta, confiável e amigável ao usuário. Os erros mais comuns encontrados durante a execução do código Python são: TypeError, Type Check e Type Conversion.

### Entendento o desafio
**TypeError** -
O TypeError é uma exceção que ocorre quando você tenta realizar uma operação ou função com um tipo de dado inadequado ou incompatível.

```python
# Exemplo de TypeError
resultado = "texto" + 5  # Erro: Não é possível somar string e inteiro
```

**Type Check** -
Verifica explicitamente o tipo de uma variável em Python. Embora Python seja uma linguagem de tipagem dinâmica, pode-se fazer verificações para garantir que as operações sejam realizadas com tipos corretos.

```python
# Verifica o tipo de uma variável
valor = 10
if isinstance(valor, int):  # Verifica se "valor" é inteiro
    print("Valor é um número inteiro.")
else:
    print("Valor não é um número inteiro.")
```
**Principais métodos:**
- type(objeto): Retorna o tipo de um objeto.
- isinstance(objeto, tipo): Verifica se o objeto é de um tipo específico.

**Type Conversion** -
Converte um valor de um tipo para outro. O Python oferece funções integradas para conversão de tipos, permitindo o ajuste dinamico dos tipos conforme necessário.

**Tipos de conversão:**

- Conversão implícita: Python realiza automaticamente entre tipos compatíveis.

```python
x = 5  # Inteiro
y = 2.5  # Float
z = x + y  # Aqui "x" é convertido implicitamente para float
print(z)  # Saída: 7.5
```
- Conversão explícita: Realizada manualmente pelo programador usando funções como int(), float(), str().

```python
# Conversão de string para inteiro
texto = "10"
numero = int(texto)  # Converte a string para inteiro
print(numero * 2)  # Saída: 20
```

### Funções comuns de conversão:
- int(): Converte para inteiro.
- float(): Converte para número de ponto flutuante.
- str(): Converte para string.
- list(), tuple(), set(): Convertem para os respectivos tipos de coleção.

## Principais motivos que destacam a importância do tratamento de erros:

### Evitar Interrupções Inesperadas:
- Sem o tratamento de erros, qualquer exceção não prevista pode fazer o programa parar abruptamente, causando uma má experiência para o usuário.
- O uso de blocos como try-except permite capturar e lidar com erros, mantendo o programa funcionando, mesmo diante de imprevistos.

### Melhorar a Experiência do Usuário:
- Fornecer mensagens claras e amigáveis ajuda o usuário a entender o que deu errado e como corrigir a entrada ou ação.
- Em vez de apresentar uma mensagem técnica, pode-se oferecer soluções práticas.

### Manutenção e Depuração Facilitadas:
- Com o tratamento de erros, é mais fácil identificar a origem de problemas durante o desenvolvimento ou a manutenção do código.
- Usar logs ou mensagens específicas em exceções ajuda a rastrear erros complexos.

### Prevenir Dados Corrompidos:
- Em sistemas que manipulam dados críticos (bancos de dados, arquivos, etc.), erros não tratados podem levar à corrupção ou perda de informações.
- Usar tratamento adequado garante que, mesmo em caso de erros, os dados sejam protegidos.

### Flexibilidade e Personalização:
Com o tratamento de erros, pode-se personalizar as respostas do programa a diferentes tipos de falhas, permitindo comportamentos alternativos ou a recuperação do sistema.

### Conclusão: 
O tratamento de erros torna o código mais resiliente, seguro e agradável de usar. Ele é fundamental para lidar com situações imprevistas e criar uma aplicação robusta e confiável.
