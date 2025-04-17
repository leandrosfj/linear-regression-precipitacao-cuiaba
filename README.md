# linear-regression-precipitacao-cuiaba

Este projeto tem como objetivo realizar análises de dados de precipitação em Cuiabá utilizando técnicas de regressão linear e análise de séries temporais. O projeto foi desenvolvido como parte de um trabalho de métodos computacionais.

## Objetivos do Projeto

- Coletar e processar dados de precipitação de múltiplas fontes
- Realizar análises utilizando regressão linear e transformada de Fourier
- Gerar visualizações gráficas dos resultados
- Realizar análises descritivas dos dados
- Implementar análise deslizante dos dados (janelas móveis de 5 anos)

## Arquitetura do Projeto

```
linear-regression-precipitacao-cuiaba/
├── src/                            # Código-fonte principal
│   ├── db/                         # Armazenamento dos dados brutos
│   ├── results/                    # Resultados das análises e gráficos
│   ├── load_precipitacao.py        # Script para carregar dados
│   ├── analise_precipitacao.py     # Implementação da análise de regressão
├── run_analise_precipitacao.py     # Script principal para executar a análise
├── requirements.txt                # Dependências do projeto
└── README.md                       # Documentação
```

## Tecnologias Utilizadas

- Python 3.x
- Bibliotecas Principais:
  - scikit-learn: Para implementação de modelos de regressão linear
  - numpy: Para manipulação de arrays e operações matemáticas
  - matplotlib: Para visualização de dados e geração de gráficos
  - pandas: Para manipulação e análise de dados

## Configuração do Ambiente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/linear-regression-precipitacao-cuiaba.git
cd linear-regression-precipitacao-cuiaba
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Funcionalidades Principais

### Carregamento de Dados
- Leitura de arquivos CSV contendo dados de precipitação
- Processamento e limpeza dos dados
- Combinação de múltiplas fontes de dados

### Análise de Dados
- Implementação de regressão linear
- Análise de séries temporais
- Cálculo de métricas de precisão
- Análise deslizante com janelas móveis

### Visualização
- Geração de gráficos de regressão
- Visualização de tendências temporais
- Exportação de resultados em formato PNG

## Executando o Projeto

1. . Execute a análise de regressão:
```bash
python run_analise_precipitacao.py
```

## Considerações Técnicas

- O projeto considera o zero como o número de casas decimais do erro (1 x 10^-n)
- Implementa análise deslizante dos dados com janelas de 5 anos
- Suporta análise de dados de múltiplos anos
- Gera visualizações gráficas para análise dos resultados

