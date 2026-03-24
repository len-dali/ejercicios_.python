#/Función Login: Recibe un nombre de usuario y una contraseña, y devuelve unvalor lógico: verdadero si se ha introducido el nombre y la contraseña adecuadas.


def login(usuario, clave, cuantasveces):
    usuario_correcto = "admin"
    clave_correcta = "1234"
    
    cuantasveces += 1
    
    if usuario == usuario_correcto and clave == clave_correcta:
        return True, cuantasveces
    else:
        return False, cuantasveces

cuantasveces = 0
entrar = False

while True:
    usuario = input("Usuario: ")
    clave = input("Password: ")

    entrar, cuantasveces = login(usuario, clave, cuantasveces)

    if not entrar:
        print("Error. Nombre de usuario o contraseña incorrecta.")

    if entrar or cuantasveces == 3:
        break

if entrar:
    print("Bienvenidos al sistema")
else:
    print("No has entrado en el sistema")