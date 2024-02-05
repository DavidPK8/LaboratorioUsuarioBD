from CursorPool import CursorDelPool
from Usuario import Usuario
from LoggerBase import log


class UsuarioDAO:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY "idUsuario"'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username = %s, password = %s WHERE "idUsuario" = %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE "idUsuario" = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            listaUsuarios = []
            for i in registros:
                usuario = Usuario(i[0], i[1], i[2])
                listaUsuarios.append(usuario)
            return listaUsuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = usuario.username, usuario.password
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Persona insertada: {usuario}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = usuario.username, usuario.password, usuario.idUsuario
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Persona actualizada: {usuario}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.idUsuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Persona eliminada: {usuario}")
            return cursor.rowcount


if __name__ == "__main__":
    # # Eliminar un registro
    usuario1 = Usuario(idUsuario = 5)
    usuariosEliminados = UsuarioDAO.eliminar(usuario1)
    log.debug(f"Personas eliminadas: {usuariosEliminados}")

    # Actualizar un registro
    # usuario1 = Usuario(1, "Paul", "4321")
    # usuariosActualizados = UsuarioDAO.actualizar(usuario1)
    # log.debug(f"Personas actualizadas: {usuariosActualizados}")

    # Insertar un registro
    # usuario1 = Usuario(username = "Martin", password = "1234")
    # usuariosInsertados = UsuarioDAO.insertar(usuario1)
    # log.debug(f"Personas insertadas: {usuariosInsertados}")

    # Seleccionar Objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuarioObj in usuarios:
        log.debug(usuarioObj)
