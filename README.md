# Projeto de Análise de Emendas Parlamentares (ETL no Databricks)

Este projeto tem como objetivo processar e analisar dados de Emendas Parlamentares através de um pipeline de ETL moderno na plataforma Databricks. A solução utiliza a Arquitetura Medalhão (Medallion Architecture) para estruturar os dados e o Databricks Genie para a criação de painéis e consultas em linguagem natural.

## 🎯 Objetivo

Construir um fluxo de ingestão, transformação e agregação (ETL) dos dados de Emendas Parlamentares. Os dados brutos são recebidos em formato CSV, refinados ao longo de camadas estruturadas em formato Delta (Bronze, Silver e Gold) utilizando o Unity Catalog, e finalmente disponibilizados na camada Gold. A camada Gold servirá como base de conhecimento estruturada para o **Databricks Genie**, onde usuários finais poderão gerar dashboards e fazer perguntas de negócio utilizando linguagem natural.

## 🏗️ Arquitetura de Dados (Medalhão)

- **Raw (Volumes do Unity Catalog):** Área de pouso (Landing Zone) onde os arquivos originais (.csv) são ingeridos e armazenados sem nenhuma modificação.
- **Camada Bronze:** Ingestão dos dados brutos do Volume para Tabelas Delta. Os dados mantêm sua estrutura original (as-is), ganhando performance e versionamento.
- **Camada Silver:** Limpeza, padronização de tipos de dados, tratamentos de nulos, deduplicação e cruzamento (join) de informações (ex: Emendas com Convênios e Favorecidos).
- **Camada Gold:** Dados agregados e modelados para o negócio, prontos para consumo por ferramentas de BI e pelo **Databricks Genie** para relatórios gerenciais e análises interativas.

## ⚙️ Stack Tecnológica

- **Linguagem:** Python 3.x (PySpark e Databricks SDK)
- **Plataforma de Dados:** Databricks
- **Governança e Armazenamento:** Unity Catalog (Volumes e Delta Tables)
- **Visualização e BI:** Databricks Genie

## 📂 Estrutura do Projeto

```
projeto/
├── databricks.yml                  # Configuração do Databricks Bundle (DAB)
├── pyproject.toml                  # Dependências e configuração do pacote Python
├── notebooks/
│   ├── projeto_inicial.ipynb       # Notebook de setup (catálogo, schemas, upload de CSVs)
│   └── sample_notebook.ipynb       # Notebook de exemplo do bundle
├── src/
│   ├── etl_emendas_parlamentares/  # Pacote Python (job de ingestão Bronze)
│   │   ├── main.py                 # Ponto de entrada do job
│   │   └── emendas.py              # Funções de leitura dos CSVs do Volume
│   └── etl_emendas_parlamentares_etl/  # Pipeline Lakeflow (transformações DLT)
│       └── transformations/        # Transformações Bronze → Silver → Gold
├── resources/                      # Definições de jobs e pipelines do bundle
├── database/                       # Arquivos CSV brutos (não rastreado pelo Git)
├── tests/                          # Testes automatizados
├── fixtures/                       # Dados de teste
├── .env                            # Variáveis de ambiente (não rastreado pelo Git)
└── .gitignore                      # Regras de arquivos ignorados pelo Git
```

## 🚀 Como Executar

1. Criar e ativar o ambiente virtual: `python -m venv .venv` e `.venv\Scripts\activate`
2. Instalar as dependências do projeto: `pip install databricks-sdk`
3. Configurar o profile do Databricks CLI (`databricks configure --profile DATALAKE_EXs`)
4. Executar o notebook `notebooks/projeto_inicial.ipynb` para provisionar catálogo, schemas e volumes
5. Fazer upload dos CSVs da pasta `database/` para o Volume no Databricks
6. Validar o bundle: `databricks bundle validate --profile DATALAKE_EXs`
7. Fazer deploy: `databricks bundle deploy --profile DATALAKE_EXs`
