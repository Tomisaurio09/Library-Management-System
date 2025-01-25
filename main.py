#Crea una aplicación que permita a los usuarios gestionar una biblioteca de libros.

#Esta branch tiene algunos errores en cuanto agregar la lista con los libros al archivo JSON
#Por eso voy a hacer una branch aparte.



import json
from libros import *
from validate import validate_input as validate

books_file = "libros.json"
users_file = "users.json"
library = Biblioteca()
try:
    with open(books_file, 'r') as file:
        books = json.load(file)
except FileNotFoundError:
    print(f"Error: The file '{books_file}' is not found.")
    books = {}
except json.JSONDecodeError:
    print(f"Error: The file '{books_file}' contains invalid JSON data.")
    books = {}
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")
    books = {}


def create_books():
    book_title = input("Decime el titulo del libro: ").title()
    book_autor = input("Decime el autor del libro: ").title()
    book_ano_publicacion = input("Decime el año de publicacion del libro: ")
    book_genre = input("Decime el genero del libro: ").title()

    book_object = Libro(book_title,book_autor,book_ano_publicacion,book_genre)

    book = book_object.crear_libro(book_object)
    print("El libro se creo correctamente")

    return book

#returned_book = create_books()

#def add_book_to_library(book,library):
    library.agregar_libro(book)
    return library

#libreria = add_book_to_library(returned_book,library)

#def eliminar(library,book):
    del_book = input("Decime el nombre del libro que queres eliminar: ").title()
    if del_book == book["titulo"]:
        library.eliminar_libro(book)
        return
    else:
        print("No elegiste un libro valido")
        user_choice = validate("Queres probar de nuevo? (S/N): ",["S","N"])
        if user_choice == "N":
            print("Thank you for using my program")
            exit()
        elif user_choice == "S":
            eliminar(library,book)

#eliminar(library,returned_book)

def introduction():
    print("Hello User!\n")
    print("Este es un sistema de biblioteca")
    print("Por ahora, podes interactuar con libros, agregar,eliminar,filtrar,ver sus detalles,etc")


def main():
    introduction()

    print("\nWhat do you want to do?")
    print("""
        1. Create a book and Add the book to the library
        2. Delete the book from the library
        3. Show all the books in the library
        4. Show information about one specific book
        5. Search a book using a filter
        6. Exit the program
            """)
    
    user_choice = validate("Choose one of the available options: ", ["1", "2", "3", "4", "5","6"])

    if user_choice == "1":
        creating_book = create_books()
        new_book = library.agregar_libro(creating_book)
        try:
            with open(books_file, "w") as file:
                json.dump(new_book, file, indent=4)
        except Exception as e:
            print(f"An unexpected error occurred while writing to the file: {e}")


if __name__ == "__main__":
    main()
