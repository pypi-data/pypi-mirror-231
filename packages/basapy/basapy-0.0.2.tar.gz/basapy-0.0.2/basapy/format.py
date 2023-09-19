from pyspark.sql import DataFrame
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def format_decimal_separator(number: float) -> str:
    # Converte o número para string e substitui o ponto decimal por uma vírgula
    return str(number).replace('.', ',')

def remove_thousand_separator(number: str) -> str:
    # Remove separadores de milhar (pontos) se existirem
    return number.replace('.', '')

@udf(StringType())
def format_numeric(number: float) -> str:
    return remove_thousand_separator(format_decimal_separator(number))

def format_numeric_columns(df: DataFrame) -> DataFrame:
    # Lista de colunas numéricas
    num_columns = [col_name for col_name, col_type in df.dtypes if col_type in ['int', 'double', 'float']]
    
    for col in num_columns:
        df = df.withColumn(col, format_numeric(df[col]))
        
    return df
