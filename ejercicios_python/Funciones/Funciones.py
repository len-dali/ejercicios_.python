

[funcion(parametros)] -> valor de retorno

print (param1, param2, param3, ...)- > void
print("Hola", "Mundo," 35)

input(param1: string) - > string
name = input('Escribe tu nombre: ')

int(param1: string) - > int
num1 = int('1')

float(param1: string) - > float
num2 = float('3.5')

abs(num: int +/-) - > int +
num3 = abs(-10)



Funciones en python

def my_function(param1, param2, param3, ...):
	instrucciones
	return

my_function()	


#Funcion sin parametros y sin retornos

def say_hello():
	print('Hello!')

say_hello()	
print(say_hello)
print(type(say_hello))

#Funcion con parametros sin retorno
def say_hello_by_name(name):
	print ('Hola', name)

say_hello_by_name('Lendali')	
say_hello_by_name('Humans')
say_hello_by_name('Inges')

def tabla(num):
	print('Tabla del', num)
	print()
	for i in range(10):
		print(num, '*', (i+1), '=', (i+1) * num)

tabla(5)		
tabla(13)
tabla(7)

#Funciones con parametros y con retorno

def suma(num1, num2):
	return num1 + num2

result_suma = suma(23, 57)	
print(result_suma)

result_suma = suma(12, 5)
print(result_suma)

result_suma = suma(3, 25)

def iniciales(name, ape1, ape2):
	return name[0] + ape1[0] + ape2[0]

curp = iniciales('Lendali', 'Gasca', 'Cano')	
print(curp)

print(iniciales('Ariana', 'Trejo', 'Chivas'))


#Funciones con parametros nombrados
#Funciones con parametros posicionales
def super_heroe(name, hero):
	print(name, 'is', hero)

super_heroe('Tony Stark', 'Ironman')	
super_heroe('Peter Parker', 'Spiderman')
super_heroe('Batman', 'Bruce Wayne')
super_heroe(hero='Hulk', name='Bruce Banner')

print(iniciales(ape_1='Roggers', name='Steve', ape2='Chivas'))

#Funciones con parametros opcionales
