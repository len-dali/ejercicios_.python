#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

minutos = int(input('Ingresa la cantidad de minutos:'))

res_horas = int(minutos/60)
res_min = int(minutos%60)

print (res_horas, "horas y ",res_min, "minutos.")
