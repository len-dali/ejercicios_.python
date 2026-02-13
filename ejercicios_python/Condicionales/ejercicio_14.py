#Precio de las Uvas

precio_inicial = float(input("Introduce el precio inicial (céntimos): "))
kilos = float(input("Introduce cuántos kilos has vendido: "))
tipo = input("Introduce el tipo de uva (A/B): ").upper()


if tipo != "A" and tipo != "B":
    print("Tipo incorrecto")
else:
    tamano = input("Introduce el tamaño de la uva (1/2): ")
    
    if tamano != "1" and tamano != "2":
        print("Tamaño incorrecto")
    else:
        
        if tipo == "A":
            if tamano == "1":
                precio_inicial += 20
            else:
                precio_inicial += 30
        else: 
            if tamano == "1":
                precio_inicial -= 20
            else:
                precio_inicial -= 30
        
        
        precio_final = precio_inicial * kilos
        print(f"La ganancia es {precio_final / 100} euros.")