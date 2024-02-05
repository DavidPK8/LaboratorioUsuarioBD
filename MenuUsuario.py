from LoggerBase import log
from UsuarioDAO import UsuarioDAO
from Usuario import Usuario

def menu():
    global opcion
    print("*** MENU ***")
    print("1. Mostrar")
    print("2. Insertar")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))

menu()

while opcion != 5:
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuarioObj in usuarios:
            log.debug(usuarioObj)
    elif opcion == 2:
        nombre = input("Ingrese el nombre: ")
        clave = input("Ingrese el password: ")
        usuario1 = Usuario(username = nombre, password = clave)
        usuariosInsertados = UsuarioDAO.insertar(usuario1)
        log.debug(f"Personas insertadas: {usuariosInsertados}")
    elif opcion == 3:
        id = int(input("Ingrese el id que desee modificar: "))
        nombre = input("Ingrese el nombre: ")
        clave = input("Ingrese el password: ")
        usuario1 = Usuario(id, nombre, clave)
        usuariosActualizados = UsuarioDAO.actualizar(usuario1)
        log.debug(f"Personas actualizadas: {usuariosActualizados}")
    elif opcion == 4:
        id = int(input("Ingrese el id que desee eliminar: "))
        usuario1 = Usuario(idUsuario = id)
        usuariosEliminados = UsuarioDAO.eliminar(usuario1)
        log.debug(f"Personas eliminadas: {usuariosEliminados}")
    else:
        log.debug("Opcion no disponible del menu, vuelva a intentarlo")

    menu()

log.debug("FIN DEL PROGRAMA")