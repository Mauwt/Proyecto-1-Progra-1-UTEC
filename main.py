import opciones
import time
import os
import platform
import sys

def animacion_de_carga():
  print("cargando:")
  
  #animacion = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
  animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
  
  for i in range(len(animation)):
      time.sleep(0.2)
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()
  im_pantalla() 

def load_animation(mensaje):  
    # Cadena que se mostrará cuando se cargue la aplicación    
    ls_len = len(mensaje)  
    # Cadena para crear la línea giratoria
    animation = ". . . . . ."
    anicount = 0      
    # utilizado para realizar un seguimiento de la duración de la animación
    counttime = 0        
    i = 0                  
    while (counttime != 100):
        
        time.sleep(0.075)               
        
        # convertir la cadena a lista ya que la cadena es inmutable
        load_str_list = list(mensaje)          
        
        # x->obteniendo el código ASCII
        x = ord(load_str_list[i])
          
        # y->para almacenar código ASCII alterado
        y = 0                             
  
        # si el caracter es "." o " ", manténgalo inalterado cambiar mayúsculas a minúsculas y viceversa
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # para almacenar la cadena resultante
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
        
        # mostrando la cadena resultante
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
        mensaje = res
  
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1

def opcion_salir():

    im_pantalla()
    load_animation('saliendo del programa')

    print( )
    print("⣿⣿⣿⣿⣿⣿⣿⣿⡇GRACIAS⣿⣿⣿⣿⣿⣿⣿⣿⡇" + "\n" "⣿⣿⣿⣿⣿⣿VUELVA PRONTO⣿⣿⣿⣿⣿")

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
        animacion_de_carga()
    else:
        return False

def menu():

  while True:
    print("\n⣿⣿⣿⣿⣿⣿⣿⣿⡇VENTA DE AUTOS⣿⣿⣿⣿⣿⣿⣿⣿⡇")
    print()
    
    print("1   Registrar Autos \n2   Autos disponibles\n3   Comprar Auto \n4   salir")
      
    opcion = int(input("Seleccione una opción: \n"))

    if opcion == 1:
        im_pantalla()
        animacion_de_carga()
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