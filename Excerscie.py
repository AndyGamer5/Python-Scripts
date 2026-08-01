import numpy as np
# 1. Crear un array de números del 1 al 20
array = np.arange(1, 21)

# 2. Cambiar la forma a una matriz de 4x5
matriz = array.reshape(4, 5)
print("Matriz 4x5:")
print(matriz)

# 3. Estadísticas básicas
suma_total = np.sum(matriz)
media_valores = np.mean(matriz)
desviacion_estandar = np.std(matriz)

print("\nSuma total:", suma_total)
print("Media de los valores:", media_valores)
print("Desviación estándar:", desviacion_estandar)

# 4. Extraer una submatriz de los primeros dos elementos de las primeras dos filas
submatriz = matriz[:2, :2]
print("\nSubmatriz (2x2) de los primeros dos elementos:")
print(submatriz)

# 5. Multiplicar todos los elementos por 2
matriz_doble = matriz * 2
print("\nMatriz con elementos multiplicados por 2:")
print(matriz_doble)

# 6. Valor máximo y mínimo de la matriz
valor_maximo = np.max(matriz)
valor_minimo = np.min(matriz)

print("\nValor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)