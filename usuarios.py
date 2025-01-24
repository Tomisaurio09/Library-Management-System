class Usuario:
    def __init__(self,nombre,identificacion,tipo_usuario,email,libros_prestados):
        self.nombre = nombre
        self.identificacion = identificacion
        self.tipo_usuario = tipo_usuario
        self.email = email
        self.libros_prestados = libros_prestados


class Estudiante(Usuario):
    def __init__(self, nombre, identificacion, tipo_usuario, email, libros_prestados):
        super().__init__(nombre, identificacion, tipo_usuario, email, libros_prestados)

class Profesor(Usuario):
    def __init__(self, nombre, identificacion, tipo_usuario, email, libros_prestados):
        super().__init__(nombre, identificacion, tipo_usuario, email, libros_prestados)