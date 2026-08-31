from pyspark import pipelines as dp


@dp.table(
    comment="Tabela Bronze - Convênios de Emendas Parlamentares (dados brutos do CSV)"
)
def bronze_emendas_convenios():
    """Ingestão do CSV EmendasParlamentares_Convenios.csv para tabela Delta."""
    return (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .option("delimiter", ";")
        .csv("/Volumes/datalake_emendas/bronze/raw/EmendasParlamentares_Convenios.csv")
    )


@dp.table(
    comment="Tabela Bronze - Favorecidos de Emendas Parlamentares (dados brutos do CSV)"
)
def bronze_emendas_favorecidos():
    """Ingestão do CSV EmendasParlamentares_PorFavorecido.csv para tabela Delta."""
    return (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .option("delimiter", ";")
        .csv("/Volumes/datalake_emendas/bronze/raw/EmendasParlamentares_PorFavorecido.csv")
    )
