# Segundo examen parcial
import csv 
import pandas as pd

# =============================================================================
# SECCION 1: EJERCICIOS PARA RESOLVER EN CLASE
# =============================================================================
print("\n\n=== EJERCICIOS ===\n")

# EJERCICIO 1: Guardar numeros en archivo
# Crea una funcion llamada "guardar_numeros" que reciba una lista de numeros
# y el nombre de un archivo.
# La funcion debe guardar cada numero en una linea del archivo.
# Pruebala con la lista [10, 20, 30, 40] y el archivo "numeros.txt"

# TU CODIGO AQUI:

def guardar_numeros(numeros, nombre_archivo):
    with open(nombre_archivo, "w") as f:
        for num in numeros:
            f.write(f"{num}\n")

#prueba de la funcion:
guardar_numeros([10, 20, 30, 40], "numeros.txt")

# EJERCICIO 2: Leer numeros desde archivo
# Crea una funcion llamada "leer_numeros" que reciba el nombre de un archivo.
# La funcion debe leer los numeros del archivo y devolverlos en una lista de enteros.
# Luego calcula e imprime el promedio de los numeros leidos de "numeros.txt"

# TU CODIGO AQUI:

def leer_numeros(nombre_archivo):
    numeros = []
    with open(nombre_archivo, "r") as f:
        for linea in f:
            numeros.append(int(linea.strip()))
    return numeros

numeros = leer_numeros("numeros.txt")

promedio = sum(numeros) / len(numeros)
print(f"Promedio: {promedio}")


# EJERCICIO 3: Filtrar mayores
# Crea una funcion llamada "filtrar_mayores" que reciba una lista y un limite.
# La funcion debe devolver una nueva lista con los numeros mayores al limite.
# Pruebala con la lista leida del archivo y con limite = 25

# TU CODIGO AQUI:

def filtrar_mayores(lista, limite):
    mayores = []
    for num in lista:
        if num > limite:
            mayores.append(num)
    return mayores

numeros_mayores = filtrar_mayores(numeros, 25)
print(f"Numeros mayores a 25: {numeros_mayores}")


# EJERCICIO 4: Crear CSV de estudiantes
# Crea una funcion llamada "crear_csv_estudiantes" que reciba el nombre de un archivo.
# La funcion debe crear un archivo CSV con columnas:
# nombre,edad,calificacion
# Agrega al menos 5 estudiantes inventados.

# TU CODIGO AQUI:

def crear_csv_estudiantes(nombre_archivo):
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 85},
        {"nombre": "Luis", "edad": 22, "calificacion": 78},
        {"nombre": "Maria", "edad": 19, "calificacion": 92},
        {"nombre": "Carlos", "edad": 23, "calificacion": 65},
        {"nombre": "Sofia", "edad": 21, "calificacion": 88}
    ]
    with open(nombre_archivo, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["nombre", "edad", "calificacion"])
        writer.writeheader()
        writer.writerows(estudiantes)

crear_csv_estudiantes("estudiantes.csv")


# EJERCICIO 5: Analisis manual de CSV
# Sin usar pandas, lee el archivo de estudiantes y calcula:
# - el promedio de calificaciones
# - cuantos estudiantes tienen edad mayor a 21

# TU CODIGO AQUI:

