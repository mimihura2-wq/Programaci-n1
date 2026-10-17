#Crear una lista
biblioteca_1 = []
biblioteca_2 = []

def agregar_libro(biblioteca,titulo):
    #agregar a la Biblioteca
    biblioteca.append(titulo)
    print("libro agregado: ", titulo)
    
#Eliminar libros   
def eliminar_libro(biblioteca,titulo):
    if titulo in biblioteca:
        biblioteca.remove(titulo)
        print("libro borrado: ", titulo)
    else:
        print("Este libro no existe en la Biblioteca")

def buscar_libro(biblioteca,titulo):
    if titulo in biblioteca:
        print("Libro encontrado: ", titulo)
    else:
        print("Ese libro no fue encontrado.")

def mostrar_libros(biblioteca):
    if len(biblioteca) == 0:
        print("No hay libros en la biblioteca.")
    else:
        print("libros disponibles: ")
        for libro in biblioteca:
            print("-", libro)
        
    
agregar_libro(biblioteca_1, "Educar Sin Culpas")
agregar_libro(biblioteca_2, "Basta de Tanto")
agregar_libro(biblioteca_1, "50 Sombras de Gray")
agregar_libro(biblioteca_2, "Harry Potter")
buscar_libro(biblioteca_1, "Harry Potter")
eliminar_libro(biblioteca_2, "Basta de Tanto")
mostrar_libros(biblioteca_1)
mostrar_libros(biblioteca_2)
