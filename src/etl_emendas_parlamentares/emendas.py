"""Módulo para leitura e ingestão de dados de Emendas Parlamentares."""

from databricks.sdk.runtime import spark
from pyspark.sql import DataFrame


CATALOG = "datalake_emendas"
SCHEMA = "bronze"
VOLUME = "raw"
VOLUME_PATH = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}"


def ler_csv_do_volume(nome_arquivo: str) -> DataFrame:
    """Lê um arquivo CSV do Volume raw e retorna um DataFrame Spark.

    Args:
        nome_arquivo: Nome do arquivo CSV dentro do volume (ex: 'EmendasParlamentares.csv')

    Returns:
        DataFrame Spark com os dados brutos do CSV.
    """
    caminho = f"{VOLUME_PATH}/{nome_arquivo}"
    return (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .option("delimiter", ";")
        .csv(caminho)
    )


def ler_emendas() -> DataFrame:
    """Lê o arquivo EmendasParlamentares.csv do Volume."""
    return ler_csv_do_volume("EmendasParlamentares.csv")


def ler_convenios() -> DataFrame:
    """Lê o arquivo EmendasParlamentares_Convenios.csv do Volume."""
    return ler_csv_do_volume("EmendasParlamentares_Convenios.csv")


def ler_favorecidos() -> DataFrame:
    """Lê o arquivo EmendasParlamentares_PorFavorecido.csv do Volume."""
    return ler_csv_do_volume("EmendasParlamentares_PorFavorecido.csv")
