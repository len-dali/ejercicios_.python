#/Procedimiento IncializarPila

def inicializar_pila():
    return []

def add_pila(elem, pila, tam_pila):
    if len(pila) < tam_pila:
        pila.append(elem)
    else:
        print("La pila está llena")


def sacar_de_la_pila(pila):
    if len(pila) > 0:
        return pila.pop()
    else:
        return "La pila está vacía"

def longitud_pila(pila):
    return len(pila)
def escribir_pila(pila):
    if len(pila) == 0:
        print("La pila está vacía")
    else:
        print("Contenido de la pila:", pila)


tam_pila = 10
mipila = inicializar_pila()

while True:

    print("1.- Añadir elemento a la pila")
    print("2.- Sacar elemento de la pila")
    print("3.- Longitud de la pila")
    print("4.- Mostrar pila")
    print("5.- Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        elem = input("Dame la cadena para añadir a la pila: ")
        add_pila(elem, mipila, tam_pila)

    elif opcion == 2:
        print(sacar_de_la_pila(mipila))

    elif opcion == 3:
        print("Longitud:", longitud_pila(mipila))

    elif opcion == 4:
        escribir_pila(mipila)

    elif opcion == 5:
        break

    else:
        print("Opción incorrecta")