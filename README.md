# Trabajo-algoritmos-y-programación
# Nombre:
La Sierra Resort Natural
# Lema: 
Desconecta del mundo, reconecta contigo,  en armonía con la tierra y el mar 
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

# d. VISUAL

╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║   ██╗      █████╗     ███████╗██╗███████╗██████╗ ██████╗      ║
    ║   ██║     ██╔══██╗    ██╔════╝██║██╔════╝██╔══██╗██╔══██╗    ║
    ║   ██║     ███████║    ███████╗██║█████╗  ██████╔╝██████╔╝    ║
    ║   ██║     ██╔══██║    ╚════██║██║██╔══╝  ██╔══██╗██╔══██╗    ║
    ║   ███████╗██║  ██║    ███████║██║███████╗██║  ██║██║  ██║    ║
    ║   ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ║
    ║                                                               ║
    ║              RESORT NATURAL - MANAGEMENT SYSTEM               ║
    ║                                                               ║
    ║         [-]  "Desconecta del mundo, reconecta contigo,   [-] ║
    ║         [-]   en armonía con la tierra y el mar"         [-] ║
    ║                                                               ║
    ║         Version: 1.0                                          ║
    ║         Desarrollado por: Vanessa Giraldo & Tania Ramírez    ║
    ║         Programa: Ingeniería Industrial - UdeA                ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
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
