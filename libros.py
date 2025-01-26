from validate import validate_input as validate



class Libro:
    def __init__(self,titulo,autor,ano_publicacion,genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
        self.genero = genero

    def crear_libro(self,libro):
        libro = {
            "titulo": self.titulo,
            "autor": self.autor,
            "ano de publicacion": self.ano_publicacion,
            "genero": self.genero
        }

        return libro

class Biblioteca:
    def __init__(self,libros_disponibles):
        self.nombre = "Biblioteca Nacional"
        self.libros_disponibles = libros_disponibles #esta esperando una lista
        self.usuarios = []
        self.prestamos = []

    def eliminar_libro(self,titulo_libro,ano_libro): #string
        #preguntar
        libro_eliminado = False
        for libro_a_eliminar in self.libros_disponibles:
            if libro_a_eliminar["titulo"] == titulo_libro and libro_a_eliminar["ano de publicacion"] == ano_libro:
                print("El libro se elimino correctamente")
                self.libros_disponibles.remove(libro_a_eliminar)
                libro_eliminado = True
                break
        if not libro_eliminado:
            print(f"El libro {titulo_libro} no se encuentra en la biblioteca.")
            user_choice = validate("Quiere eliminar otro libro? (S/N): ",["S","N"])
            if user_choice == "N":
                print("Thank you for using my program")
                exit()
            elif user_choice == "S":
                self.eliminar_libro(titulo_libro)


    def mostrar_informacion_libro(self,libros_filtrados): #lista
        for libro in libros_filtrados:
            print(f"""
                        Titulo: {libro["titulo"]}
                        Autor: {libro["autor"]}
                        Ano de Publicacion: {libro["ano de publicacion"]}
                        Genero: {libro["genero"]}
                        \n""")
    

    def mostrar_libros_disponibles(self):
        titulos_libros = list(map(lambda x: x["titulo"],self.libros_disponibles))
        if titulos_libros:
            print("Los libros disponibles son: ")
            for libro in titulos_libros:
                print(f"-{libro}")
        else:
            print("No hay ningun libro en la biblioteca")
            

    def filtrar_todo(self,propiedad_libro,propiedad_a_filtrar): #propiedad_libro = genero, propiedad_a_filtrar = horror
        new_list = list(filter(lambda x: x[propiedad_libro] == propiedad_a_filtrar,self.libros_disponibles))
        if new_list:
            self.mostrar_informacion_libro(new_list) #esto tiene que ser un string
        else:
            print(f"No hay ningún libro con {propiedad_libro}: {propiedad_a_filtrar} en la biblioteca")
            user_choice = validate("Quiere usar otro filtro? (S/N): ",["S","N"])
            if user_choice == "N":
                print("Thank you for using my program")
                exit()
            elif user_choice == "S":
                propiedad_libro = input("Decime que propiedad parametro queres usar para el filtro? (Por ejemplo, titulo): ").lower()
                propiedad_a_filtrar = input(f"Decime el {propiedad_libro} a filtrar: ").title()
                self.filtrar_todo(propiedad_libro,propiedad_a_filtrar) 

    def filtrar_por_genero(self,genero):
        self.filtrar_todo("genero",genero)

    def filtrar_por_nombre(self,titulo):
        self.filtrar_todo("titulo",titulo)

    def filtrar_por_fecha(self,fecha):
        self.filtrar_todo("ano de publicacion",fecha)

    def filtrar_por_autor(self,autor):
        self.filtrar_todo("autor",autor)
