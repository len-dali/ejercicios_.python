#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente.

base = int(input('Dime la base: '))
exponente = int(input('Dime el exponente: '))

if exponente > 0:
   resultado = base ** exponente

elif exponente == 0:
   resultado = 1

else: 
     resultado = 1 /(base ** (exponente))   

print(f'La potencia es: {resultado}')