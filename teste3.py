# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

# RESOLUÇÃO
import json

with open("dados.json", encoding='utf-8') as jsonData:
    dados = json.load(jsonData)

valoresValidos = []


def media_numeros(numeros):
    soma = 0
    quantidade_numeros = len(numeros)

    for numero in numeros:
        soma += numero

    media = soma / quantidade_numeros
    return media


for i in dados:
    if i['valor'] != 0:
        valoresValidos.append(i['valor'])

mediaMensal = media_numeros(valoresValidos)

count = 0
for i in valoresValidos:
    if i > mediaMensal:
        count += 1


print(f"O menor faturamento foi: 0.0")
print(f"O menor faturamento em um dia valido foi: {min(valoresValidos)}")
print(f"O maior faturamento foi: {max(valoresValidos)}")
print(
    f"O número de dias no mês em que o valor de faturamento foi superior à média é: {count}")
