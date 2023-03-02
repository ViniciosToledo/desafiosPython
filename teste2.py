#  2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
#     escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#  IMPORTANTE:
#  Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código


# RESOLUÇÃO
def verificaFibonacci(valor):
    a = 0
    b = 1
    proximoValor = 0

    while proximoValor < valor:
        proximoValor = a + b
        a = b
        b = proximoValor

    if proximoValor == valor:
        print('Pertence a sequência Fibonacci!')
    else:
        print('Não pertence a sequência Fibonacci!')


num = int(input('Digite um número: '))
print(verificaFibonacci(num))
