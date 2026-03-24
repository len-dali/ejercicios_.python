#Cadena con espacios

def ConvertirEspaciado(mensaje):
    return " ". join(mensaje)
    
mensaje = input("Introduce un mensaje: ")
print("El mensaje con espacios:")
print(ConvertirEspaciado(mensaje))