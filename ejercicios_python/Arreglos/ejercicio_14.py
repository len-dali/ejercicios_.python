# Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
#// * Las cantidades totales de cada articulo.
#// * La cantidad de artículos en la sucursal 2.
#// * La cantidad del articulo 3 en la sucursal 1.
#// * La recaudación total de cada sucursal.
#// * La recaudación total de la empresa.
#// * La sucursal de mayor recaudación.


precio = []
cantidad = []

for i in range(5):
    p = float(input(f"Ingrese Precio Artículo {i+1}: "))
    precio.append(p)

for i in range(4):
    fila = []
    for j in range(5):
        c = int(input(f"Ingrese Cant. de Artículo {j+1}, en Sucursal {i+1}: "))
        fila.append(c)
    cantidad.append(fila)


print("\nCantidades por artículos:")
for j in range(5):
    suma = 0
    for i in range(4):
        suma += cantidad[i][j]
    print(f"Total artículo {j+1}: {suma}")

articulos_sucursal2 = 0
for j in range(5):
    articulos_sucursal2 += cantidad[1][j]

print("\nTotal Sucursal 2:", articulos_sucursal2)


print("Sucursal 1, Artículo 3:", cantidad[0][2])

mayor_rec = 0
num_mayor = 0
total_empresa = 0

for i in range(4):
    total_sucursal = 0
    
    for j in range(5):
        total_sucursal += cantidad[i][j] * precio[j]
    
    print(f"Recaudación Sucursal {i+1}: {total_sucursal}")
    
    if total_sucursal > mayor_rec:
        mayor_rec = total_sucursal
        num_mayor = i + 1
    
    total_empresa += total_sucursal

print("\nRecaudación total de la empresa:", total_empresa)
print("Sucursal de mayor recaudación:", num_mayor)