# Trabajo-algoritmos-y-programación
# Nombre:
La Sierra Resort Natural
# Lema: 
Desconecta del mundo, reconecta contigo,  en armonía con la tierra y el mar 
# layout:
<img width="736" height="522" alt="Captura de pantalla 2025-10-02 234508" src="https://github.com/user-attachments/assets/da1aeb2a-6a46-4491-a399-3ed4285ddb8f" />

# Descripción:
La Sierra Resort Natural es un sistema integral de gestión hotelera desarrollado en Python que simula la operación completa de un resort ecológico de lujo. Este software permite administrar de manera eficiente todos los procesos operativos del resort, desde la planificación de recursos y la llegada de huéspedes hasta el control financiero y la generación de reportes gerenciales. ste proyecto refleja fielmente la experiencia de la lúdica realizada, transformando un ejercicio práctico en una herramienta tecnológica funcional y escalable.

# EQUIPO DESARROLLADOR

# Líder del Proyecto: 
Vanessa Giraldo
# Programa: 
Ingeniería Industrial
# Habilidades y Fortalezas:
Liderazgo proactivo: Capacidad excepcional para dirigir equipos, tomar decisiones estratégicas y mantener la motivación del grupo hacia el cumplimiento de objetivos.
Visión analítica: Habilidad sobresaliente para descomponer problemas complejos, identificar requisitos clave y estructurar soluciones eficientes.
Dominio tecnológico: Agilidad destacada en el manejo de plataformas digitales

# Responsabilidades en el Proyecto:
Coordinación general del equipo y distribución de tareas
Creación y gestión del repositorio en GitHub
Desarrollo del módulo de planeación de demanda y estructura principal del programa
Implementación del sistema de menús y navegación
Supervisión de la integración de todos los módulos
Preparación de la documentación técnica
Coordinación de pruebas y debugging final

# Desarrolladora: 
Tania Ramírez
# Programa: 
Ingeniería Industrial
# Habilidades y Fortalezas:

Alta productividad: Capacidad demostrada para desarrollar código funcional de manera eficiente, cumpliendo con plazos establecidos sin sacrificar calidad.
Atención al detalle: Meticulosidad en la implementación de validaciones, manejo de errores y experiencia de usuario, garantizando robustez del sistema.
Adaptabilidad tecnológica: Facilidad para aprender y aplicar nuevas tecnologías, librerías y metodologías de programación de forma ágil y efectiva.

# Responsabilidades en el Proyecto:

Desarrollo del módulo de registro de clientes y validaciones de datos
Implementación del sistema de cálculo de costos, ventas y ganancias
Desarrollo del módulo administrador y sistema de reportes
Creación del sistema de exportación a archivos CSV
Diseño de la interfaz visual de consola con colores y formato
Realización de pruebas de funcionalidad y casos de uso
Apoyo en la documentación de código y preparación para sustentación

# a. VISIÓN
El programa que se hará tendrá por nombre software la sierra resort y será una aplicación de consola en Python, fácil de usar y agradable a los ojos, que proporciona información sobre el resort. La idea es que los usuari͏os pueden ingresar su demanda antes de empezar para que asi nosotros podamos regi͏strar llegada͏s de clientes e͏stables,͏ saca͏r costos, ventas y beneficios automáticos. Tamb͏ién hay un módulo que muestra informes unidos de lo que ha pasado en un día. Al final, el sistema puede guardar los datos más importantes, est͏o f͏acilitar͏á dar resulta͏dos y analizar luego.
El objetivo principal de este desarrollo es hacer más fácil la gestión del resort, disminuyendo errores humanos en los cuadernos y ͏asegurando que la información esté siempre en orden y accesible. También se quiere que cualquiera, hasta alguien sin saber de tecnología, pueda usarlo sin problema gracias a una clara entrada de datos.
Las ventaj͏a͏s de este procgrama son much͏os: por un lado, dej͏ará tener manejo y segui͏mien͏to sobre los clientes y servicios; por otro, ahorrara tiempo al automatizar l͏os cálculos d͏e ventas y gananci͏as.

# b. REQUISITOS
Funcionales:El sistema debe permitir ingresar la oferta inicial de servicios y recursos , para así tener claro con cuántas habitaciones, cupos de turismo o alimentos se cuenta. Durante el día, cada vez que lleguen clientes, el programa debe registrar sus datos. En caso de que sea una familia se deben ingresar cuatro personas, si es pareja serán dos y si es individual solo una. Para cada persona se solicitará nombre, apellido y documento, aplicando validaciones como evitar números en los nombres y apellidos, y garantizar que los documentos tengan únicamente dígitos con una longitud adecuada, a medida que ingresamos datos debe ir descontando de la oferta esa demanda.

El software debe ser capaz de hacer los cálculos de ventas, costos y ganancias en tiempo real adicional a ello existirá un espacio exclusivo para el administrador, al cual se accede con un usuario y una contraseña que deben coincidir con los que estén registrados previamente. Una vez dentro, se podrán consultar reportes como el número total de clientes, el desglose por tipo de grupo, la cantidad de mascotas registradas, la disponibilidad restante de habitaciones, turismo y alimentación, además de los reportes de ventas, costos y ganancias; Cuando el día termine, el sistema ofrecerá la opción de salir y guardar.

