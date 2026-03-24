#Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

cad = input("Introduce una cadena: ")
newcad = ""

for posicion in range(len(cad)):
    letra = cad[posicion]
    
    if letra == letra.upper():
        newcad = newcad + letra.lower()
        
    elif letra == letra.lower():
        newcad = newcad + letra.upper()

print("La cadena convertida es:", newcad)
