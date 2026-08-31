from pyspark import pipelines as dp


@dp.table(
    comment="Tabela Bronze - Emendas Parlamentares (dados brutos do CSV)"
)
def bronze_emendas_parlamentares():
    """Ingestão do CSV EmendasParlamentares.csv para tabela Delta."""
    return (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .option("delimiter", ";")
        .csv("/Volumes/datalake_emendas/bronze/raw/EmendasParlamentares.csv")
    )
