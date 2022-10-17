from tabulate import tabulate

def registro():

    # Petición y validación de datos 
    marca = input("Marca: ").capitalize().strip()
    fabricacion = int(input("Año de fabricación: ").strip())
    color = input("Color: ").lower().strip()
    precio = int(input("Precio (S/):").strip())
    estado = "disponible"

    # Añadir el auto como lista al archivo autos_db.txt
    datos = [marca, fabricacion, color, precio,estado]

    with open("autos_db.txt", "a", encoding="UTF-8") as F:
        
        texto = []
        
        with open("autos_db.txt", "r", encoding="UTF-8") as G:
            
            texto = G.readlines()
            for i in range(len(texto)):
                texto[i]=texto[i].replace("\n", "")
            G.close()
        
        if str(datos) in texto:
            print("Este auto ya se encuentra registrado \n")
        
        else:
            F.write(str(datos) + "\n")
            F.close
            print("AUTO RERGISTRADO")   

def disponibles():
    autos = []
    tabla=[]

    with open("autos_db.txt", "r", encoding="UTF-8") as F:
        autos = F.readlines()
        F.close()

    for i in range(len(autos)):
        auto_ = autos[i].replace("\n","").replace("[","").replace("]","").replace(" ","").replace("'","").split(",")

        if auto_[4] == "disponible":
            tabla.append(auto_)
        else:
            continue
    
    print(tabulate(tabla, headers=["MARCA", "FABRICACIÓN", "COLOR", "PRECIO", "ESTADO"]))

def venta():
    # Petición y validación de datos 
    marca = input("Marca: ").capitalize().strip()
    fabricacion = int(input("Año de fabricación: ").strip())
    color = input("Color: ").lower().strip()
    precio = int(input("Precio (S/):").strip())

    if fabricacion > 2022 or fabricacion < 1700:
        print("\nIngrese una año de fabricación valido")
    if color.isnumeric() == True:
        print("\nIngrese un color valido")

    auto_seleccionado = [marca, fabricacion, color, precio, "disponible"]
    autos=[]

    with open("autos_db.txt", "r", encoding="UTF-8") as F:
        autos = F.readlines()
        F.close()
    
    no_found= True

    for i in range(len(autos)):
        if autos[i].replace("\n","") == str(auto_seleccionado):
            autos[i] = autos[i].replace("disponible", "vendido")
            no_found = False
        
    if no_found == True:
        print("No se encontro este auto en la base de datos")
    else:
        with open("autos_db.txt", "w", encoding="UTF-8") as F:
            for i in range(len(autos)):
                line = str(autos[i])
                F.write(line)
            print(str(auto_seleccionado[0]) + " "  + str(auto_seleccionado[1]) + ' VENDIDO')
            F.close()
