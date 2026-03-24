'''
Strings con Python

'''

name = "Francisco"
profession = "Master"

Greetings = "Hello I'm Lendali"
print(Greetings)
Translate = '"Hello" es "Hola"'
print(Translate)

#Escapar Caracteres con \
#Cambiar el sentido del caracter

Greetings = 'Hello I \´m Francisco'
print(Greetings)

menu = 'Elige una opcion:\n1.- Op1\n2.- Op2'
print(menu)

#String Format
message1 = "Hello I'm and I´m ".format(name, profession)
#f string
message2 = f"Hello I´m {name} and I´m {profession}" 
print(message2)

#Metodos para Strings

movie = "Volver al futuro"
print(movie.upper())
print(movie.lower())
print(movie.capitalize())
print(movie.title())
print(movie.split(" "))
print(movie.startswith("V"))
print(movie. endswith("V"))
print('a' in movie)

