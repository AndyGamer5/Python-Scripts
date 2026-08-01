
cantidad = float(input("Ingresa una cantidad: "))

# Calcular porcentajes
diez_por_ciento = cantidad * 0.10
doce_por_ciento = cantidad * 0.12
IVA = cantidad * 0.16

# Sumar resultados
suma_total = diez_por_ciento + doce_por_ciento + IVA + cantidad
cantidad_sin_iva = diez_por_ciento + doce_por_ciento + cantidad

# Mostrar resultados
print("10%:", diez_por_ciento)
print("12%:", doce_por_ciento)
print("IVA (16%):", IVA)
print("Cantidad sin iva:", cantidad_sin_iva)
print("Suma total:", suma_total)
