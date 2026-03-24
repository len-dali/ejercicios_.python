#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.

newcad =""
cad = input('Introduce una cadena: ')
while True:
    car_buscar = input('Introduce el caracter que deseas buscar: ')
    if len (car_buscar) == 1:
        break

while True:
    car_sustituir = input('Introduce un caracter para sustituir: ')
    if len (car_sustituir) == 1:
        break

for posicion in range (len(cad)):
    if cad[posicion] == car_buscar:
        newcad = newcad + car_sustituir
    else:
        newcad = newcad + cad[posicion]

print('La cadena modificada es:', newcad)


