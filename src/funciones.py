# Aquí van las funciones del programa. Se ponen funciones para validar, registrar 
# y calcular

from datos import demanda, clientes, PRECIOS
import os

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

        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        documento = input("Documento: ").strip()

        # Validaciones sencillas (sin librerías externas)
        # Nombre: más de 3 letras y sin números
        if nombre == "":
            print("El nombre no puede ser vacío.")
            return
        nombre_sin_espacios = nombre.replace(" ", "")
        if len(nombre_sin_espacios) <= 3 or not nombre_sin_espacios.isalpha():
            print("Nombre inválido: debe tener más de 3 letras y no contener números.")
            return

        # Apellido: más de 3 letras y sin números
        if apellido == "":
            print("El apellido no puede ser vacío.")
            return
        apellido_sin_espacios = apellido.replace(" ", "")
        if len(apellido_sin_espacios) <= 3 or not apellido_sin_espacios.isalpha():
            print("Apellido inválido: debe tener más de 3 letras y no contener números.")
            return

        # Documento: solo números y longitud entre 3 y 15
        if documento == "":
            print("El documento no puede ser vacío.")
            return
        if not documento.isdigit() or not (3 <= len(documento) <= 15):
            print("Documento inválido: debe tener solo números y entre 3 y 15 dígitos.")
            return

        # Validar que no exista el documento
        for c in clientes:
            if c["documento"] == documento:
                print("Este documento ya está registrado.")
                return

        # Registrar persona
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


def calcular_finanzas():
    print("\n--- CÁLCULO DE FINANZAS ---")

    # Contar personas por tipo
    conteo = {"individual": 0, "pareja": 0, "familia": 0}

    for cliente in clientes:
        tipo = cliente["tipo"]
        if tipo in conteo:
            conteo[tipo] += 1

    # Convertir de personas a grupos
    grupos_individual = conteo["individual"]        # 1 persona = 1 grupo
    grupos_pareja = conteo["pareja"] // 2           # 2 personas por grupo
    grupos_familia = conteo["familia"] // 4         # 4 personas por grupo

    # Calcular ventas
    ventas = (
        grupos_individual * PRECIOS["individual"] +
        grupos_pareja * PRECIOS["pareja"] +
        grupos_familia * PRECIOS["familia"]
    )

    print("\nResumen:")
    print(f" - Grupos individuales: {grupos_individual}")
    print(f" - Grupos pareja:      {grupos_pareja}")
    print(f" - Grupos familia:     {grupos_familia}")
    print(f"\nVentas totales: ${ventas}")


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')