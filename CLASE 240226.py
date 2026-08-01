# Empaquetando la Logica en Funciones

# =============================================================================
# SECCION 1: EJEMPLOS
# =============================================================================

# --- Funciones Simples ---

# Ejemplo 1: Funcion sin parametros
def saludar():
    print("Hola, bienvenido!")

saludar()

# Ejemplo 2: Funcion con un parametro
def saludar_persona(nombre):
    print("Hola,", nombre)

saludar_persona("Ana")
saludar_persona("Juan")

# Ejemplo 3: Funcion con multiples parametros
def sumar(a, b):
    resultado = a + b
    print("La suma es:", resultado)

sumar(5, 3)
sumar(10, 20)

# --- Funciones con return ---

# Ejemplo 4: Funcion que devuelve un valor
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 5)
print("Resultado:", resultado)

# Ejemplo 5: Usar el valor retornado en operaciones
def elevar_cuadrado(numero):
    return numero ** 2

x = elevar_cuadrado(5)
y = elevar_cuadrado(3)
print("Suma de cuadrados:", x + y)

# Ejemplo 6: Diferencia entre print y return
def funcion_con_print(x):
    print(x * 2)

def funcion_con_return(x):
    return x * 2

a = funcion_con_print(5)  # Imprime 10
print("a es:", a)  # a es None

b = funcion_con_return(5)  # No imprime nada
print("b es:", b)  # b es 10

# --- Parametros por Defecto ---

# Ejemplo 7: Funcion con parametro por defecto
def saludar_con_estilo(nombre, saludo="Hola"):
    print(saludo, nombre)

saludar_con_estilo("Ana")
saludar_con_estilo("Juan", "Buenos dias")

# Ejemplo 8: Parametros por defecto en calculo
def calcular_precio(precio, descuento=0):
    precio_final = precio - (precio * descuento / 100)
    return precio_final

print(calcular_precio(100))
print(calcular_precio(100, 10))

# --- Scope de Variables ---

# Ejemplo 9: Variable local
def funcion_local():
    x = 10  # Variable local
    print("Dentro de la funcion:", x)

funcion_local()
# print(x)  # Esto causaria un error

# Ejemplo 10: Variable global
y = 20  # Variable global

def funcion_global():
    print("Dentro de la funcion:", y)

funcion_global()
print("Fuera de la funcion:", y)

# --- Funciones con Listas ---

# Ejemplo 11: Funcion que procesa una lista
def calcular_promedio(numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    return suma / cantidad

calificaciones = [85, 90, 78, 92, 88]
promedio = calcular_promedio(calificaciones)
print("Promedio:", promedio)

# Ejemplo 12: Funcion que encuentra el maximo
def encontrar_maximo(lista):
    if len(lista) == 0:
        return None
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

numeros = [45, 78, 23, 91, 56]
print("Maximo:", encontrar_maximo(numeros))

# Ejemplo 13: Funcion que filtra datos
def obtener_aprobados(calificaciones):
    aprobados = []
    for calif in calificaciones:
        if calif >= 70:
            aprobados.append(calif)
    return aprobados

notas = [85, 65, 90, 55, 78, 92]
print("Aprobados:", obtener_aprobados(notas))

# --- Funciones con Diccionarios ---

# Ejemplo 14: Funcion que procesa un diccionario
def mostrar_estudiante(estudiante):
    nombre = estudiante["nombre"]
    edad = estudiante["edad"]
    carrera = estudiante["carrera"]
    print(f"{nombre}, {edad} años, estudia {carrera}")

alumno = {"nombre": "Ana", "edad": 20, "carrera": "Biologia"}
mostrar_estudiante(alumno)

# Ejemplo 15: Funcion que devuelve un diccionario
def crear_perfil(nombre, edad, ciudad):
    perfil = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }
    return perfil

mi_perfil = crear_perfil("Juan", 22, "CDMX")
print(mi_perfil)

# Ejemplo 16: Funcion de analisis de datos
def analizar_experimento(datos):
    resultados = datos["resultados"]
    promedio = sum(resultados) / len(resultados)
    maximo = max(resultados)
    minimo = min(resultados)
    return {
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo
    }

experimento = {
    "nombre": "Medicion de pH",
    "resultados": [7.2, 7.5, 7.3, 7.4, 7.1]
}

estadisticas = analizar_experimento(experimento)
print("Estadisticas:", estadisticas)


# =============================================================================
# SECCION 2: EJERCICIOS PARA RESOLVER EN CLASE
# =============================================================================

print("\n\n=== EJERCICIOS ===\n")

print("\n\nEJERCICIO 1: Funcion de Bienvenida\n")
# Crea una funcion llamada "dar_bienvenida" que reciba un nombre
# y imprima "Bienvenido/a [nombre] al laboratorio"
# Llamala 2 veces con diferentes nombres

