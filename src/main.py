# Este archivo tiene la función de mostrar el menú principal, 
# llamar a las funciones correspondientes según la elección del usuario y 
# manejar la lógica principal del programa, y controlar el flujo de la aplicación.


# Por ahora solo creamos el menú principal.
from funciones import planear_demanda, registrar_cliente, calcular_finanzas, limpiar_consola
from admin import admin_login

def menu_principal():
    # Muestra el menú principal y permite al usuario seleccionar opciones.
    while True:
        print("\n=======================================")
        print("     LA SIERRA RESORT NATURAL")
        print("=======================================")
        print("1. Planeación de la demanda")
        print("2. Registro de clientes")
        print("3. Cálculo de costos y ventas")
        print("4. Módulo administrador")
        print("5. Salir")
        print("=======================================")

        opcion = input("Seleccione una opción: ")

        limpiar_consola()

        if opcion == "1":
            planear_demanda()

        elif opcion == "2":
            registrar_cliente()

        elif opcion == "3":
            calcular_finanzas()

        elif opcion == "4":
            admin_login()
        elif opcion == "5":
            print("\n¿Desea exportar los datos del día a CSV? (s/n)")
            exportar = input("> ").lower()

            if exportar == "s":
                from funciones import exportar_clientes, exportar_finanzas
                exportar_clientes()
                exportar_finanzas()

            print("\nGracias por usar el sistema. Hasta pronto.")
            break

        else:
            print("\nERROR!!!!! \nOpción inválida. Intente nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()