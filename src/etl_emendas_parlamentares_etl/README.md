# etl_emendas_parlamentares_etl (Pipeline DLT)

Esta pasta contém o código-fonte da pipeline Delta Live Tables (DLT) / Lakeflow de Emendas Parlamentares:

- `transformations/`: Definições de tabelas e transformações do pipeline (Bronze → Silver → Gold).
- `explorations/`: Notebooks para análise exploratória dos dados.

## Estrutura de Transformações

As transformações utilizam a API declarativa de pipelines do PySpark (`pyspark.pipelines` / `dlt`):

* `transformations/bronze_emendas.py`: Ingestão dos CSVs do Volume para tabelas Delta na camada Bronze (`bronze_emendas_parlamentares`, `bronze_emendas_convenios`, `bronze_emendas_favorecidos`).

## Execução

Pelo Databricks CLI:
```bash
databricks bundle run etl_emendas_parlamentares_etl --profile DATALAKE_EXs
```

