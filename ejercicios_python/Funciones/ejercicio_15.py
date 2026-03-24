#Procedimiento IncializarCola

def inicializar_cola():
    return []

def add_cola(elem, cola, tam_cola):
    if len(cola) < tam_cola:
        cola.append(elem)
    else:
        print("La cola está llena")


def sacar_de_la_cola(cola):
    if len(cola) > 0:
        return cola.pop(0)
    else:
        return "La cola está vacía"


def longitud_cola(cola):
    return len(cola)


def escribir_cola(cola):
    if len(cola) == 0:
        print("La cola está vacía")
    else:
        print("Contenido de la cola:", cola)


tam_cola = 3
micola = inicializar_cola()

while True:

    print("1.- Añadir elemento a la cola")
    print("2.- Sacar elemento de la cola")
    print("3.- Longitud de la cola")
    print("4.- Mostrar cola")
    print("5.- Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        elem = input("Dame la cadena para añadir a la cola: ")
        add_cola(elem, micola, tam_cola)

    elif opcion == 2:
        print(sacar_de_la_cola(micola))

    elif opcion == 3:
        print("Longitud:", longitud_cola(micola))

    elif opcion == 4:
        escribir_cola(micola)

    elif opcion == 5:
        break

    else:
        print("Opción incorrecta")