def analizar_estudiantes_manual(nombre_archivo):
    total_calificacion = 0
    total_estudiantes = 0
    mayores_21 = 0
    
    with open(nombre_archivo, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_calificacion += int(row["calificacion"])
            
            if int(row["edad"]) > 21:
                mayores_21 += 1

            total_estudiantes += 1
    
    if total_estudiantes > 0:
        promedio_calificacion = total_calificacion / total_estudiantes
    else:
        promedio_calificacion = 0

    print(f"Promedio de calificaciones: {promedio_calificacion}")
    print(f"Estudiantes con edad mayor a 21: {mayores_21}") 

analizar_estudiantes_manual("estudiantes.csv")

# EJERCICIO 6: Funcion de analisis de estudiantes
# Crea una funcion llamada "analizar_estudiantes" que reciba el nombre de un archivo CSV
# y devuelva un diccionario con:
# - promedio_calificacion
# - max_calificacion
# - min_calificacion
# - total_estudiantes

# TU CODIGO AQUI:

def analizar_estudiantes(nombre_archivo):
    total_calificacion = 0
    total_estudiantes = 0
    max_calificacion = float("-inf")
    min_calificacion = float("inf")
    
    with open(nombre_archivo, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            calificacion = int(row["calificacion"])
            total_calificacion += calificacion
            total_estudiantes += 1
            if calificacion > max_calificacion:
                max_calificacion = calificacion
            if calificacion < min_calificacion:
                min_calificacion = calificacion
    
    promedio_calificacion = total_calificacion / total_estudiantes if total_estudiantes > 0 else 0
    return {
        "promedio_calificacion": promedio_calificacion,
        "max_calificacion": max_calificacion,
        "min_calificacion": min_calificacion,
        "total_estudiantes": total_estudiantes
    }

resultado = analizar_estudiantes("estudiantes.csv")
print(resultado)


# EJERCICIO 7: Cargar CSV con pandas
# Carga el archivo de estudiantes con pandas.
# Muestra:
# - los estudiantes con calificacion menor a 80
# - el DataFrame ordenado por edad de mayor a menor

# TU CODIGO AQUI:

df_estudiantes = pd.read_csv("estudiantes.csv")
estudiantes_menor_80 = df_estudiantes[df_estudiantes["calificacion"] < 80]
print("Estudiantes con calificacion menor a 80:")
print(estudiantes_menor_80)
df_ordenado = df_estudiantes.sort_values(by="edad", ascending=False)
print("DataFrame ordenado por edad de mayor a menor:")
print(df_ordenado)


# EJERCICIO 8: Nueva columna de estatus
# Usando pandas y el DataFrame de estudiantes,
# agrega una columna llamada "estatus":
# - "Aprobado" si la calificacion es mayor o igual a 70
# - "Reprobado" si la calificacion es menor a 70
# Muestra el DataFrame resultante.

# TU CODIGO AQUI:

df_estudiantes["estatus"] = df_estudiantes["calificacion"].apply(
    lambda calificacion: "Aprobado" if calificacion >= 70 else "Reprobado"
)

print("Lista de estudiantes con su estatus:")
print(df_estudiantes)

# EJERCICIO 9: CSV de ventas
# Crea un archivo CSV llamado "ventas.csv" con columnas:
# producto,categoria,precio
# Agrega al menos 5 productos inventados de distintas categorias.
# Luego cargalo con pandas y calcula el precio promedio por categoria.

# TU CODIGO AQUI:

def crear_csv_ventas(nombre_archivo):
    ventas = [
        {"producto": "Laptop", "categoria": "Electrónica", "precio": 1200},
        {"producto": "Silla", "categoria": "Muebles", "precio": 150},
        {"producto": "Smartphone", "categoria": "Electrónica", "precio": 800},
        {"producto": "Mesa", "categoria": "Muebles", "precio": 300},
        {"producto": "Audífonos", "categoria": "Electrónica", "precio": 200}
    ]
    with open(nombre_archivo, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["producto", "categoria", "precio"])
        writer.writeheader()
        writer.writerows(ventas)
        
crear_csv_ventas("ventas.csv")
df_ventas = pd.read_csv("ventas.csv")
precio_promedio_categoria = df_ventas.groupby("categoria")["precio"].mean()
print("Precio promedio por categoria:")
print(precio_promedio_categoria)


# EJERCICIO 10: Analisis de experimentos
# Crea un archivo CSV llamado "experimentos.csv" con columnas:
# experimento,medicion
# Agrega 5 experimentos inventados.
# Luego cargalo con pandas y calcula:
# - la media de las mediciones
# - la desviacion estandar
# - cuales mediciones son mayores a media + desviacion estandar

# TU CODIGO AQUI:

def crear_csv_experimentos(nombre_archivo):
    datos = [
        {"experimento": "Exp1", "medicion": 5.2},
        {"experimento": "Exp2", "medicion": 7.8},
        {"experimento": "Exp3", "medicion": 6.4},
        {"experimento": "Exp4", "medicion": 8.1},
        {"experimento": "Exp5", "medicion": 4.9}
    ]

    with open(nombre_archivo, "w", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["experimento", "medicion"])
        writer.writeheader()
        writer.writerows(datos)

crear_csv_experimentos("experimentos.csv")

datos = pd.read_csv("experimentos.csv")

promedio = datos["medicion"].mean()
desviacion = datos["medicion"].std()

limite = promedio + desviacion

altos = datos[datos["medicion"] > limite]

print("Promedio:", promedio)
print("Desviación estándar:", desviacion)
print("Valores altos:")
print(altos)

