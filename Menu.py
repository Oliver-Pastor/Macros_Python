#Programa para calcular macronutrientes dependiendo del objetivo
#Oliver Pastor 7/01/2026

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

peso=float(input("Ingresa su peso en kg"))
etapa=int(input("Ingrese opcion (1 o 2) ")) #Opciones

match etapa:
    case 1:
        VolumenM()
    case 2:
        Deficit()
    case _:
        print("Opcion invalida")