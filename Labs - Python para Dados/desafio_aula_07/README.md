## Funções em Python
Funções em Python são blocos de código reutilizáveis que permitem organizar e simplificar o programa.
Para criar uma função em Python, utiliza-se a palavra-chave *def*, seguida de um nome para a função, parênteses () contendo zero ou mais "parâmetros", e dois pontos : e o output da função ->.

Exemplo:
```python
# Exemplo 01 Função
valor_1 = 4
valor_2 = 6

valor_4 = 3.5
valor_5 = 4.0

def soma(valor_1_para_somar: float, valor_2_para_somar: float) -> float:
    """
    Função de soma de valores do tipo float que retorna um valor float.
    """
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return resultado_da_soma

valor_3 = soma(valor_1_para_somar=valor_1, valor_2_para_somar=valor_2)
valor_6 = soma(valor_4, valor_5)

print(valor_3)
print(valor_6)
```

*Estudos em andamento, aos poucos irei atualizando a página com os exercícios.*