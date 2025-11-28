# Aquí van las funciones del programa. Se ponen funciones para validar, registrar 
# y calcular

from datos import demanda, clientes, PRECIOS, COSTOS
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
    registros_temporales = []
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

        # Guardar temporalmente (no añadimos aún a `clientes`)
        registros_temporales.append({
            "nombre": nombre,
            "apellido": apellido,
            "documento": documento,
            "tipo": tipo
        })

    # Si llegamos aquí, todos los miembros del grupo son válidos: se añaden todos a la lista global
    clientes.extend(registros_temporales)

    # Actualizar demanda
    demanda["habitaciones"] -= 1
    demanda["turismo"] -= personas
    demanda["alimentacion"] -= personas

    print(f"\nSe registró un grupo tipo '{tipo}' con {personas} personas.")
    print("Estado actual de la demanda:")
    print(demanda)


def calcular_finanzas():
    print("\n--- COSTOS, VENTAS Y GANANCIAS ---")

    # Contar personas por tipo (cada cliente es una persona)
    conteo_personas = {"individual": 0, "pareja": 0, "familia": 0}
    for c in clientes:
        tipo = c.get("tipo")
        if tipo in conteo_personas:
            conteo_personas[tipo] += 1

    # Convertir personas → grupos
    grupos = {
        "individual": conteo_personas["individual"],     # 1 persona = 1 grupo
        "pareja": conteo_personas["pareja"] // 2,        # 2 personas = 1 grupo pareja
        "familia": conteo_personas["familia"] // 4       # 4 personas = 1 grupo familia
    }

    # Totales acumulados
    total_costos = 0
    total_ventas = 0
    total_ganancias = 0

    # Personas por tipo de grupo
    personas_por_tipo = {
        "individual": 1,
        "pareja": 2,
        "familia": 4
    }

    print("\nDetalle por tipo de grupo:")

    for tipo, cantidad_grupos in grupos.items():
        if cantidad_grupos == 0:
            continue

        personas = personas_por_tipo[tipo]

        # Costo total del grupo
        costo_por_grupo = (
            COSTOS["habitacion"] +
            COSTOS["alimentacion"] * personas +
            COSTOS["turismo"] * personas
        )

        venta_por_grupo = PRECIOS[tipo]
        ganancia_por_grupo = venta_por_grupo - costo_por_grupo

        total_costos += costo_por_grupo * cantidad_grupos
        total_ventas += venta_por_grupo * cantidad_grupos
        total_ganancias += ganancia_por_grupo * cantidad_grupos

        print(f"\nTipo: {tipo.capitalize()}")
        print(f" - Grupos vendidos:   {cantidad_grupos}")
        print(f" - Costo por grupo:   ${costo_por_grupo}")
        print(f" - Venta por grupo:   ${venta_por_grupo}")
        print(f" - Ganancia por grupo:${ganancia_por_grupo}")

    print("\n--- RESUMEN GENERAL ---")
    print(f"Costos totales:    ${total_costos}")
    print(f"Ventas totales:    ${total_ventas}")
    print(f"Ganancia neta:     ${total_ganancias}")


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')