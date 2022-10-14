from tabulate import tabulate

def registro():

    # Petición y validación de datos 
    marca = input("Marca: ").capitalize()
    fabricacion = int(input("Año de fabricación: "))
    color = input("Color: ").lower()
    precio = int(input("Precio (S/):"))
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

    # with open("autos_db.txt","r",encoding="UTF-8") as F:

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
    marca = input("Marca: ").capitalize()
    fabricacion = int(input("Año de fabricación: "))
    color = input("Color: ").lower()
    precio = int(input("Precio (S/):"))

    auto_seleccionado = [marca, fabricacion, color, precio, "disponible"]
    autos=[]

    with open("autos_db.txt", "r", encoding="UTF-8") as F:
        autos = F.readlines()
        F.close()
    
    for i in range(len(autos)):
        if autos[i].replace("\n","") == str(auto_seleccionado):
            autos[i] = autos[i].replace("disponible", "vendido")
    
    with open("autos_db.txt", "w", encoding="UTF-8") as F:
        for i in range(len(autos)):
            line = str(autos[i])
            F.write(line)
        F.close()
            

    print(autos)
    print(str(auto_seleccionado))
