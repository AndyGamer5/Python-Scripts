import numpy as np
import pandas as pd

# 1. Generar un conjunto de datos de ingresos
# Supongamos que queremos simular los ingresos anuales de 1000 personas
# usando una distribución normal (media: 50,000, desviación estándar: 15,000)

np.random.seed(42)  # Fijar la semilla para resultados reproducibles
ingresos = np.random.normal(50000, 15000, 1000)

# imprime los ingresos
print(ingresos)

# 2. Crear un DataFrame con Pandas
df = pd.DataFrame({
    'Ingresos': ingresos
})

# 3. Guardar el DataFrame en un archivo CSV
df.to_csv('ingresos_simulados.csv', index=False)  # Guardar sin incluir el índice
print("Archivo 'ingresos_simulados.csv' generado con los datos de ingresos.")

# 2. Calcular estadísticas básicas
media_ingresos = np.mean(ingresos)
mediana_ingresos = np.median(ingresos)
desviacion_ingresos = np.std(ingresos)
max_ingreso = np.max(ingresos)
min_ingreso = np.min(ingresos)

# 3. Contar cuántas personas ganan más de 50,000
personas_mayor_50000 = np.sum(ingresos > 50000)

# 4. Mostrar resultados
print("Estadísticas de los ingresos simulados:")
print(f"Media de ingresos: ${media_ingresos:,.2f}")
print(f"Mediana de ingresos: ${mediana_ingresos:,.2f}")
print(f"Desviación estándar de ingresos: ${desviacion_ingresos:,.2f}")
print(f"Ingreso más alto: ${max_ingreso:,.2f}")
print(f"Ingreso más bajo: ${min_ingreso:,.2f}")
print(f"Número de personas que ganan más de $50,000: {personas_mayor_50000}")