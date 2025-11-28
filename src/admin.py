# Aquí va el login del administrador y todos los reportes importantes.
from datos import ADMIN_USERS, clientes, demanda
from funciones import calcular_finanzas

def admin_login():
    print("\n--- INICIO DE SESIÓN ADMINISTRADOR ---")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if usuario in ADMIN_USERS and ADMIN_USERS[usuario] == contrasena:
        print("Acceso permitido.")
        admin_menu()
    else:
        print("Credenciales incorrectas.")



def admin_menu():
    while True:
        print("\n--- MÓDULO ADMINISTRADOR ---")
        print("1. Total clientes")
        print("2. Clientes por tipo")
        print("3. Disponibilidad actual")
        print("4. Ventas totales")
        print("5. Salir del administrador")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"\nTotal de clientes: {len(clientes)}")

        elif opcion == "2":
            tipos = {"individual": 0, "pareja": 0, "familia": 0}
            for c in clientes:
                tipos[c["tipo"]] += 1
            print("\nClientes por tipo:")
            print(tipos)

        elif opcion == "3":
            print("\nDemanda restante:")
            print(demanda)

        elif opcion == "4":
            calcular_finanzas()

        elif opcion == "5":
            print("Saliendo del administrador...")
            break

        else:
            print("Opción inválida.")