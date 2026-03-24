#Procedimiento centrar: Recibe una cadena y la imprime centrada en la pantalla. Suponemos que tenemos una pantalla de 80 caracteres de ancho. Para centrar usamos la formula 40 - (Longitud(cad)/2) Parámetros de entrada: cadena a imprimir centrada

def centrar(cad):
    #Definir i como entero
    for i in range(40 - (len(cad) // 2)):
        print(" ", end="")
    print(cad)
    #Imprimir un subrrayado con "="
    for i in range (40 - (len(cad) // 2)):
        print (" ", end="")
    for i in range(len(cad)):
        print("=", end="")
    print(" ")

message_1 = "Un mensaje centrado"
centrar(message_1)
message_2 = "Otro mensaje"
centrar(message_2)

