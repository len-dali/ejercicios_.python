#Calcular sueldo

sueldo_base = int(input("Dime tu sueldo base:"))
venta_1 = int(input("Dime el precio de la venta 1: "))
venta_2 = int(input("Dime el precio de la venta 2: "))
venta_3 = int(input("Dime el precio de la venta 3: "))
 
comisión = (venta_1 * 0.1 + venta_2 * 0.1 + venta_3 * 0.1)
print("Comisión por ventas:", comisión)
print("Sueldo base: ", sueldo_base+comisión)