import json

with open('faturamento.json') as file:
    data = json.load(file)

menor_faturamento = float('inf')
maior_faturamento = float('-inf')
soma_faturamento = 0
dias_com_faturamento = 0
dias_acima_da_media = 0

for dia in data:
    if dia['valor'] > 0:
        if dia['valor'] < menor_faturamento:
            menor_faturamento = dia['valor']
        if dia['valor'] > maior_faturamento:
            maior_faturamento = dia['valor']
        soma_faturamento += dia['valor']
        dias_com_faturamento += 1

media_mensal = soma_faturamento / dias_com_faturamento

for dia in data:
    if dia['valor'] > media_mensal:
        dias_acima_da_media += 1

print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

print("Fim do cálculo de faturamento.")
