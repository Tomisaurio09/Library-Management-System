class Usuario:
    def __init__(self,nombre,tipo_usuario,email,libros_prestados):
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario
        self.email = email
        self.libros_prestados = libros_prestados


class Estudiante(Usuario):
    def __init__(self, nombre,tipo_usuario, email, libros_prestados):
        super().__init__(nombre,tipo_usuario, email, libros_prestados)

class Profesor(Usuario):
    def __init__(self, nombre,tipo_usuario, email, libros_prestados):
        super().__init__(nombre, tipo_usuario, email, libros_prestados)


"""
recomendaciones de libro:

Para Estudiantes:

Título: El señor de los anillos: La comunidad del anillo
Fecha de publicación: 1954
Autor: J.R.R. Tolkien
Género: Fantasía épica

Para Maestros:

Título: Los 7 hábitos de la gente altamente efectiva
Fecha de publicación: 1989
Autor: Stephen R. Covey
Género: Desarrollo personal / Liderazgo
"""
