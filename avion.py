from os import system
system("cls")
while True:
    print("""
    ¡Bienvenidos a Lemon airlines!
    
    1- Comprar pasajes
    2- Mostrar ubicaciones disponibles
    3- Ver listado de pasajeros
    4- Buscar pasajero
    5- Imprimir lista de pasajeros
    0- Salir""")
    op=input("Elige una opcion: ")
    match op:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "0":
            import sys
            sys.exit()
        case other:
            print("¡Error! Opcion no valida!")
            