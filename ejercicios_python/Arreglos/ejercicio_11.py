#/Diseñar el algoritmo correspondiente a un programa, que:
#* Crea una tabla bidimensional de longitud 5x5 y nombre 'diagonal'.
#* Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
#* Muestra el contenido de la tabla en pantalla.

num_filas = 5
num_cols = 5

matriz = []

for fila in range(num_filas):
    fila_datos = []
    for col in range(num_cols):
        if fila == col or fila == (num_filas - 1) - col:
            fila_datos.append(1)
        else:
            fila_datos.append(0)
    matriz.append(fila_datos)

for fila in range(num_filas):
    for col in range(num_cols):
        print(matriz[fila][col], end=" ")
    print()