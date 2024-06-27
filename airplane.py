# ¡¡¡¡Aqui pondremos TODAS LAS FUNCIONES!!!!
# PARA AGREGAR FUNCIONES A ARCHIVO PRINCIPAL ---> airplane.funcion(argumento)
from os import system
asientos=[]
pasajeros=[]
persona=[]
# asiento comun $60.000
# asiento espacio piernas $80.000
# asiento preferente $100.000
def clear():
    system("cls")

def pause():
    input("Presione enter para continuar...")


def compra_pasajes(opcion):
    print(""" Seleccione el asiento a reservar:
        1.- Asiento común: $60.000
        2.- Espacio adicional para piernas: $80.000
        3.- Preferente: $100.000             """)
    match opcion: