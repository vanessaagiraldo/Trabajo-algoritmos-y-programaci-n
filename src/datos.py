# Aquí se guarda toda la información del resort: los clientes, los precios, 
# la oferta disponible y los datos del administrador.

# Define Usuarios administrador
ADMIN_USERS = {
    "admin": "admin123",
    "vanessa.giraldo": "sierra2024",
    "tania.ramirez": "resort2024"
}


# Precios por tipo de cliente
PRECIOS = {
    "familia": 350000,
    "pareja": 200000,
    "individual": 120000
}

# Costos por habitación, alimentación por persona y turismo por persona
COSTOS = {
    "habitacion": 60000,
    "alimentacion": 15000,
    "turismo": 10000
}

# Lista de clientes registrados
clientes = []


# Demanda inicial del resort (planeación)
demanda = {
    "habitaciones": 0,
    "turismo": 0,
    "alimentacion": 0,
    "mascotas": 0
}


# Estado financiero del día
estado_financiero = {
    "ventas": 0,
    "costos": 0,
    "ganancia": 0
}
