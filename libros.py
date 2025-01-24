class Libro:
    def __init__(self,titulo,autor,fecha_publicacion,genero):
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.genero = genero

    def crear_libro(self,libro):
        libro = {
            "titulo": self.titulo,
            "autor": self.autor,
            "fecha de publicacion": self.fecha_publicacion,
            "genero": self.genero
        }

        return libro



class Biblioteca:
    def __init__(self,nombre,libros_disponibles,usuarios,prestamos):
        self.nombre = "Biblioteca Nacional"
        self.libros_disponibles = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro): #espera un objeto
        self.libros_disponibles.append(libro)
        

    def eliminar_libro(self,libro):
        if libro["titulo"] in self.libros_disponibles:
            del libro
        else:
            print(f"El libro {libro["titulo"]} no se encuentra en la biblioteca.")
            #implementar funcion para preguntarle al usuario si quiere buscar otro libro para eliminar

    def mostrar_informacion_libro(self,libro):
        if libro["titulo"] in self.libros_disponibles:
            print(f"""
                    Titulo: {libro["titulo"]}
                    Autor: {libro["autor"]}
                    Fecha de Publicacion: {libro["fecha de publicacion"]}
                    Genero: {libro["genero"]}
                    \n""")
        else:
            print(f"El libro {libro["titulo"]} no se encuentra en la biblioteca.")
            #implementar funcion para preguntarle al usuario si quiere buscar otro libro para ver su informacion

    def mostrar_libros_disponibles(self):
        titulos_libros = list(map(lambda x: x["titulos"],self.libros_disponibles))
        if titulos_libros:
            print("Los libros disponibles son: \n")
            for libro in titulos_libros:
                print(libro)
        else:
            print("No hay ningun libro en la biblioteca")
            

    def filtrar_todo(self,propiedad_libro,propiedad_a_filtrar): #propiedad_libro = genero, propiedad_a_filtrar = horror
        new_list = new_list = list(filter(lambda x: x[propiedad_libro] == propiedad_a_filtrar,self.libros_disponibles))
        if new_list:
            for libro in new_list:
                self.mostrar_informacion_libro(libro)
        else:
            print(f"No hay ningún libro con {propiedad_libro}: {propiedad_a_filtrar} en la biblioteca")

    def filtrar_por_genero(self,genero):
        self.filtrar_todo("genero",genero)

    def filtrar_por_nombre(self,titulo):
        self.filtrar_todo("titulo",titulo)

    def filtrar_por_fecha(self,fecha):
        self.filtrar_todo("fecha de publicacion",fecha)

    def filtrar_por_autor(self,autor):
        self.filtrar_todo("autor",autor)
