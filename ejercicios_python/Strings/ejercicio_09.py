#Realizar un programa que compruebe si una cadena contiene una subcadena.

cad = input("Introduce una cadena: ")
subcad = input("Introduce una subcadena: ")

indicador = False

num_subcadenas = len(cad) - len(subcad) + 1

for nsubc in range(num_subcadenas):
    if cad[nsubc:nsubc + len(subcad)] == subcad:
        indicador = True

if indicador:
    print("La cadena contiene la subcadena.")
else:
    print("La cadena no contiene la subcadena.")