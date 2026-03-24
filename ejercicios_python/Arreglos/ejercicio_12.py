#Diseñar el algoritmo correspondiente a un programa, que:
#* Crea una tabla bidimensional de longitud 5x15 y nombre 'marco'.
#* Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
#* Visualiza el contenido de la matriz en pantalla.

num_filas = 5
num_cols = 15

matriz = []

for fila in range(num_filas):
    fila_datos = []
    for col in range(num_cols):
        if fila == 0 or fila == num_filas - 1 or col == 0 or col == num_cols - 1:
            fila_datos.append(1)
        else:
            fila_datos.append(0)
    matriz.append(fila_datos)

for fila in matriz:
    for valor in fila:
        print(valor, end=" ")
    print()