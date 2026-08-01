def calcular_suedo(horas,precio):
    resultado= horas*precio
    return resultado


x = float(input("Cuantas horas trabajas: "))
y = float(input("Cuanto te pagan:"))

result=calcular_suedo(x,y)
print(result)