No funcionales: el programa debe ser claro y fácil de usar, responder rápido a las acciones del usuario. También debe ser confiable, mostrando mensajes de error cuando haya datos inválidos en lugar de fallar, y debe cuidar la seguridad de la información, en especial las credenciales de acceso. La compatibilidad es otro punto importante: el programa debe poder ejecutarse sin problema en cualquier sistema operativo que tenga instalada una versión reciente de Python, y los archivos guardados que genere deben abrirse en otros programas. La estructura del código, además, debe ser modular, para que en el futuro se puedan añadir nuevas funciones sin complicaciones.

# c. LIBRERIAS
Para hace͏r el progr͏ama s͏e pueden usar difere͏nte͏s librerias de Python, en la parte de datos podemos usar Pandas, que hace fácil poner͏ información en tablas, hacer cálculos y crear reportes con m͏ucho más libertad.Para ͏hacer de mejor forma lo que se ve en ͏la pantalla ͏se puede usar una librería como rich o para algo ͏más sencillo, tabulate, ͏estas librerías dejan mostr͏ar ta͏blas d͏e manera clara y más linda. En el asunto de validaciones la librer͏ía re es buena para͏ verificar que l͏os nombres y apellidos no tengan ͏números͏ y ͏que los documentos so͏lo tengan cifras.
Para la zona de contraseñas se puede recurrir a getpass, que evita que estas aparezcan en pantalla mientras se escriben, si queremos protegerlas aún más, podemos almacenarlas como un hash en lugar de texto plano, y para eso sirven librerías como hashlib o bcrypt


# d. VISUAL

<img width="472" height="310" alt="image" src="https://github.com/user-attachments/assets/2848fac9-216d-42f6-927c-ca1a434c31b8" />

# e. ALGORITMOS

INICIO SistemaResort

    // --- Planeación de la demanda ---
    Mostrar "Ingrese alistamiento inicial"
    Solicitar capacidades de habitaciones, alimentación y turismo
    Guardar datos de alistamiento

    // --- Menú principal del sistema ---
    REPEAT
        Mostrar menú:
            1. Registrar llegada de clientes
            2. Consultar módulo administrador
            3. Cerrar sistema

        Leer opción

        SI opción == 1 ENTONCES
            // --- Registro de clientes ---
            Mostrar tipos de cliente (individual, pareja, familia)
            Leer tipoSeleccionado

            Determinar número de personas a registrar según tipo
            PARA cada persona
                Solicitar nombre, apellido y documento
                Validar datos ingresados
                Guardar persona en lista de clientes
            FIN PARA

            Actualizar disponibilidad y ventas según el tipo registrado
            Mostrar "Registro exitoso"

        FIN SI


        SI opción == 2 ENTONCES
            // --- Módulo administrador ---
            Solicitar usuario y contraseña
            Validar credenciales

            SI credenciales correctas ENTONCES
                Mostrar reportes:
                    - Total de clientes
                    - Clientes por tipo
                    - Total de mascotas
                    - Disponibilidad de habitaciones, turismo y alimentación
                    - Ventas, costos y ganancia

                // --- Cálculo financiero general ---
                ventas = totalClientes * precioUnitario
                costos = costosFijos + costosVariables
                ganancia = ventas - costos

            SINO
                Mostrar "Acceso denegado"
            FIN SI

        FIN SI

    UNTIL opción == 3

    // --- Cierre del sistema ---
    Preguntar si desea exportar datos a CSV
    SI respuesta == sí ENTONCES
        Generar archivo CSV con clientes y totales
    FIN SI

    Mostrar "Sistema finalizado"

FIN SistemaResort
    
# f. ESTRUCTURAS DE DATOS - LA SIERRA RESORT NATURAL 

# 1 DICCIONARIO: ADMIN_USERS
ADMIN_USERS = {
    'admin': 'admin123',
    'vanessa.giraldo': 'sierra2024',
    'tania.ramirez': 'resort2024'
}
# Justificación:

- Acceso rápido O(1): Permite verificar credenciales instantáneamente usando el usuario como clave
- Relación clave-valor: Asocia naturalmente cada usuario con su contraseñaJustificación:
- Acceso rápido O(1): Permite verificar credenciales instantáneamente usando el usuario como clave
- Relación clave-valor: Asocia naturalmente cada usuario con su contraseña

# Datos Almacenados:

- Clave: Nombre de usuario (string)
- Valor: Contraseña (string)

# 2. DICCIONARIO: PRECIOS

PRECIOS = {
    'familia': 350000,
    'pareja': 200000,
    'individual': 120000
}

# Justificación:
- Legibilidad: Asocia claramente cada tipo de cliente con su tarifa
- Mantenibilidad: Centraliza los precios en un solo lugar, fácil de actualizar

# Datos Almacenados:

- Clave: Tipo de cliente ('familia', 'pareja', 'individual')
- Valor: Precio en pesos colombianos (integer)

# 3. LISTA: clientes
# Justificación:

- Orden cronológico: Mantiene el orden de llegada de los clientes
- Tamaño dinámico: Crece automáticamente con cada nuevo registro
