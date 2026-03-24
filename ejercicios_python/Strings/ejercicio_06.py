#Realizar un programa que dada una cadena de caracteres por caracteres, genere otra cadena resultado de invertir la primera.

cad = input('Introduce una cadena: ')
invertida = ""
for car in range (len(cad) -1, -1, -1):
    invertida=invertida + cad[car]

print('La cadena invertida es:', invertida)