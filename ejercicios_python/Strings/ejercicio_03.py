#Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

frase = input('INGRESA UNA FRASE: ')

letra = input('INGRESA UNA LETRA: ')
while len(letra) != 1:
    letra = input('INGRESA UNA LETRA:')

count = 0
for i in frase:
    if i == letra:
        count += 1    

print(f"La letra '{letra}' esta '{count}' veces en '{frase}'")