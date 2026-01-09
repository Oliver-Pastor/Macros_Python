#Programa para calcular macronutrientes dependiendo del objetivo
#Oliver Pastor 7/01/2026

def leer_peso():
    """
    Solicita el peso al usuario y valida que los datos sean validos.

    Se repite hasta que el usuario ingrese un numero valido > que 0.

    Retorna:
        float: Peso en kilogramos
    """
    while True:  #Repetir hasta que este bien
        try:    #Intenta algo que pueda fallar
            peso=float(input("Ingrese su peso en Kilos:")) 
            if peso <=0:
                print("El peso debe ser mayor que 0")
            else:
                return peso
        except ValueError: #Que hacer si falla
            print("Ingrese un numero valido")

def leer_etapa():
    """
    Solicita la etapa al usuario.

    Opciones:
        1. volumen (Ganancia muscular)
        2. Deficit (Perdida de grasa)

    Retorna:
        int: etapa seleccionada (1 o 2).
    """
    while True:
        try:
            etapa = int(input("Ingrese opcion 1 o 2"))
            if etapa in (1,2): #etapa esta dentro del conjunto 1 o 2
                return etapa   #equivalente a if etapa ==1 or etapa ==2:
            print("Solo 1 o 2")
        except ValueError:
            print("Ingrese un numero valido") #Se ejecuta si falla la conversion

def VolumenM():
    print("Vamo con fua")


def Deficit():
    print("Para la playa")


print("==============================")
print("Calculadora de macronutrientes")
print("==============================") #Mensaje
print("1. Volumen (Ganancia muscular)")
print("2. Deficit (Perdida de grasa)" )
print("------------------------------")

peso = leer_peso()
etapa=leer_etapa()


#Math es el switch en python 
match etapa:
    case 1:
        VolumenM()
    case 2:
        Deficit()
    case _:
        print("Opcion invalida")