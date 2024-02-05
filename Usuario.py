from LoggerBase import log


class Usuario:
    def __init__(self, idUsuario = None, username = None, password = None):
        self._idUsuario = idUsuario
        self._username = username
        self._password = password

    def __str__(self):
        return f"""
            Id Usuario = {self._idUsuario}
            Username = {self._username}
            Password = {self._password}
        """

    @property
    def idUsuario(self):
        return self._idUsuario

    @idUsuario.setter
    def idUsuario(self, idUsuario):
        self._idUsuario = idUsuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password


if __name__ == "__main__":
    usuario1 = Usuario(1, "David", "8888")
    log.debug(usuario1)
