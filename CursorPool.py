from Conexion import Conexion
from LoggerBase import log


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug("Inicio del metodo with __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipoExcepcion, valorExcepcion, detalleExcepcion):
        log.debug("Se ejecuta el metodo __exit__")
        if valorExcepcion:
            self._conexion.rollback()
            log.error(f"Ocurrio un error: {valorExcepcion} {tipoExcepcion} {detalleExcepcion}")
        else:
            self._conexion.commit()
            log.debug("Commit de la transaccion")
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug("Dentro del bloque with")
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())