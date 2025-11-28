# Aquí van las funciones del programa. Se ponen funciones para validar, registrar 
# y calcular

from datos import demanda

def planear_demanda():
    print("\n--- PLANEACIÓN DE LA DEMANDA ---")

    habitaciones = input("Ingrese habitaciones disponibles: ")
    turismo = input("Ingrese cupos de turismo: ")
    alimentacion = input("Ingrese cupos de alimentación: ")
    mascotas = input("Ingrese capacidad de mascotas: ")

    # Validar que sean números
    if not (habitaciones.isdigit() and turismo.isdigit() and alimentacion.isdigit() and mascotas.isdigit()):
        print("Por favor ingrese solo números.")
        return

    demanda["habitaciones"] = int(habitaciones)
    demanda["turismo"] = int(turismo)
    demanda["alimentacion"] = int(alimentacion)
    demanda["mascotas"] = int(mascotas)

    print("\nDemanda registrada correctamente:")
    print(demanda)