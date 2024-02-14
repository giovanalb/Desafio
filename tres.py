import json

with open('C:/Users/Giovana/Downloads/Projeto/dados/dados 1.json') as file:
    dados_faturamento = json.load(file)

faturamento_diario = [dia['valor'] for dia in dados_faturamento]

faturamento_diario_completo = [faturamento for faturamento in faturamento_diario if faturamento > 0]

menor_faturamento = min(faturamento_diario_completo)
maior_faturamento = max(faturamento_diario_completo)

media_mensal = sum(faturamento_diario_completo) / len(faturamento_diario_completo)

dias_acima_da_media = sum(1 for faturamento in faturamento_diario if faturamento > media_mensal)

print(f"Menor valor de faturamento diário: R${round(menor_faturamento, 2)}")
print(f"Maior valor de faturamento diário: R${round(maior_faturamento, 2)}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")