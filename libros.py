from validate import validate_input as validate
import json


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
    def __init__(self):
        self.nombre = "Biblioteca Nacional"
        self.libros_disponibles = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro): #espera un objeto
        self.libros_disponibles.append(libro)
        return self.libros_disponibles
        
        
    def eliminar_libro(self,libro):
        #preguntar
        libro_eliminado = False
        for libro_a_eliminar in self.libros_disponibles:
            if libro_a_eliminar["titulo"] == libro["titulo"]:
                print("El libro se elimino correctamente")
                self.libros_disponibles.remove(libro_a_eliminar)
                libro_eliminado = True
                break
        if not libro_eliminado:
            print(f"El libro {libro["titulo"]} no se encuentra en la biblioteca.")
            user_choice = validate("Quiere eliminar otro libro? (S/N): ",["S","N"])
            if user_choice == "N":
                print("Thank you for using my program")
                exit()
            elif user_choice == "S":
                self.eliminar_libro(libro)

    def mostrar_informacion_libro(self,libro):
        libro_encontrado = False
        for libro_disponible in self.libros_disponibles:
            if libro_disponible["titulo"] == libro["titulo"]:
                libro_encontrado = True
                print(f"""
                        Titulo: {libro_disponible["titulo"]}
                        Autor: {libro_disponible["autor"]}
                        Ano de Publicacion: {libro_disponible["ano de publicacion"]}
                        Genero: {libro_disponible["genero"]}
                        \n""")
                break

        if not libro_encontrado:
            print(f"El libro {libro['titulo']} no se encuentra en la biblioteca.")
            user_choice = validate("Quiere ver la informacion de otro libro? (S/N): ", ["S", "N"])
            if user_choice == "N":
                print("Thank you for using my program")
                exit()
            elif user_choice == "S":
                self.mostrar_informacion_libro(libro)

    def mostrar_libros_disponibles(self):
        titulos_libros = list(map(lambda x: x["titulo"],self.libros_disponibles))
        if titulos_libros:
            print("Los libros disponibles son: ")
            for libro in titulos_libros:
                print(libro)
        else:
            print("No hay ningun libro en la biblioteca")
            

    def filtrar_todo(self,propiedad_libro,propiedad_a_filtrar): #propiedad_libro = genero, propiedad_a_filtrar = horror
        new_list = list(filter(lambda x: x[propiedad_libro] == propiedad_a_filtrar,self.libros_disponibles))
        if new_list:
            for libro in new_list:
                self.mostrar_informacion_libro(libro)
        else:
            print(f"No hay ningún libro con {propiedad_libro}: {propiedad_a_filtrar} en la biblioteca")
            user_choice = validate("Quiere usar otro filtro? (S/N): ",["S","N"])
            if user_choice == "N":
                print("Thank you for using my program")
                exit()
            elif user_choice == "S":
                self.filtrar_todo(propiedad_libro,propiedad_a_filtrar)

    def filtrar_por_genero(self,genero):
        self.filtrar_todo("genero",genero)

    def filtrar_por_nombre(self,titulo):
        self.filtrar_todo("titulo",titulo)

    def filtrar_por_fecha(self,fecha):
        self.filtrar_todo("ano de publicacion",fecha)

    def filtrar_por_autor(self,autor):
        self.filtrar_todo("autor",autor)
