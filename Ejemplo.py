''''''''''''''''''''''''''''
var_int = 9
var_float = 21.33
var_str = "putillo"
lista = [1,2,3,4,5,6]
presona = {
  "nombre": "emilio",
  "edad": 48,
  "estatura": 1.58,
  "color":["negro", "blanco"]
  }

print(var_int)
print(var_float)
print(var_str)
print(lista[1])
print(presona["color"])
'''''''''''''''''''''''''''''''''
libros=[]

for i in range(3):
    titulo= input("Dime el titulo pndj ")
    anio= int(input('Dame el anio de publicacion '))
    editorial=input('Escribe la editorial ')

    libro={
    titulo: titulo,
    anio: anio,
    editorial: editorial
    }
    libros.append(libro)

print(libros)