import os
import pandas as pd
import numpy as np

def carregar_precipitacao_anual(db_path):
    """
    Carrega todos os arquivos CSV da pasta db_path, processa os dados de precipitação anual,
    descartando valores nulos, -9999, negativos ou absurdos (>500mm/hora).
    Retorna um DataFrame com colunas: 'ano', 'precipitacao_total'.
    """
    # Listar todos os arquivos CSV na pasta (ordenar por ano)
    csv_files = sorted([
        f for f in os.listdir(db_path) if f.endswith('.CSV')
    ])
    def extrair_ano(arquivo):
        return int(arquivo.split('_')[-3].split('-')[-1])
    dados_anuais = {}
    for file in csv_files:
        ano = extrair_ano(file)
        file_path = os.path.join(db_path, file)
        df = pd.read_csv(
            file_path,
            sep=';',
            skiprows=8,
            usecols=['DATA', 'PRECIPITACAO TOTAL'],
            encoding='latin1',
            dtype=str
        )
        df = df.rename(columns={
            'DATA': 'data',
            'PRECIPITACAO TOTAL': 'precipitacao'
        })
        df['precipitacao'] = (
            df['precipitacao']
            .replace('-9999', np.nan)
            .str.replace(',', '.', regex=False)
            .astype(float)
        )
        df = df.dropna(subset=['precipitacao'])
        df = df[(df['precipitacao'] >= 0) & (df['precipitacao'] < 500)]
        soma_diaria = df.groupby('data')['precipitacao'].sum()
        total_anual = soma_diaria.sum()
        dados_anuais[ano] = total_anual
    anos = sorted(dados_anuais.keys())
    valores = [dados_anuais[a] for a in anos]
    df_anos = pd.DataFrame({'ano': anos, 'precipitacao_total': valores})
    return df_anos 

def carregar_precipitacao_mensal(db_path):
    """
    Carrega todos os arquivos CSV da pasta db_path, processa os dados de precipitação mensal,
    descartando valores nulos, -9999, negativos ou absurdos (>500mm/hora).
    Retorna um DataFrame com colunas: 'ano', 'mes', 'precipitacao_total'.
    """
    csv_files = sorted([
        f for f in os.listdir(db_path) if f.endswith('.CSV')
    ])
    def extrair_ano(arquivo):
        return int(arquivo.split('_')[-3].split('-')[-1])
    lista_registros = []
    for file in csv_files:
        ano = extrair_ano(file)
        file_path = os.path.join(db_path, file)
        df = pd.read_csv(
            file_path,
            sep=';',
            skiprows=8,
            usecols=['DATA', 'PRECIPITACAO TOTAL'],
            encoding='latin1',
            dtype=str
        )
        df = df.rename(columns={
            'DATA': 'data',
            'PRECIPITACAO TOTAL': 'precipitacao'
        })
        df['precipitacao'] = (
            df['precipitacao']
            .replace('-9999', np.nan)
            .str.replace(',', '.', regex=False)
            .astype(float)
        )
        df = df.dropna(subset=['precipitacao'])
        df = df[(df['precipitacao'] >= 0) & (df['precipitacao'] < 500)]
        df['ano'] = df['data'].str[:4].astype(int)
        df['mes'] = df['data'].str[5:7].astype(int)
        soma_mensal = df.groupby(['ano', 'mes'])['precipitacao'].sum().reset_index()
        lista_registros.append(soma_mensal)
    df_meses = pd.concat(lista_registros, ignore_index=True)
    df_meses = df_meses.groupby(['ano', 'mes'])['precipitacao'].sum().reset_index()
    df_meses = df_meses.rename(columns={'precipitacao': 'precipitacao_total'})
    return df_meses 