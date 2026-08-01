import pandas as pd

def analizar_cotizaciones(ruta_archivo):
    """
    Lee un archivo CSV de cotizaciones y calcula estadísticas básicas.
    
    Parameters:
    ruta_archivo (str): Ruta al archivo CSV de cotizaciones.
    
    Returns:
    pandas.DataFrame: DataFrame con el mínimo, máximo y media de cada columna numérica.
    """
    # Leer el archivo CSV con punto y coma como separador
    df = pd.read_csv(ruta_archivo, sep=';', decimal=',')
    
    # Identificar las columnas numéricas (excluyendo cualquier no numérica)
    columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Calcular estadísticas
    estadisticas = pd.DataFrame({
        'Mínimo': df[columnas_numericas].min(),
        'Máximo': df[columnas_numericas].max(),
        'Media': df[columnas_numericas].mean()
    })
    
    return estadisticas

# Llamada a la función
ruta_archivo = 'cotizacion.csv'
estadisticas = analizar_cotizaciones(ruta_archivo)
print(estadisticas)
