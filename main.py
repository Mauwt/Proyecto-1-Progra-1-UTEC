import opciones
import time
import os
import platform

def opcion_salir():

    im_pantalla()
    cont = 0
    while cont <=2:
        time.sleep(0.6)
        print('saliendo del programa.....')
        im_pantalla()
        if cont ==2:
            time.sleep(0.8)
            print("⣿⣿⣿⣿⣿⣿⣿⣿⡇GRACIAS⣿⣿⣿⣿⣿⣿⣿⣿⡇" + "\n" "⣿⣿⣿⣿⣿⣿VUELVA PRONTO⣿⣿⣿⣿⣿")
        cont += 1

def im_pantalla():

    time.sleep(0.5)
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def anterior():
    print('\n')
    print('[0]salir' + "\n" + '[1]regresar al menu')
    print('\n')
    
    gg = int(input('Ingrese una opcion:'))
    if gg == 1:
        im_pantalla()
    else:
        return False

def menu():

  while True:
    print("⣿⣿⣿⣿⣿⣿⣿⣿⡇VENTA DE AUTOS⣿⣿⣿⣿⣿⣿⣿⣿⡇")
    print()
    
    print("1   Registrar Autos \n2   Autos disponibles\n3   Comprar Auto \n4   salir")
      
    opcion = int(input("Seleccione una opción: \n"))

    if opcion == 1:
        im_pantalla()
        opciones.registro()
        
        salir = anterior()
        if salir == False:
            break

    if  opcion == 2:
        im_pantalla()
        opciones.disponibles()
          
    if opcion == 3:
        opciones.venta()
        
        salir = anterior()
        if salir == False:
            break

    if opcion == 4:
        opcion_salir()
        break

    elif opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 :
        im_pantalla()
        print('\n')
        print( '⣿⣿ Ingrese una opción válida ⣿⣿' )
        print()

if __name__ == '__main__':         
    menu()