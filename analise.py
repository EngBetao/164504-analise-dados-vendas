import pandas as pd
import matplotlib.pyplot as plt

# 1. DADOS (Simulação)
dados = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Vendas': [12000, 15000, 11000, 16000, 19000, 22000, 21000, 25000, 23000, 28000, 35000, 42000],
    'Custos': [8000, 9000, 8500, 9500, 10000, 11000, 12000, 13000, 12500, 14000, 18000, 20000]
}

df = pd.DataFrame(dados)

# 2. CÁLCULOS
faturamento_total = df['Vendas'].sum()
lucro_total = (df['Vendas'] - df['Custos']).sum()
mes_recorde = df.loc[df['Vendas'].idxmax()]

print(f"--- RELATÓRIO DE PERFORMANCE 2024 ---")
print(f"💰 Faturamento Anual: R$ {faturamento_total:,.2f}")
print(f"🏆 Melhor Mês: {mes_recorde['Mês']} com R$ {mes_recorde['Vendas']:,.2f}")

# 3. GRÁFICO
plt.figure(figsize=(10, 6))
plt.bar(df['Mês'], df['Vendas'], color='green', label='Vendas')
plt.plot(df['Mês'], df['Custos'], color='red', marker='o', label='Custos')
plt.title('Evolução de Vendas 2024')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('grafico_vendas.png') # Salva o gráfico como imagem
print("✅ Gráfico salvo como 'grafico_vendas.png