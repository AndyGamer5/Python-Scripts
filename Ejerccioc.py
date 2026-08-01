import re

cadena = input("Ingrese una cadena: ")
if re.match(r"ab*", cadena):
  print("La cadena coincide con el patrón.")
else:
  print("La cadena no coincide con el patrón.")