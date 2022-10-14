import opciones

print("VENTA DE AUTOS")
while True:
    print("1   Registrar Autos \n2   Autos disponibles\n3   Comprar Auto")
    
    opcion = int(input("Seleccione una opción: \n"))
    if opcion == 1:
        opciones.registro()
        break
    if opcion == 2:
        opciones.disponibles()
        break
    if opcion == 3:
        opciones.venta()
        break