# TU CODIGO AQUI:
def dar_bienvenida (nombre):
    print("Bienvenido/a", nombre,"al laboratorio")

dar_bienvenida("Andres")
dar_bienvenida("Mariel")


print("\n\nEJERCICIO 2: Calculadora Simple\n")
# Crea una funcion llamada "restar" que reciba dos numeros
# y devuelva su resta
# Pruebala con los numeros 10 y 3

# TU CODIGO AQUI:

def restar(a, b):
    resta= a-b
    return resta

print(restar(10,3))

print("\n\nEJERCICIO 3: Convertidor de Temperatura\n")
# Crea una funcion "celsius_a_fahrenheit" que reciba una temperatura en Celsius
# y devuelva su equivalente en Fahrenheit
# Formula: F = (C * 9/5) + 32
# Pruebala con 25 grados Celsius

# TU CODIGO AQUI:

def celsius_a_fahrenheit(temp):
    f = (temp * 9/5) + 32
    return f

print(celsius_a_fahrenheit(25))



print("\nEJERCICIO 4: Verificador de Edad\n")
# Crea una funcion "es_mayor_edad" que reciba una edad
# y devuelva True si es >= 18, False si no
# Pruebala con las edades 15 y 20

# TU CODIGO AQUI:

def es_mayor_edad(edad):
    if edad >= 18:
        print(True)
    else:
        print(False)

es_mayor_edad(15)
es_mayor_edad(20)

print("\n\nEJERCICIO 5: Calculadora de Area\n")
# Crea una funcion "calcular_area_rectangulo" que reciba base y altura
# y devuelva el area (base * altura)
# Incluye un parametro por defecto altura=1
# Pruebala con (5, 3) y con (5)

# TU CODIGO AQUI:
def calcular_area_rectangulo(base, altura=1):
    area= (base*altura)
    return area

print(calcular_area_rectangulo(5 , 3))
print(calcular_area_rectangulo(5))


print("\n\nEJERCICIO 6: Contador de Pares\n")
# Crea una funcion "contar_pares" que reciba una lista de numeros
# y devuelva cuantos numeros pares hay
# Pruebala con la lista [1, 2, 3, 4, 5, 6, 7, 8]

# TU CODIGO AQUI:
def contar_pares(lista):
    contador = 0
    
    for i in lista:
        if i % 2 == 0:
            contador += 1  

    return contador 

resultado = contar_pares([1, 2, 3, 4, 5, 6, 7, 8])
print(resultado)

print("\n\nEJERCICIO 7: Buscar en Lista\n")
# Crea una funcion "esta_en_lista" que reciba una lista y un valor
# y devuelva True si el valor esta en la lista, False si no
# Pruebala buscando el numero 5 en [1, 3, 5, 7, 9]

# TU CODIGO AQUI:
def esta_en_lista(lista, valor):
    for i in lista:
        if i == valor:
            return True
    return False

resultado = esta_en_lista([1, 3, 5, 7, 9], 5)
print(resultado)

print("\n\nEJERCICIO 8: Suma de Lista\n")
# Crea una funcion "sumar_lista" que reciba una lista de numeros
# y devuelva la suma total (sin usar sum())
# Pruebala con [10, 20, 30, 40]

# TU CODIGO AQUI:
def sumar_lista(lista):
    total = 0 
    for i in lista:
        total += i
    return total

resultado=sumar_lista([10,20,30,40])
print(resultado)


print("\n\nEJERCICIO 9: Informacion de Producto\n")
# Crea una funcion "mostrar_producto" que reciba un diccionario con:
# - nombre, precio, stock
# Y que imprima: "[nombre] - $[precio] - Stock: [stock] unidades"
# Pruebala con un producto de tu eleccion

# TU CODIGO AQUI:
producto = {
    "nombre": "Laptop",
    "precio": 15000,
    "stock": 8
}

def mostrar_producto(diccionario):
    nombre = diccionario["nombre"]
    precio = diccionario["precio"]
    stock = diccionario["stock"]
    
    print(f"{nombre} - ${precio} - Stock: {stock} unidades")

mostrar_producto(producto)


print("\n\nEJERCICIO 10: Crear Reporte de Estudiante\n")
# Crea una funcion "generar_reporte" que reciba nombre, lista de calificaciones
# y devuelva un diccionario con:
# - nombre, promedio, aprobado (True si promedio >= 70)
# Pruebala con "Ana" y calificaciones [85, 90, 78]

# TU CODIGO AQUI:
def generar_reporte(nombre, lista):
    total = 0
    for i in lista:
        total += i
    
    promedio = total / len(lista)
    
    aprobado = promedio >= 70
    
    reporte = {
        "nombre": nombre,
        "promedio": promedio,
        "aprobado": aprobado
    }
    
    return reporte

resultado = generar_reporte("Ana", [85, 90, 78])
print(resultado)



# Fin de los ejercicios
print("\n\nExcelente! Has completado los ejercicios de la Sesion 4")
