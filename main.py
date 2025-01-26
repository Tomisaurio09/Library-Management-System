#Crea una aplicación que permita a los usuarios gestionar una biblioteca de libros.

#Branch experiment
#El error es que al agregar la lista con el libro adentro en el JSON, solo se agrega uno porque el archivo se sobreescribe.
#No puedo tener mas de 2 libros


import json
from libros import *
from validate import validate_input as validate

books_file = "libros.json"
users_file = "users.json"

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

if "libreria" not in books:
    books["libreria"] = []

library = Biblioteca(books["libreria"])

def create_books():
    book_title = input("Decime el titulo del libro: ").title()
    book_autor = input("Decime el autor del libro: ").title()
    book_ano_publicacion = input("Decime el año de publicacion del libro: ")
    book_genre = input("Decime el genero del libro: ").title()

    book_object = Libro(book_title,book_autor,book_ano_publicacion,book_genre)

    book = book_object.crear_libro(book_object)
    print("El libro se creo correctamente")

    return book


def introduction():
    print("Hello User!\n")
    print("Este es un sistema de biblioteca")
    print("Por ahora, podes interactuar con libros, agregar,eliminar,filtrar,ver sus detalles,etc")

def filter_introduction():
    print("Decime que filtro queres aplicar: \n")
    print("""
        1. Title of the book
        2. Author of the book
        3. Year of release of the book
        4. Gender of the book
        5. Exit
            """)

def main():
    introduction()

    print("\nWhat do you want to do?")
    print("""
        1. Create a book and Add the book to the library
        2. Delete the book from the library
        3. Show all the books in the library
        4. Search a book using a filter
        5. Exit the program
            """)

    user_choice = validate("Choose one of the available options: ", ["1", "2", "3", "4", "5"])

    if user_choice == "1":
        creating_book = create_books()
        books["libreria"].append(creating_book)
        try:
            with open(books_file, "w") as file:
                json.dump(books, file, indent=4)
        except Exception as e:
            print(f"An unexpected error occurred while writing to the file: {e}")

    elif user_choice == "2":
        book_to_remove_name = input("Decime el titulo del libro que queres eliminar: ").title()
        book_to_remove_ano = input("Decime en que año salio el libro que queres eliminar: ")  # Pides la información del libro a eliminar
        library.eliminar_libro(book_to_remove_name,book_to_remove_ano)
        books["libreria"] = library.libros_disponibles
        try:
            with open(books_file, "w") as file:
                json.dump(books, file, indent=4)
        except Exception as e:
            print(f"An unexpected error occurred while writing to the file: {e}")
    elif user_choice == "3":
        library.mostrar_libros_disponibles()

    elif user_choice == "4":
        filter_introduction()
        user_choice_filter = validate("Choose one of the available options: ", ["1", "2", "3", "4", "5"])

        if user_choice_filter == "1":
            book_title = input("Decime el titulo del libro a filtrar: ").title()
            library.filtrar_por_nombre(book_title)

        elif user_choice_filter == "2":
            book_author = input("Decime el nombre del autor del libro a filtrar: ").title()
            library.filtrar_por_autor(book_author)
        
        elif user_choice_filter == "3":
            book_year = input("Decime el año en el que salio el libro a filtrar: ")
            library.filtrar_por_fecha(book_year)

        elif user_choice_filter == "4":
            book_gender = input("Decime el genero del libro a filtrar: ").title()
            library.filtrar_por_genero(book_gender)
        
        elif user_choice_filter == "5":
            print("Thanks for using my program")
            exit()
    elif user_choice == "5":
        print("Thanks for using my program")
        exit()
if __name__ == "__main__":
    main()
