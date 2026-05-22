import pandas as pd
import numpy as np
from scipy import stats

#=====================================
# VALIDACION DE NULOS
#=====================================

def validar_nulos(df):

    print("Cantidad de valores nulos por columna:\n")
    print(df.isnull().sum())

#=====================================
# RESUMEN ESTADISTICO
#=====================================

def resumen_estadistico(df):

    print("\nResumen estadistico del dataset:\n")
    display(df.describe())

#=====================================
# NORMALIZACION DE COLUMNAS
#=====================================

def normalizar_columnas(df):

    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )

    return df

#=====================================
# DETECCION DE OUTLIERS (SCIPY)
#=====================================

def detectar_outliers(columna):

    z_scores = stats.zscore(columna.dropna())

    outliers = abs(z_scores) > 3

    return outliers.sum()