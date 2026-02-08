#Iniciales


nombre = input("Dime tu nombre: ")
apellido1 = input("Dime tu primer apellido: ")
apellido2 = input("Dime tu segundo apellido: ")

iniciales = (nombre[0] + apellido1[0] + apellido2[0]).upper()

print(f"Las iniciales son: {iniciales}")