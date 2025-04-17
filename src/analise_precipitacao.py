import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from src.load_precipitacao import carregar_precipitacao_mensal

# Caminho da pasta com os arquivos CSV
db_path = 'src/db'

# Carregar dados mensais de precipitação já tratados
df_meses = carregar_precipitacao_mensal(db_path)
anos = sorted(df_meses['ano'].unique())
meses = range(1, 13)

# Análise deslizante de 5 anos para cada mês
resultados = []
plt.figure(figsize=(14, 8))
for mes in meses:
    dados_mes = df_meses[df_meses['mes'] == mes].sort_values('ano')
    if len(dados_mes) < 5:
        continue
    anos_mes = dados_mes['ano'].tolist()
    prec_mes = dados_mes['precipitacao_total'].tolist()
    for i in range(len(anos_mes) - 4):
        anos_janela = anos_mes[i:i+5]
        prec_janela = prec_mes[i:i+5]
        X = np.array(anos_janela).reshape(-1, 1)
        y = np.array(prec_janela)
        modelo = LinearRegression()
        modelo.fit(X, y)
        y_pred = modelo.predict(X)
        r2 = modelo.score(X, y)
        resultados.append({
            'mes': mes,
            'inicio': anos_janela[0],
            'fim': anos_janela[-1],
            'coef': modelo.coef_[0],
            'intercept': modelo.intercept_,
            'r2': r2
        })
    # Plotar série histórica mensal
    plt.plot(anos_mes, prec_mes, marker='o', label=f'Mês {mes:02d}')

plt.title('Precipitação Total Mensal - Cuiabá (Todos os anos)')
plt.xlabel('Ano')
plt.ylabel('Precipitação Total no mês (mm)')
plt.legend(title='Mês', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig('src/results/precipitacao_mensal_regressao.png')

# Geração do relatório descritivo mensal
with open('src/results/relatorio_precipitacao_mensal.txt', 'w', encoding='utf-8') as f:
    for res in resultados:
        f.write(f"Mês {res['mes']:02d} | Janela {res['inicio']} a {res['fim']}: ")
        f.write(f"Coef. angular: {res['coef']:.2f} mm/ano, ")
        f.write(f"Intercepto: {res['intercept']:.2f}, ")
        f.write(f"R²: {res['r2']:.4f}\n")
    
