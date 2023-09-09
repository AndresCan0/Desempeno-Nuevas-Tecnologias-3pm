import os
import time
usuarios = {}

prestamos = []



max_length = 0  



border = '+' + '-' * 48 + '+'  

menu = """
++++++++++++++++++++++++++++++++++++++++++++++++++++
|              Sistema de Préstamos de              |
|            Bicicletas de la Ciudad                |
|                                                   |
| 1. Registrar Usuario                              |
| 2. Iniciar Sesión                                 |
| 3. Salir                                          |
++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

menu_usuario = """
++++++++++++++++++++++++++++++++
|             Menu de Usuario       |
|                                   |
| 1. Tomar Bicicleta                |
| 2. Consultar Listado de Usuarios  |
| 3. Consultar Listado de Préstamos |
| 4. Cerrar Sesión                  |
+++++++++++++++++++++++++++++++++
"""

print(border)
print('|', 'Nombre:', 'Andres Felipe Cano Colorado ' , '          |')  
print('|', 'Clase:', 'Nuevas Tecnologias 3pm', '                 |')  
print('|', 'Fecha:', '09/09/2023' , '                             |')   
print(border)

def registrar_usuario():
    numero_tarjeta = input("Ingrese el número de tarjeta del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    usuarios[numero_tarjeta] = {'nombre': nombre, 'contrasena': input("Ingrese la contraseña del usuario: ")}
    print(f"Usuario registrado: {nombre} (Tarjeta: {numero_tarjeta})")
    time.sleep(2)

def iniciar_sesion():
    numero_tarjeta = input("Ingrese el número de tarjeta del usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    if numero_tarjeta in usuarios and usuarios[numero_tarjeta]['contrasena'] == contrasena:
        print(f"Sesión iniciada para el usuario: {usuarios[numero_tarjeta]['nombre']}")
        return numero_tarjeta
    else:
        print("\nInicio de sesión fallido. Verifique el número de tarjeta y la contraseña.")
        return None

# Función para que un usuario tome una bicicleta
def tomar_bicicleta(numero_tarjeta):
    origen = input("Ingrese el origen del viaje: ")
    destino = input("Ingrese el destino del viaje: ")
    prestamos.append({
        'usuario': usuarios[numero_tarjeta]['nombre'],
        'origen': origen,
        'destino': destino
    })
    print(f"{usuarios[numero_tarjeta]['nombre']} ha cogido una cicla desde {origen} hasta {destino}")
    time.sleep(2)

# Función para consultar el listado de usuarios
def consultar_listado_usuarios():
    print("Listado de Usuarios:")
    for numero_tarjeta, datos in usuarios.items():
        print(f"Tarjeta: {numero_tarjeta}, Nombre: {datos['nombre']}")
        time.sleep(5)

# Función para consultar el listado de préstamos
def consultar_listado_prestamos():
    print("Listado de Préstamos:")
    for prestamo in prestamos:
        print(f"Usuario: {prestamo['usuario']}, Origen: {prestamo['origen']}, Destino: {prestamo['destino']}")
        time.sleep(6)

while True:
    opcion = input(menu + "Seleccione una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        numero_tarjeta = iniciar_sesion()
        if numero_tarjeta:
            while True:
                opcion_usuario = input(menu_usuario + "Seleccione una opción: ")

                if opcion_usuario == '1':
                    tomar_bicicleta(numero_tarjeta)
                elif opcion_usuario == '2':
                    consultar_listado_usuarios()
                elif opcion_usuario == '3':
                    consultar_listado_prestamos()
                elif opcion_usuario == '4':
                    print(f"Sesión cerrada para el usuario: {usuarios[numero_tarjeta]['nombre']}")
                    break
                else:
                    print("Opción invalida. Por favor, seleccione una opción válida. ")

    elif opcion == '3':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
