# Aquí van las funciones del programa. Se ponen funciones para validar, registrar 
# y calcular

from datos import demanda, clientes

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


# Función para registrar un cliente
def registrar_cliente():
    print("\n--- REGISTRO DE CLIENTES ---")

    print("Seleccione el tipo de grupo:")
    print("1. Individual (1 persona)")
    print("2. Pareja (2 personas)")
    print("3. Familia (4 personas)")

    opcion = input("Ingrese una opción (1-3): ")

    if opcion == "1":
        tipo = "individual"
        personas = 1
    elif opcion == "2":
        tipo = "pareja"
        personas = 2
    elif opcion == "3":
        tipo = "familia"
        personas = 4
    else:
        print("Opción inválida.")
        return

    # Validar disponibilidad mínima
    if demanda["habitaciones"] < 1:
        print("No hay habitaciones disponibles.")
        return
    if demanda["turismo"] < personas:
        print("No hay cupos de turismo suficientes.")
        return
    if demanda["alimentacion"] < personas:
        print("No hay cupos de alimentación suficientes.")
        return

    # Registrar por persona
    for i in range(personas):
        print(f"\nPersona {i+1}:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        documento = input("Documento: ")

        clientes.append({
            "nombre": nombre,
            "apellido": apellido,
            "documento": documento,
            "tipo": tipo
        })

    # Actualizar demanda
    demanda["habitaciones"] -= 1
    demanda["turismo"] -= personas
    demanda["alimentacion"] -= personas

    print(f"\nSe registró un grupo tipo '{tipo}' con {personas} personas.")
    print("Estado actual de la demanda:")
    print(demanda)