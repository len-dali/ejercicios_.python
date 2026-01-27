# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados celcius
# Celcius

print('Conversión de Fahrenheit a Celsius')
fahrenheit = float(input('Ingresa los grados Fahrenheit: '))
celsius = (fahrenheit - 32) * (5/9)

print('Grados Fahrenheit', fahrenheit)
print('Grados Celsius', celsius)

print(f'{ fahrenheit }°F equivale a { celsius }°C')  